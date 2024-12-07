import pygame
from pygame.surface import Surface

from labyrinth.core.config import Config


def create_map() -> list[list[int]]:
    return [
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


class Maze:
    def __init__(self, config: Config) -> None:
        self.game_config: Config = config
        self.map: list[list[int]] = create_map()

    def draw_map(self, screen: Surface) -> None:
        for x, y in self.get_tiles():
            self.draw_tile(screen, x, y)

    def get_tiles(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 1:
                    yield x, y

    def draw_tile(self, screen, x, y) -> None:
        pygame.draw.rect(
            screen, self.game_config.color_white,
            (x * self.game_config.tile_size,
             y * self.game_config.tile_size,
             self.game_config.tile_size,
             self.game_config.tile_size)
        )
