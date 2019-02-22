from pygame.locals import QUIT, Rect
import numpy as np
import random
import pygame
import sys


class Board:
    def __init__(self, grid_size, cell_size):
        self.FPS = 10
        self.dead_color = (20, 120, 20)
        self.alive_color = (255, 255, 255)
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.window_size = (self.grid_size * self.cell_size) - 1
        print(self.window_size)

        self.grid = {
            (x * self.cell_size, y * self.cell_size): random.choice(
                [self.dead_color, self.alive_color]
            )
            for x in range(self.grid_size)
            for y in range(self.grid_size)
        }

        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))

    def __draw(self):
        for coords, color in self.grid.items():
            pygame.draw.rect(
                self.screen,
                color,
                Rect(coords, (self.cell_size - 1, self.cell_size - 1)),
            )

    def __count_neighbors(self, coords):
        coords = np.array([coords] * 8)
        directions = np.array(
            [
                (0, -self.cell_size),
                (self.cell_size, -self.cell_size),
                (-self.cell_size, -self.cell_size),
                (0, self.cell_size),
                (self.cell_size, self.cell_size),
                (-self.cell_size, self.cell_size),
                (self.cell_size, 0),
                (-self.cell_size, 0),
            ]
        )

        neighbors = []
        for direction in (coords + directions).tolist():
            if (
                len(
                    [
                        x
                        for x in direction
                        if x >= 0 and x < self.cell_size * self.grid_size
                    ]
                )
                < 2
            ):
                neighbors.append(self.dead_color)
            else:
                neighbors.append(self.grid[tuple(direction)])

        return neighbors.count(self.alive_color)

    def __apply_rules(self):
        new_grid = {}
        for coords in self.grid:
            if self.grid[coords] == self.dead_color:
                n = self.__count_neighbors(coords)
                if n == 3:
                    new_grid[coords] = self.alive_color
                else:
                    new_grid[coords] = self.dead_color

            if self.grid[coords] == self.alive_color:
                n = self.__count_neighbors(coords)
                if n < 2:
                    new_grid[coords] = self.dead_color
                elif n > 3:
                    new_grid[coords] = self.dead_color
                else:
                    new_grid[coords] = self.alive_color

        self.grid = new_grid

    def create_life(self):
        fps_clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.__apply_rules()
            self.__draw()
            pygame.display.update()
            fps_clock.tick(self.FPS)


if __name__ == "__main__":
    Board(grid_size=100, cell_size=6).create_life()
