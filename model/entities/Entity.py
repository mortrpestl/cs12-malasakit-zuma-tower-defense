# pyright: strict

from abc import ABC
from Utils import *

class Entity(ABC):
    def __init__(self, pos: tuple[int, int], color: Color):
        self._pos = pos
        self._color = color