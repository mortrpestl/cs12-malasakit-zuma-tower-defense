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

    def update(self) -> None:
        pass

    def draw(self) -> None:
        for row in self._model.stage.grid.grid:
            for cell in row:
                self.draw_cell(cell)