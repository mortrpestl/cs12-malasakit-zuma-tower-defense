# pyright: strict

from abc import ABC
from utils import *

class Entity(ABC):
    def __init__(self, pos: tuple[int, int], color: Color):
        self._pos = pos
        self._color = color
    
    @property    
    def pos(self):
        return self._pos