# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Regenerator(Enemy):
    def __init__(self, color: Color, path: Path):
        super().__init__(color, path)
        
        self._pyxel_set = \
            (1, 16, 0, 32, 48, BGColor.PEACH) if color is Color.RED else \
            (1, 16, 48, 32, 48, BGColor.PEACH) if color is Color.BLUE else \
            (1, 16, 96, 32, 48, BGColor.PEACH) if color is Color.PURPLE else \
            (1, 16, 144, 32, 48, BGColor.PEACH) if color is Color.ORANGE else \
            (1, 16, 192, 32, 48, BGColor.PEACH) if color is Color.GREEN else \
            (1, 80, 0, 32, 48, BGColor.PEACH)
        self._pyxel_scale = 0.833
    # TODO implement regenerator specific logic