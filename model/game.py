# pyright: strict
from player import Player
from stage import Stage
from round import Round
from utils import *
from game_config import GameConfig
from random import Random

class Game:
    def __init__(self, config: GameConfig, mode: GameMode):
        self.__player = Player(config)
        self.__stage = Stage(config)
        self.__rounds: list[Round] = [self.create_round() for _ in range(12)] # at least 12 rounds
        self.__enemies = config.enemies
        self.__current_round = 0
        self.__exp = 0
        self.__mode = mode
        self.__rng = Random(12) # fixed seed
    
    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @property
    def current_round(self) -> int:
        return self.__current_round
    
    def create_round(self) -> Round:
        config = WaveConfig(
            self.__rng.choices(list(Color), k=self.__enemies),
            self.__rng.choices(self.__stage.paths, k=self.__enemies),
            self.__rng.choices(list(EnemyType), k=self.__enemies)
        )
        return Round(config)
    
    # TODO update, is_game_over