# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Chameleon(Enemy):                                         
    def __init__(self, color: Color, path: Path):
        super().__init__(color, path)
        
        self._pyxel_set = \
            (2, 8, 8, 48, 32, BGColor.PEACH) if color is Color.RED else \
            (2, 8, 56, 48, 32, BGColor.PEACH) if color is Color.BLUE else \
            (2, 8, 104, 48, 32, BGColor.PEACH) if color is Color.PURPLE else \
            (2, 8, 152, 48, 32, BGColor.PEACH) if color is Color.ORANGE else \
            (2, 8, 200, 48, 32, BGColor.PEACH) if color is Color.GREEN else \
            (2, 72, 8, 48, 32, BGColor.PEACH)
        self._pyxel_scale = 0.833
    # TODO implement chameleon specific logic