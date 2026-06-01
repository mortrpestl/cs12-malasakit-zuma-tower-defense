# pyright: strict

from abc import abstractmethod
from model.entities.bullet import Bullet
from model.entities.entity import Entity
from random import Random

# for making more tower classes
class Tower(Entity):
    def __init__(self):
        super().__init__()
        self._level = 1 # 1 if unupgraded; make an enum?
        self._cost = 5
        self._rng = Random(12)
    
    @property
    def level(self) -> int:
        return self._level

    @property
    def cost(self) -> int:
        return self._cost
    
    @property
    @abstractmethod
    def shoot_interval(self) -> int:
        ...

    def upgrade(self):
        self._level = 2

    @abstractmethod
    def shoot(self) -> list[Bullet]:
        ...