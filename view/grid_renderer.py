# pyright: strict

import pyxel 

from model.Model import Model 
from model.cell import Cell
from model.entities.bullet import Bullet
from model.entities.tower import Tower
from model.entities.shooter import Shooter
from model.player import Player
from model.path import Path
from model.cell import Cell


from renderer import Renderer

"""
Grid size: 860px x 600px (20 x 15 tiles)
Adjustment from top: 30px
Each block side length: 40px x 40px
 
Centering adjustment from top and left: 
+20px 
+20px
"""

class GridRenderer(Renderer):
        
    def normalize_coord(self, r : int, c : int):
        adj : int = 30 
        half_side : int = 20
        
        return (40*r + half_side + adj, 40*c + half_side)
        
    def draw_bullets(self, bullets : list[Bullet]):
        
        for bullet in bullets:
            x,y = bullet.pos
            pyxel.blt(x,y, ...)

    def draw_towers(self, towers : list[Tower]):
        
        for tower in towers:
            x,y = tower.pos
            pyxel.blt(x,y, ...)

    def draw_shooters(self, shooter : Shooter):
        pyxel.blt(x,y, ...)

    def draw_players(self, player : Player):
        pyxel.blt(x,y, ...)

    def draw_paths(self, paths : list[Path]):
        for path in paths:
            self.draw_cells(path)

    def draw_cells(self, cell: Path):
        # ! edit this perhaps
        for cell in cells:
            x,y = cell.pos 
            
            pyxel.blt(cell.x, cell.y, ...)
            

    def draw(self, model: Model):
        draw_bullets(model.bullets)
        draw_towers(model.towers)
        draw_shooters(model.shooters)
        draw_players(model.players)
        draw_paths(model.paths)
        draw_cells(model.cells)
        
        ...
        # renders the game