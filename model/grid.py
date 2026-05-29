# pyright: strict
from game_config import GameConfig
from cell import Cell
from random import Random

class Grid:
    def __init__(self, config: GameConfig):
        self.__config = config
        self.__r = config.rows
        self.__c = config.cols
        self.__grid: list[list[Cell]] = [[Cell(j, i, is_tunnel=False) for j in range(self.__config.cols)] for i in range(self.__config.rows)] # no tunnels for now
        self.__rng = Random(12) # fixed seed

    @property 
    def r(self) -> int:
        return self.__r

    @property
    def c(self) -> int:
        return self.__c 
    
    @property
    def grid(self) -> list[list[Cell]]:
        return self.__grid