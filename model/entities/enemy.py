# pyright: strict

from model.entities.entity import Entity
from model.path import Path
from model.utils import *

class Enemy(Entity):
    def __init__(self, color: Color, path: Path):
        # default settings
        super().__init__()
        self._lives = 1
        self._exp = 10
        self._color = color
        self._path = path
        self.y, self.x = path.start.y, path.start.x # start at beginning of path
    
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
    def path(self) -> Path:
        return self._path
    
    def take_hit(self, color: Color) -> bool:
        res = self.color == color
        self._lives -= res
        return res