# Version 4 of the Python Game of Life implementation:
# - Pre calculate white grid instead of drawing each line with python for loop each frame
# - Move neighbors_grid to global instead of write it to memory in each alive() call fonction



import numpy
import pygame
import time

window_width = 1280
window_height = 720
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
GREEN = (0, 254, 0)
cell = 10 # size of one cell
tick = 0
nb_tick = 5000 # number of iterations

rng = numpy.random.default_rng(seed=1337) #seed set to 1337
current_grid = rng.integers(0, 2, size=(int(window_height / cell), int(window_width / cell)), dtype=int)
next_grid = current_grid.copy()
neighbors_grid = [(-1, -1), (-1, 0), (-1, 1), # move neighbors_grid to global save memory write
		(0, -1),           (0, 1),
  		(1, -1),  (1, 0),  (1, 1)]

white_grid = pygame.Surface((window_width, window_height), pygame.SRCALPHA) # pre calculate white grid
for x in range(0, window_width, cell):
    pygame.draw.line( white_grid, WHITE, (x, 0), (x, window_height))
for y in range(0, window_height, cell):
    pygame.draw.line( white_grid, WHITE, (0, y), (window_width, y))
pygame.draw.rect( white_grid, WHITE, (0, 0, window_width, window_height), width=1)

pygame.init()
frame = pygame.display.set_mode([window_width, window_height])
clock = pygame.time.Clock()
frame.fill(BLACK)
main = True
frozen = False

def alive(current_grid): #process each cell to determine the next state
    nb_cells = numpy.zeros_like(current_grid)

    for dy, dx in neighbors_grid:
        nb_cells += numpy.roll(numpy.roll(current_grid, dy, axis=0), dx, axis=1)

    survive = ((current_grid == 1) & ((nb_cells == 2) | (nb_cells == 3)))
    born = ((current_grid == 0) & (nb_cells == 3))
    next_grid = numpy.where(survive | born, 1, 0)
    return next_grid

def draw_alive(next_grid): #draw a green rectangle to each 1 in the grid
	frame.fill(BLACK)

	for r in range(next_grid.shape[0]):
		for c in range(next_grid.shape[1]):
			if next_grid[r, c] == 1:
				frame.fill(GREEN, (c*cell, r*cell, cell, cell))
	frame.blit(white_grid, (0, 0)) # draw pre calculate grid


start = time.perf_counter()
while main: # main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			main = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				main = False

	if not frozen: # tick and time counter
		next_grid = alive(current_grid)
		draw_alive(next_grid)
		current_grid = next_grid.copy()
		tick += 1
		if tick >= nb_tick:
			end = time.perf_counter()
			print("time:",end - start)
			print("tick/s:",tick / (end - start))
			frozen = True

	if main:			
		pygame.display.flip()

pygame.quit()
