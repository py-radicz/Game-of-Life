import pygame
import sys
import random
from pygame.locals import *

FPS = 10
WINDOW = 500
CELLSIZE = 5
PADDING = (WINDOW // CELLSIZE) - 1
assert WINDOW % CELLSIZE == 0, "win size must be a multiple of cell"


class Board():

	def __init__(self):

		pygame.init()
		pygame.display.set_caption('Game of Life')
		self.screen = pygame.display.set_mode((WINDOW + PADDING, WINDOW + PADDING))
		self.grid = [[0] * (WINDOW // CELLSIZE) for i in range(WINDOW // CELLSIZE)]

	def draw(self):
		for i, x in enumerate(range(0, WINDOW + PADDING, CELLSIZE + 1)):
			for j, y in enumerate(range(0, WINDOW + PADDING, CELLSIZE + 1)):

				if self.grid[i][j] == 0:
					color = (20, 120, 20)
				else:
					color = (255, 255, 255)

				pygame.draw.rect(self.screen, color, Rect((x, y), (CELLSIZE, CELLSIZE)))

	def randomize(self):
		for i in range(1, (WINDOW // CELLSIZE) - 1):
			for j in range(1, (WINDOW // CELLSIZE) - 1):

				if random.randint(0, 100) < 50:
					self.grid[i][j] = 1

	def rules(self):
		new_grid = [[0] * (WINDOW // CELLSIZE) for i in range(WINDOW // CELLSIZE)]

		for i in range(1, (WINDOW // CELLSIZE) - 1):
			for j in range(1, (WINDOW // CELLSIZE) - 1):

				if self.grid[i][j] == 0:

					neighbors = self.grid[i + 1][j] + self.grid[i - 1][j] + \
						self.grid[i][j + 1] + self.grid[i][j - 1] + self.grid[i - 1][j - 1]\
						+ self.grid[i + 1][j + 1] + self.grid[i + 1][j - 1]\
						+ self.grid[i - 1][j + 1]

					if neighbors == 3:
						new_grid[i][j] = 1
					else:
						new_grid[i][j] = 0

				if self.grid[i][j] == 1:

					neighbors = self.grid[i + 1][j] + self.grid[i - 1][j] + \
						self.grid[i][j + 1] + self.grid[i][j - 1] + self.grid[i - 1][j - 1]\
						+ self.grid[i + 1][j + 1] + self.grid[i + 1][j - 1]\
						+ self.grid[i - 1][j + 1]

					if neighbors < 2:
						new_grid[i][j] = 0
					elif neighbors > 3:
						new_grid[i][j] = 0
					else:
						new_grid[i][j] = 1

		self.grid = new_grid

	def mainloop(self):
		fps_clock = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			self.rules()
			self.draw()
			pygame.display.update()
			fps_clock.tick(FPS)


board = Board()
board.randomize()
board.mainloop()
