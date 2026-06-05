# pyright: strict

from abc import ABC

class Entity(ABC):
    def __init__(self):
        self._y = -1 # out of render maybe?
        self._x = -1
    
    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, new_x: int):
        self._x = new_x
    
    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, new_y: int):
        self._y = new_y