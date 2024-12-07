import pygame

from labyrinth.core.config import Config
from labyrinth.characters.enemy import Enemy
from labyrinth.characters.player import Player
from labyrinth.maze import Maze


class Game:
    def __init__(self, config: Config) -> None:
        pygame.init()
        self.game_config = config
        self.screen = pygame.display.set_mode((self.game_config.width,
                                              self.game_config.height))

        pygame.display.set_caption(self.game_config.lable)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(config=self.game_config, x_position=1, y_position=1)
        self.enemy = Enemy(config=self.game_config, x_position=7, y_position=7)
        self.maze = Maze(config=self.game_config)

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(self.game_config.FPS)
        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1, 0, self.maze.map)
        if keys[pygame.K_RIGHT]:
            self.player.move(1, 0, self.maze.map)
        if keys[pygame.K_UP]:
            self.player.move(0, -1, self.maze.map)
        if keys[pygame.K_DOWN]:
            self.player.move(0, 1, self.maze.map)

    def update_game(self) -> None:
        self.enemy.move(self.maze.map)
        if self.player.rect.colliderect(self.enemy.rect):
            self.running = False

    def draw_game(self) -> None:
        self.screen.fill((0, 0, 0))
        self.maze.draw_map(self.screen)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pygame.display.flip()
