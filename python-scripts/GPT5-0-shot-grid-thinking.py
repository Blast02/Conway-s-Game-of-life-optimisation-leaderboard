# Prompt: Make the fastest conway game of life possible.
# follow those rules :
# - use python
# - The game must be rendered in a 1280×720 window. You CAN'T use the terminal for rendering the game.
# - Each cell is 2 pixels, resulting in a grid of 640×360 cells
# -  Initialize the grid using the following code: """rng = numpy.random.default_rng(seed=1337) 
#    current_grid = rng.integers(0, 2, size=(int(window_height / cell), int(window_width / cell)), dtype=int)"""
# - The grid must wrap around (no walls)
#- use perf_counter() to measure the time taken for 500 steps
# - black background, to visually separate each cell and a distinct color for the live cells
# GPT anwser
#
# it's missing the white grid like this {photo}
#


import numpy as np
import pygame
from time import perf_counter

# Window / grid parameters
window_width = 1280
window_height = 720
cell = 2  # px per cell

cols = int(window_width // cell)   # 640
rows = int(window_height // cell)  # 360

# Initialize grid using the exact RNG code you requested
rng = np.random.default_rng(seed=1337)
current_grid = rng.integers(
    0, 2, size=(int(window_height / cell), int(window_width / cell)), dtype=int
)

# Colors
BG_COLOR = (0, 0, 0)        # black background
LIVE_COLOR = (0, 200, 80)   # live cells (green-ish)
GRID_COLOR = (255, 255, 255)  # white grid lines

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Conway's Game of Life — fast (numpy + pygame) + grid")
clock = pygame.time.Clock()

# Vectorized Game of Life step using np.roll (wrap-around)
def step(grid):
    n = (
        np.roll(grid, 1, 0) + np.roll(grid, -1, 0) +
        np.roll(grid, 1, 1) + np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, 1, 0), 1, 1) + np.roll(np.roll(grid, 1, 0), -1, 1) +
        np.roll(np.roll(grid, -1, 0), 1, 1) + np.roll(np.roll(grid, -1, 0), -1, 1)
    )
    new = ((n == 3) | ((grid == 1) & (n == 2))).astype(np.uint8)
    return new

# Render function: create small rgb array (rows x cols x 3) -> surface -> scale -> blit
def render(grid):
    # small rgb: one pixel per cell (rows x cols x 3)
    rgb = np.zeros((rows, cols, 3), dtype=np.uint8)
    rgb[grid == 1] = LIVE_COLOR
    # make_surface expects (width, height, 3) so transpose
    surf = pygame.surfarray.make_surface(np.transpose(rgb, (1, 0, 2)))
    scaled = pygame.transform.scale(surf, (window_width, window_height))
    screen.blit(scaled, (0, 0))

# Draw 1-pixel white grid lines on top of the scaled cells
def draw_grid():
    # vertical lines
    for x in range(0, window_width, cell):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, window_height - 1), 1)
    # horizontal lines
    for y in range(0, window_height, cell):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (window_width - 1, y), 1)

# MAIN
running = True
measure_steps = 501
steps_done = 0
timing_started = False
start_time = 0.0
elapsed_update_time = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start timing at the first update
    if not timing_started:
        timing_started = True
        start_time = perf_counter()

    # Update (measure only the update computation)
    current_grid = step(current_grid)
    steps_done += 1

    # When we've completed the measured number of steps, stop timer and print
    if steps_done == measure_steps:
        end_time = perf_counter()
        elapsed_update_time = end_time - start_time
        print(f"Time for {measure_steps} update steps (numpy neighbor calc + rules): {elapsed_update_time:.6f} seconds")
        pygame.display.set_caption(f"Conway's Game of Life — {measure_steps} steps update time: {elapsed_update_time:.6f}s")

    # Render
    screen.fill(BG_COLOR)
    render(current_grid)
    # overlay the white grid lines (1 px)
    draw_grid()
    pygame.display.flip()
    # No fps cap so it runs as fast as it can; uncomment to cap: clock.tick(60)

pygame.quit()
