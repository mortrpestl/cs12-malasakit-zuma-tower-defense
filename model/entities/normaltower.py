# pyright: strict

from model.entities.tower import Tower
from model.utils import Direction, get_next_color
from model.entities.bullet import Bullet
from math import atan2

class NormalTower(Tower):
    def __init__(self):
        super().__init__()
        self.__direction = Direction.RIGHT
    
    @property
    def direction(self) -> Direction:
        return self._direction
    
    @direction.setter
    def direction(self, d: Direction):
        self._direction = d
    
    def shoot(self) -> list[Bullet]:
        dy, dx = self.__direction.value
        angle = atan2(dy, dx)
        return [Bullet(self.x, self.y, angle, get_next_color()) for _ in range(self.level)]