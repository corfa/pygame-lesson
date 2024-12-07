import pygame
from pygame.surface import Surface

from labyrinth.core.config import Config


class Character:
    def __init__(self, config: Config,
                 x_position: int,
                 y_position: int,
                 color: tuple[int, int, int]):
        self.x: int = x_position
        self.y: int = y_position
        self.game_config: Config = config
        self.color = color
        self.rect = pygame.Rect(self.x * self.game_config.tile_size,
                                self.y * self.game_config.tile_size,
                                self.game_config.tile_size,
                                self.game_config.tile_size)

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx: int, dy: int, maze: list) -> None:
        new_x = self.x + dx
        new_y = self.y + dy
        if maze[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x * self.game_config.tile_size,
                                 self.y * self.game_config.tile_size)
