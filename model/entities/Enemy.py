# pyright: strict

from entity import Entity
from utils import *

class Enemy(Entity):
    def __init__(self, color: Color, path_index: int):
        # default settings
        super().__init__()
        self._lives = 1
        self._exp = 10
        self._color = color
        self._path_index = path_index
    
    @property
    def lives(self) -> int:
        return self._lives
    
    @property
    def exp(self) -> int:
        return self._exp

    @property
    def color(self) -> Color:
        return self._color
    
    @property
    def path_index(self) -> int:
        return self._path_index
    
    def take_hit(self, color: Color) -> bool:
        res = self.color == color
        self._lives -= res
        return res