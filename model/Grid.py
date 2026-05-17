# pyright: strict
from game_config import GameConfig
from entities.Entity import Entity

class Grid:
    def __init__(self, config: GameConfig):
        self.__config = config
        self.__grid: list[list[Entity | None]] = [[None for _ in range(self.__config.cols)] for _ in range(self.__config.rows)]