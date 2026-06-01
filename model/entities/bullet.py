# pyright: strict

from model.entities.entity import Entity
from model.utils import Color
from math import sin, cos

class Bullet(Entity):
    def __init__(self, x: float, y: float, angle: float, color: Color):
        super().__init__()
        self._x_abs = x
        self._y_abs = y
        self._velocity = 1 # 3 px/s
        self._alive = True
        self._angle = angle # radians
        self._color = color

    @property
    def alive(self) -> bool:
        return self._alive
    
    @property
    def color(self) -> Color:
        return self._color

    @property
    def x_abs(self) -> float:
        return self._x_abs
    
    @property
    def y_abs(self) -> float:
        return self._y_abs

    def kill(self):
        self._alive = False

    def update_position(self):
        if not self.alive:
            return
        dy = self._velocity * sin(self._angle)
        dx = self._velocity * cos(self._angle)
        self._x_abs += dx
        self._y_abs += dy