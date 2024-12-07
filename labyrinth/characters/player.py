from labyrinth.core.config import Config
from labyrinth.characters.character import Character


class Player(Character):
    """"""
    def __init__(self, config: Config,
                 x_position: int,
                 y_position: int) -> None:

        super().__init__(config, x_position=x_position,
                         y_position=y_position, color=(0, 255, 0))
