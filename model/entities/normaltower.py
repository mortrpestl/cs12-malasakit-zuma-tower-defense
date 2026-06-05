# pyright: strict

from model.entities.bullet import Bullet
from model.entities.tower import Tower
from model.game_config import GameConfig
from model.utils import Direction, get_next_color
from math import atan2
import time

class NormalTower(Tower):
    def __init__(self, config: GameConfig):
        super().__init__(config)
        self.__direction = Direction.RIGHT
        self.__last_shot = float('-inf')
    
    @property
    def direction(self) -> Direction:
        return self.__direction
    
    @direction.setter
    def direction(self, d: Direction):
        self.__direction = d
    
    @property
    def shoot_interval(self) -> float:
        return self.config.min_tower_interval

    @property
    def can_shoot(self) -> bool:
        return time.time() - self.__last_shot >= self.shoot_interval

    def shoot(self, v: float, config: GameConfig) -> list[Bullet]:
        
        width : float = config.width / config.cols
        height : float = config.height / config.rows
        self.__last_shot = time.time()

        dx, dy = self.__direction.value
        angle = atan2(-dy, dx)
        x_abs, y_abs = (self.x + 0.5) * width, (self.y + 0.5) * height + 40
        delimiter = self._level == 2
        if self.__direction in (Direction.UP, Direction.DOWN):
            return [Bullet(x_abs - width / 4 * delimiter + width / 2 * i, y_abs, angle, get_next_color(), v) for i in range(self.level)]
        else:
            return [Bullet(x_abs, y_abs - height / 4 * delimiter + height / 2 * i, angle, get_next_color(), v) for i in range(self.level)]