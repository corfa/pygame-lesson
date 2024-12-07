from dataclasses import dataclass


@dataclass
class Config:
    lable: str = "labyrinth"
    FPS: int = 10

    width: int = 800
    height: int = 600
    tile_size: int = 40

    color_white: tuple[int, int, int] = (255, 255, 255)
    color_black: tuple[int, int, int] = (0, 0, 0)


config_game = Config()
