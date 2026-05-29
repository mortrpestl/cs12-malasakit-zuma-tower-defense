# pyright: strict

from abc import ABC
from utils import *

class Entity(ABC):
    def __init__(self):
        self._y = -1 # out of render maybe?
        self._x = -1
    
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y