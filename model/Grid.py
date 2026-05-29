# pyright: strict
from game_config import GameConfig
from cell import Cell

class Grid:
    def __init__(self, config: GameConfig):
        self.__config = config
        self.__grid: list[list[Cell]] = [[Cell(j, i, is_tunnel=False) for j in range(self.__config.cols)] for i in range(self.__config.rows)]