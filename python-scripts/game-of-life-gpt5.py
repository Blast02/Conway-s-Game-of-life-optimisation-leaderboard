# prompt: make a game of life in python with a grid of 1280*720 with 128*72 cells

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from time import perf_counter

# Display size
FIG_WIDTH_PX  = 1280
FIG_HEIGHT_PX = 720
CELL_SIZE_PX  = 10

# Grid size
COLS = FIG_WIDTH_PX  // CELL_SIZE_PX   # 128
ROWS = FIG_HEIGHT_PX // CELL_SIZE_PX   # 72

# Settings
SEED = 1337
STEPS = 5000

# Colormap : 0=blanc, 1=vert
cmap = ListedColormap(["black", "green"])

def count_neighbors(grid):
    total = np.zeros(grid.shape, dtype=int)
    shifts = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
    for dy, dx in shifts:
        total += np.roll(np.roll(grid, dy, axis=0), dx, axis=1)
    return total

def step(grid):
    neighbors = count_neighbors(grid)
    survive = ((grid == 1) & ((neighbors == 2) | (neighbors == 3)))
    born = ((grid == 0) & (neighbors == 3))
    return np.where(survive | born, 1, 0).astype(np.uint8)

def main():
    # Initiate unique grid
    rng = np.random.default_rng(seed=SEED)
    grid = rng.integers(0, 2, size=(ROWS, COLS), dtype=int)

    fig, ax = plt.subplots(figsize=(FIG_WIDTH_PX/100, FIG_HEIGHT_PX/100), dpi=100)
    im = ax.imshow(grid, interpolation='nearest', aspect='equal', cmap=cmap, vmin=0, vmax=1)

    # White grid
    ax.set_xticks(np.arange(-0.5, COLS, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, ROWS, 1), minor=True)
    ax.grid(which="minor", color="white", linestyle='-', linewidth=0.2)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    generation = {'n': 0, 't0': None}

    def update(_):
        grid_next = step(update.grid)
        update.grid = grid_next
        im.set_data(grid_next)

        if generation['n'] == 0:
            generation['t0'] = perf_counter()

        generation['n'] += 1

        if generation['n'] == STEPS:
            t_elapsed = perf_counter() - generation['t0']
            print(f"Temps pour {STEPS} générations : {t_elapsed:.3f} s")
            anim.event_source.stop()

        return (im,)

    update.grid = grid
    anim = animation.FuncAnimation(fig, update, frames=None, interval=0, blit=True)
    plt.show()

if __name__ == "__main__":
    main()