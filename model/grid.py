# pyright: strict
from model.game_config import GameConfig
from model.cell import Cell
from random import Random

class Grid:
    def __init__(self, config: GameConfig):
        self.__config = config
        self.__r = config.rows
        self.__c = config.cols
        self.__grid: list[list[Cell]] = [[Cell(j, i, is_tunnel=False) for j in range(self.__config.cols)] for i in range(self.__config.rows)] # no tunnels for now
        self.__rng = Random(12) # fixed seed

    def get_cell_from_click(self, mouse_x: int, mouse_y: int, top_padding: int = 30) -> Cell | None:
        col = mouse_x // 40
        row = (mouse_y - top_padding) // 40
        if 0 <= row < self.__r and 0 <= col < self.__c:
            return self.__grid[row][col]
        return None
    
    @property 
    def r(self) -> int:
        return self.__r

    @property
    def c(self) -> int:
        return self.__c 
    
    @property
    def grid(self) -> list[list[Cell]]:
        return self.__grid