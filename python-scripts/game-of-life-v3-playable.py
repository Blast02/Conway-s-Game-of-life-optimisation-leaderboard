# Version 3 of the Python Game of Life playable implementation:
# - Can pause game
# - Place / remove cell
# - Speed up / down simulation



import numpy
import pygame
import time

window_width = 1280
window_height = 720
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
GREEN = (0, 254, 0)
cell = 10 # size of one cell
fps = 0

#rng = numpy.random.default_rng(seed=1337) #seed set to 1337
#current_grid = rng.integers(0, 2, size=(int(window_height / cell), int(window_width / cell)), dtype=int)
current_grid = numpy.zeros((int(window_height / cell), int(window_width / cell)), dtype=int)
next_grid = current_grid.copy()

pygame.init()
frame = pygame.display.set_mode([window_width, window_height])
speed = pygame.time.Clock()
frame.fill(BLACK)
main = True

def grid(): #draw white grid
	for x in range(0, window_width, cell):
		pygame.draw.line(frame, WHITE, (x, 0), (x, window_height))
	for y in range(0, window_height, cell):
		pygame.draw.line(frame, WHITE, (0, y), (window_width, y))	
	pygame.draw.rect(frame, WHITE, (0, 0, window_width, window_height), width=1)

def alive(current_grid): #process each cell to determine the next state
    nb_cells = numpy.zeros_like(current_grid)
    neighbors_grid = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]
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
# remove unnecessary draw screen update

pause = False

while main: # main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			main = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				main = False

		if event.type == pygame.KEYDOWN: # right arrow to speed up
			if event.key == pygame.K_RIGHT:
				fps += 1
				print(fps)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: #lift arrow to speed down
				if fps > 1:
					fps -= 1
					print(fps)

		if event.type == pygame.KEYUP:# space to pause game
			if event.key == pygame.K_SPACE:
				pause = True

				while pause:
					for event in pygame.event.get():

						if event.type == pygame.MOUSEBUTTONDOWN: #left clic to add 1 cell
							mouse_y, mouse_x = pygame.mouse.get_pos()
							grid_y, grid_x = (mouse_y // cell), (mouse_x // cell)
							if event.button == 1:
								current_grid[grid_x, grid_y] = 1
							elif event.button == 3: # right clic to remove 1 cell
								current_grid[grid_x, grid_y] = 0

						if event.type == pygame.MOUSEMOTION:
							if event.buttons[0]: #hold left clic to add cells
								mouse_y, mouse_x = event.pos
								grid_y, grid_x = (mouse_y // cell), (mouse_x // cell)
								current_grid[grid_x, grid_y] = 1

							elif event.buttons[2]: #hold right clic to remove cells
								mouse_y, mouse_x = event.pos
								grid_y, grid_x = (mouse_y // cell), (mouse_x // cell)
								current_grid[grid_x, grid_y] = 0

						if event.type == pygame.KEYUP:
							if event.key == pygame.K_SPACE:
								pause = False

					for r in range(current_grid.shape[0]):
						for c in range(current_grid.shape[1]):
							button_rect = pygame.Rect(c*cell, r*cell, cell, cell)

					draw_alive(current_grid)
					grid()
					pygame.display.flip()

	next_grid = alive(current_grid)
	draw_alive(next_grid)
	grid()
	current_grid = next_grid.copy()
	speed.tick(fps)

	if main:			
		pygame.display.flip()

pygame.quit()
