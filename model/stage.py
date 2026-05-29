# pyright: strict
from game_config import GameConfig
from grid import Grid
from path import Path

class Stage:
    def __init__(self, config: GameConfig):
        self.__config = config
        self.__grid = Grid(config)
        # basic paths for now
        right = [self.__grid.grid[0][i] for i in range(config.cols)] + [self.__grid.grid[i][-1] for i in range(1, config.rows)]
        down = [self.__grid.grid[i][0] for i in range(config.rows)] + [self.__grid.grid[-1][i] for i in range(1, config.cols)]
        self.__paths = [Path(right), Path(down)]
    
    @property
    def paths(self) -> list[Path]:
        return self.__paths