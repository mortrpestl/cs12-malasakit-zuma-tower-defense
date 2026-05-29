# pyright: strict

from entity import Entity
from math import sin, cos

class Bullet(Entity):
    def __init__(self, x: float, y: float, angle: float):
        self._x_abs = x
        self._y_abs = y
        self._velocity = 3 # 3 px/s
        self._alive = True
        self._angle = angle # radians

    @property
    def alive(self) -> bool:
        return self._alive

    def kill(self):
        self._alive = False

    def update_position(self):
        if not self.alive:
            return
        dy = self._velocity * sin(self._angle)
        dx = self._velocity * cos(self._angle)
        self._x_abs += dx
        self._y_abs += dy