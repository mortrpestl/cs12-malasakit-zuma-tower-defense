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
        print(f"enemy list of tiles: {[(cell.y, cell.x) for cell in self._path.cells]}")
    
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
