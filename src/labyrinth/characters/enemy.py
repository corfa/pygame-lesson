import random

from labyrinth.core.config import Config
from labyrinth.characters.character import Character


class Enemy(Character):
    def __init__(self, config: Config,
                 x_position: int = 7,
                 y_position: int = 7) -> None:

        super().__init__(config, x_position, y_position, color=(255, 0, 0))

    def move(self, maze: list) -> None:
        directions: list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if maze[new_y][new_x] == 0:
                self.x = new_x
                self.y = new_y
                self.rect.topleft = (self.x * self.game_config.tile_size,
                                     self.y * self.game_config.tile_size)
                break
