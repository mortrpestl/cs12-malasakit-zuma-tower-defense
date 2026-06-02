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
        self._y, self._x = path.start.y, path.start.x # start at beginning of path
        self._idx = 0
        
        self._pyxel_set = \
            (0, 8, 0, 48, 48, BGColor.PEACH) if color is Color.RED else \
            (0, 8, 48, 48, 48, BGColor.PEACH) if color is Color.BLUE else \
            (0, 8, 96, 48, 48, BGColor.PEACH) if color is Color.PURPLE else \
            (0, 8, 144, 48, 48, BGColor.PEACH) if color is Color.ORANGE else \
            (0, 8, 192, 48, 48, BGColor.PEACH) if color is Color.GREEN else \
            (0, 72, 0, 48, 48, BGColor.PEACH)
        self._pyxel_scale = 0.833 # hardcoded: change later
    
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
    
    @property
    def is_alive(self) -> bool:
        return self._lives > 0 and self._idx < len(self._path.cells) - 1

    @property
    def pyxel_set(self):
        return self._pyxel_set
    
    @property
    def pyxel_scale(self) -> float:
        return self._pyxel_scale
    
    def take_hit(self, color: Color) -> bool:
        res = self.color == color
        self._lives -= res
        return res
    
    def go_next_tile(self):
        if not self.is_alive:
            return
        self._idx += 1
        if self._idx >= len(self._path.cells):
            return
        next_cell = self._path.cells[self._idx]
        self._y, self._x = next_cell.y, next_cell.x
