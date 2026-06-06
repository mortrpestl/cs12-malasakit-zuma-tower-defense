# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import Color
from random import Random

class Chameleon(Enemy):                                         
    def __init__(self, color: Color, path: Path, color_change_freq: int = 2, hp_multiplier: int = 1):
        super().__init__(color, path, hp_multiplier)
        self.__tiles_moved = 0
        self.__color_change_freq = color_change_freq
        self.__rng = Random(12) # set seed

    @property
    def color_change_freq(self) -> int:
        return self.__color_change_freq

    def go_next_tile(self):
        super().go_next_tile()
        self.__tiles_moved += self._idx < len(self._path.cells)
        if self.__tiles_moved % self.color_change_freq == 0:
            self._color = self.__rng.choice([x for x in list(Color) if x != self.color])
