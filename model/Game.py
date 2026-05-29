# pyright: strict
from player import Player
from stage import Stage
from round import Round
from utils import *
from game_config import GameConfig
from grid import Grid

class Game:
    def __init__(self, config: GameConfig, mode: GameMode):
        self.__player = Player(config)
        self.__stage = Stage()
        self.__rounds: list[Round] = []
        self.__current_round = 0
        self.__exp = 0
        self.__mode = mode
        self.__grid = Grid(config)
    
    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @property
    def current_round(self) -> int:
        return self.__current_round
    
    # TODO game methods