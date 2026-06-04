# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Chameleon(Enemy):                                         
    def __init__(self, color: Color, path: Path):
        super().__init__(color, path)
        
        self._pyxel_set = \
            (0, 136, 105, 48, 32, BGColor.PEACH) if color is Color.RED else \
            (0, 136, 153, 48, 32, BGColor.PEACH) if color is Color.BLUE else \
            (0, 136, 201, 48, 32, BGColor.PEACH) if color is Color.PURPLE else \
            (0, 200, 9, 48, 32, BGColor.PEACH) if color is Color.ORANGE else \
            (0, 200, 57, 48, 32, BGColor.PEACH) if color is Color.GREEN else \
            (0, 200, 105, 48, 32, BGColor.PEACH)
    
    # TODO implement chameleon specific logic