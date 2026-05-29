# pyright: strict
from model.player import Player
from model.stage import Stage
from model.round import Round
from model.utils import *
from model.game_config import GameConfig
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

    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @property
    def current_round(self) -> int:
        return self.__current_round
    
    @property
    def rng(self) -> Random:
        return self.__rng

    @property
    def rounds(self) -> list[Round]:
        return self.__rounds

    def create_round(self) -> Round:
        config = WaveConfig(
            self.rng.choices(list(Color), k=self.__enemies),
            [self.rng.randint(0, len(self.__stage.paths) - 1) for _ in range(self.__enemies)],
            self.rng.choices(list(EnemyType), k=self.__enemies)
        )
        return Round(config, self.__stage.paths)
    
    # TODO update, is_game_over