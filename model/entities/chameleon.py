# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *
from random import Random

class Chameleon(Enemy):                                         
    def __init__(self, color: Color, path: Path, color_change_freq: int = 120):
        super().__init__(color, path)
        
        self._pyxel_set = \
            (2, 8, 8, 48, 32, BGColor.PEACH) if color is Color.RED else \
            (2, 8, 56, 48, 32, BGColor.PEACH) if color is Color.BLUE else \
            (2, 8, 104, 48, 32, BGColor.PEACH) if color is Color.PURPLE else \
            (2, 8, 152, 48, 32, BGColor.PEACH) if color is Color.ORANGE else \
            (2, 8, 200, 48, 32, BGColor.PEACH) if color is Color.GREEN else \
            (2, 72, 8, 48, 32, BGColor.PEACH)
        self._pyxel_scale = 0.833
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
            self._color = self.__rng.choice(list(Color))