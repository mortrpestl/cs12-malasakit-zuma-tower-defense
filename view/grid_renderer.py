# pyright: strict

import pyxel

from renderer import Renderer
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

"""
NEWNEWNEWNEW Grid size: 820px x 600px (19 x 15 tiles) 
OLD Grid size: 860px x 600px (20 x 15 tiles) 

Adjustment from top: 30px
Each block side length: 40px x 40px
 
Centering adjustment from top and left: 
+20px 
+20px
"""

# ! TODO JUSTIN: edit the params in the pyxel.blt below to properly show the towers

CELL_HEIGHT = 40
CELL_WIDTH = 40
TOP_BOTTOM_PADDING = 30


class GridRenderer(Renderer):

    def __init__(self, model: Model):
        super().__init__(model)
        
        # SUGGESTION FOR DIOGN: put this in grid_renderer.py # diogn's comment: is this right?
        self._zuma_rot : float = 0
        self._zuma_ball_col : int = get_next_color()

    def normalize_coord(self, r: int, c: int) -> tuple[int, int]:
        half_side = CELL_HEIGHT // 2
        return (40 * c + half_side, 40 * r + half_side + TOP_BOTTOM_PADDING)

    def draw_entity(self, entity: Entity, x: int, y: int) -> None:
        if isinstance(entity, Tower):
            pyxel.blt(x, y, ...)
        elif isinstance(entity, Shooter):
            pyxel.blt(x, y, ...)
        elif isinstance(entity, Enemy):
            pyxel.blt(x, y, ...)

    def draw_cell(self, cell: Cell) -> None:
        x, y = self.normalize_coord(cell.y, cell.x)
        if cell.is_tunnel:
            pyxel.rect(x, y, CELL_WIDTH, CELL_HEIGHT, ...)  # TODO: tunnel tile color
        if cell.entity is not None:
            self.draw_entity(cell.entity, x, y)


    # map (Justin's additions)
    
    def draw_game_map(self) -> None:
        for i in range(15):
            for j in range(19):
                pyxel.rect(40 * i, 30 + 40 * j, 40, 40, 7 * (i % 2) + 7 * (j % 2))
        
    def draw_zuma_tower(self) -> None:
        theta : float = self._zuma_rot
        
        pyxel.blt(268, 378, 0, 0, 0, 64, 64, 8, rotate=theta, scale=0.625)
        
    def draw_ball_to_shoot(self) -> None:
        theta2 : float = (self._zuma_rot + 90) * (pi / 180)
        color : int = self._zuma_ball_col
        
        pyxel.circ(300 + 25 * cos(theta2), 410 + 25 * sin(theta2), 5, color)
        
    def convert_mouse_pos_rotation(self):
        x : int = pyxel.mouse_x
        y : int = pyxel.mouse_y
        
        self._zuma_rot = atan2(y - 390, x - 280) * (180 / pi) - 90 if 30 < y < 800 else self._zuma_rot
        
    def convert_mouse_click_color(self):
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self._zuma_ball_col = get_next_color()
            
    # update + draw
    def update(self) -> None:
        pass

    def draw(self) -> None:
        for row in self._model.stage.grid.grid:
            for cell in row:
                self.draw_cell(cell)
                
    