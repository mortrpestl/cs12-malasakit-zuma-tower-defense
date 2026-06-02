# pyright: strict

from model.entities.bullet import Bullet
from model.entities.tower import Tower
from model.game_config import GameConfig
from model.utils import BGColor, Direction, get_next_color
from math import atan2

class NormalTower(Tower):
    def __init__(self, config: GameConfig):
        super().__init__()
        self.__config = config
        self._width = self.__config.width / self.__config.cols
        self._height = self.__config.height / self.__config.rows
        self.__direction = Direction.RIGHT
        
    @property
    def pyxel_set(self):
        return (1, 0, 0, 64, 64, BGColor.RED) if self._level == 1 else \
            (2, 0, 0, 64, 64, BGColor.RED)
    
    @property
    def pyxel_scale(self) -> float:
        return 0.625 # hardcoded: change later
    
    @property
    def halfway(self) -> tuple[int, int]:
        return (12, 12) # hardcoded: change later
    
    @property
    def direction(self) -> Direction:
        return self.__direction
    
    @direction.setter
    def direction(self, d: Direction):
        self.__direction = d
    
    @property
    def shoot_interval(self) -> int:
        return 120

    def shoot(self) -> list[Bullet]:
        dx, dy = self.__direction.value
        angle = atan2(-dy, dx)
        x_abs, y_abs = (self.x + 0.5) * self._width, (self.y + 0.5) * self._height + 30
        delimiter = self._level == 2
        if self.__direction in (Direction.UP, Direction.DOWN):
            return [Bullet(x_abs - self._width / 4 * delimiter + self._width / 2 * i, y_abs, angle, get_next_color()) for i in range(self.level)]
        else:
            return [Bullet(x_abs, y_abs - self._height / 4 * delimiter + self._height / 2 * i, angle, get_next_color()) for i in range(self.level)]