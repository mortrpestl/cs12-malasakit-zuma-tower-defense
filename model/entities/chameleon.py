# pyright: strict

from model.entities.enemy import Enemy
from model.path import Path
from model.utils import *

class Chameleon(Enemy):                          
    def __init__(self, color: Color, path: Path):
        super().__init__(color, path)
    # TODO implement chameleon specific logic