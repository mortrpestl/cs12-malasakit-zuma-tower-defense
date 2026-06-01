# pyright: strict

from model.model import Model
from model.entities.enemy import Enemy
from model.entities.tower import Tower
from math import atan2
import pyxel

class EntityRenderer:
    def draw(self, model: Model):
        for bullet in model.bullets:
            pyxel.circ(bullet.x_abs, bullet.y_abs, 2, bullet.color.value) # circle for now
        current_round = model.rounds[model.current_round]
        for enemy in current_round.enemies:
            if enemy.is_alive:
                self.draw_enemy(model, enemy)
        for tower in model.towers:
            self.draw_tower(model, tower)
        self.draw_shooter(model)

    def draw_enemy(self, model: Model, enemy: Enemy):
        y, x = model.get_position(enemy.y, enemy.x)
        pyxel.rect(x, y, model.config.width / model.config.cols, model.config.height / model.config.rows, enemy.color.value) # replace with sprites
    
    def draw_tower(self, model: Model, tower: Tower):
        y, x = model.get_position(tower.y, tower.x)
        pyxel.rect(x, y, model.config.width / model.config.cols, model.config.height / model.config.rows, 10) # replace with sprites
    
    def draw_shooter(self, model: Model):
        y, x = model.get_position(model.player.shooter.y, model.player.shooter.x)
        theta = atan2(pyxel.mouse_y - y, pyxel.mouse_x - x)
        pyxel.blt(x - 0.5 * model.config.width / model.config.cols, y - 0.5 * model.config.height / model.config.rows, 0, 0, 0, 64, 64, 8, rotate=theta, scale=0.625)
