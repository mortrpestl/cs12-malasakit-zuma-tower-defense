# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.grid import Grid
from model.cell import Cell
from model.entities.entity import Entity
from model.entities.enemy import Enemy
from model.entities.tower import Tower
from model.entities.shooter import Shooter

from math import atan2, cos, pi, sin
from model.utils import (
    get_next_color
)

TUNNEL_COLOR = 2
PATH_COLOR = 4

class GridRenderer(Renderer):
    def __init__(self, m: Model):
        self.__model = m
        self.__cell_width = m.config.width / m.config.cols
        self.__cell_height = m.config.height / m.config.rows
    
    def draw(self):
        for path in self.__model.stage.paths:
            for cell in path.cells:
                color = TUNNEL_COLOR if cell.is_tunnel else PATH_COLOR
                pyxel.rect(cell.x * self.__cell_width, cell.y * self.__cell_height, self.__cell_width, self.__cell_height, color)
    
    def update(self):
        pass