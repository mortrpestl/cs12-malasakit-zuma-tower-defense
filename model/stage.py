# pyright: strict
from model.game_config import GameConfig
from model.grid import Grid
from model.path import Path
from model.cell import Cell
import json
from pathlib import Path as FilePath

class Stage:
    def __init__(self, config: GameConfig, file: str = "campaign_map_1.json"):
        self.__config = config
        self.__grid = Grid(config, file)
        self.__paths = [Path(i) for i in self.load_path_from_json(file)]
    
    @property
    def paths(self) -> list[Path]:
        return self.__paths
    
    @property
    def grid(self) -> Grid:
        return self.__grid
    
    def load_path_from_json(self, file: str) -> list[list[Cell]]:
        map_path = FilePath(__file__).parent / "map" / file

        with open(map_path, "r") as f:
            data = json.load(f)
            data_paths: list[list[list[int]]] = data["paths"]

            paths: list[list[Cell]] = []

            for path in data_paths:
                p: list[Cell] = []

                for tile in path:
                    p.append(self.__grid.grid[tile[0]][tile[1]])

                paths.append(p)

        return paths   
    
