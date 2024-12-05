from labyrinth.core.config import Config
from labyrinth.characters.character import Character


class Player(Character):
    def __init__(self, config: Config,
                 x_position: int = 1,
                 y_position: int = 1) -> None:

        super().__init__(config, x_position, y_position)
