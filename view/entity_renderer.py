# pyright: strict

from model.model import Model
from model.entities.enemy import Enemy
from model.entities.normaltower import NormalTower
from model.entities.tower import Tower
from math import atan2, pi
import pyxel

class EntityRenderer:
    def draw(self, model: Model):
        for bullet in model.bullets:
            pyxel.circ(bullet.x_abs, bullet.y_abs, 2, bullet.color.value) # circle for now
        current_round = model.rounds[model.current_round]
        for enemy in current_round.enemies:
            if enemy.is_alive:
                self.draw_enemy(model, enemy)
        for tower in model.bought_towers:
            self.draw_tower(model, tower)
        self.draw_shooter(model)

    def draw_enemy(self, model: Model, enemy: Enemy):
        y, x = model.get_position(enemy.y, enemy.x)
        dz = 0.5 * (48 - model.config.width / model.config.cols)
        
        pyxel.blt(x - dz, y + 40 - dz, *enemy.pyxel_set, scale=enemy.pyxel_scale)
    
    def draw_tower(self, model: Model, tower: Tower):
        y, x = model.get_position(tower.y, tower.x)
        
        if isinstance(tower, NormalTower):
            dy, dx = tower.midpoint, tower.midpoint
            pyxel.blt(x - dx, y + 40 - dy, *tower.pyxel_set, scale=tower.pyxel_scale)
    
    def draw_shooter(self, model: Model):
        y, x = model.get_position(model.player.shooter.y, model.player.shooter.x)
        theta = atan2(pyxel.mouse_y - y, pyxel.mouse_x - x) * 180 / pi - 90
        
        pyxel.blt(x - 12, y + 28, 1, 0, 0, 64, 64, 8, rotate=theta, scale=0.625)
