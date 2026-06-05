# pyright: strict
from model.entities.entity import Entity
from model.game_config import GameConfig
from math import atan2
from model.entities.bullet import Bullet
from model.utils import get_next_color

# restrict v to [lo, hi]
def clamp(v: int, lo: int, hi: int):
    return max(lo, min(v, hi))

class Shooter(Entity):
    def __init__(self, config: GameConfig):
        # position in center
        super().__init__()
        self.__config = config
        self._y = config.rows >> 1
        self._x = config.cols >> 1
        self._y_abs = 0
        self._x_abs = 0
        self.update_position()
    
    @property
    def y_abs(self) -> float:
        return self._y_abs
    
    @property
    def x_abs(self) -> float:
        return self._x_abs

    def update_position(self):
        cell_width = self.__config.width / self.__config.cols
        cell_height = self.__config.height / self.__config.rows
        self._y_abs = (self._y + 0.5) * cell_height + 40
        self._x_abs = (self._x + 0.5) * cell_width

    def move_left(self):
        self._x = clamp(self._x - 1, 0, self.__config.cols)
    
    def move_right(self):
        self._x = clamp(self._x + 1, 0, self.__config.cols)

    def move_up(self):
        self._y = clamp(self._y - 1, 0, self.__config.rows)

    def move_down(self):
        self._y = clamp(self._y + 1, 0, self.__config.rows)

    def shoot(self, x: float, y: float, v: float) -> Bullet:
        angle = atan2(y - self._y_abs, x - self._x_abs)
        return Bullet(self._x_abs, self._y_abs, angle, get_next_color(), v)