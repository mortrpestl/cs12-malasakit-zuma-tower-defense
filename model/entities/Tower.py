# pyright: strict

from abc import abstractmethod
from utils import *
from bullet import Bullet
from entity import Entity

# for making more tower classes
class Tower(Entity):
    def __init__(self, direction: Direction, level: int, cost: int):
        self._direction = direction
        self._level = level
        self._cost = cost
    
    @property
    def direction(self) -> Direction:
        return self._direction
    
    @property
    def level(self) -> int:
        return self._level
    
    @property
    def cost(self) -> int:
        return self._cost
    
    @abstractmethod
    def shoot(self, bullets: list[Bullet]):
        ...