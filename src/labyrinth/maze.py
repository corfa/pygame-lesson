import pygame
from pygame.surface import Surface

from labyrinth.core.config import Config


class Maze:
    def __init__(self, config: Config) -> None:
        self.game_config: Config = config
        self.map: list = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

    def draw_map(self, screen: Surface) -> None:
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(
                        screen, self.game_config.color_white,
                        (x * self.game_config.tile_size,
                         y * self.game_config.tile_size,
                         self.game_config.tile_size,
                         self.game_config.tile_size)
                    )
