# pyright: strict
from model.player import Player
from model.stage import Stage
from model.round import Round
from model.utils import *
from model.game_config import GameConfig
from model.entities.tower import Tower
from model.entities.bullet import Bullet
from random import Random

class Model:
    def __init__(self, config: GameConfig, mode: GameMode):
        self.__player = Player(config)
        self.__stage = Stage(config)
        self.__enemies = config.enemies
        self.__current_round = 0
        self.__exp = 0
        self.__mode = mode
        self.__rng = Random(12) # fixed seed
        self.__rounds: list[Round] = [self.create_round() for _ in range(12)] # at least 12 rounds
        self.__config = config
        self.__towers: list[Tower] = []
        self.__bullets: list[Bullet] = []

    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @property
    def player(self) -> GameConfig:
        return self.__config
    
    @property
    def config(self) -> GameConfig:
        return self.__config
    
    @property
    def current_round(self) -> int:
        return self.__current_round
    
    @property
    def rng(self) -> Random:
        return self.__rng

    @property
    def rounds(self) -> list[Round]:
        return self.__rounds
    
    @property
    def stage(self) -> Stage:
        return self.__stage

    @property
    def enemy_count(self) -> int:
        return self.__enemies
    
    @property
    def towers(self) -> list[Tower]:
        return self.__towers
    
    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets

    def create_round(self) -> Round:
        config = WaveConfig(
            self.rng.choices(list(Color), k=self.__enemies),
            [self.rng.randint(0, len(self.__stage.paths) - 1) for _ in range(self.__enemies)],
            self.rng.choices(list(EnemyType), k=self.__enemies)
        )
        return Round(config, self.__stage.paths)
    
    @property
    def is_game_over(self) -> bool:
        return self.__current_round >= len(self.__rounds) if self.mode == GameMode.CAMPAIGN else self.player.lives <= 0
    
    def add_exp(self, amount: int):
        self.__exp += amount

    def lose_life(self):
        self.__player.lose_life()
    
    def advance_next_round(self):
        self.__current_round += 1
        self.__bullets.clear()
