# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Regenerator(Enemy):
    def __init__(self, color: Color, path: Path):
        super().__init__(color, path)
        
        self._pyxel_set = \
            (0, 80, 49, 32, 48, BGColor.PEACH) if color is Color.RED else \
            (0, 80, 97, 32, 48, BGColor.PEACH) if color is Color.BLUE else \
            (0, 80, 145, 32, 48, BGColor.PEACH) if color is Color.PURPLE else \
            (0, 80, 193, 32, 48, BGColor.PEACH) if color is Color.ORANGE else \
            (0, 144, 1, 32, 48, BGColor.PEACH) if color is Color.GREEN else \
            (0, 144, 49, 32, 48, BGColor.PEACH)
            
    # TODO implement regenerator specific logic