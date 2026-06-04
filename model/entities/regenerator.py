# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Regenerator(Enemy):
    def __init__(self, color: Color, path: Path, regen_interval: int = 2):
        super().__init__(color, path)
        self.__regen_interval = regen_interval
        self.__tiles_moved = 0
    
    @property
    def regen_interval(self) -> int:
        return self.__regen_interval
    
    def go_next_tile(self):
        super().go_next_tile()
        self.__tiles_moved += self._idx < len(self._path.cells)
        if self.__tiles_moved % self.regen_interval == 0:
            self._lives += 1
