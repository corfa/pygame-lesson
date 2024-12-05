from labyrinth.game import Game
from labyrinth.core.config import config_game


def main() -> None:
    game = Game(config=config_game)
    game.run()


if __name__ == "__main__":
    main()
