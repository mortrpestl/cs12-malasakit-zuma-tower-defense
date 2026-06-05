# pyright: strict

from model.model import Model
from model.entities.enemy import Enemy
from model.entities.tower import Tower
from view.sprites import enemy_sprites, tower_sprites
from model.utils import BGColor, SpriteSet
from math import atan2, pi

import pyxel

class EntityRenderer:
    def draw(self, model: Model):
        for bullet in model.bullets:
            pyxel.circ(bullet.x_abs, bullet.y_abs, 5, bullet.color.value) # circle for now
        current_round = model.rounds[model.current_round]
        for enemy in current_round.enemies:
            if enemy.is_alive:
                self.draw_enemy(model, enemy)
        for tower in model.bought_towers:
            self.draw_tower(model, tower)
        self.draw_shooter(model)

    def draw_enemy(self, model: Model, enemy: Enemy):
        if not enemy.is_active:
            return
        y, x = model.get_position(enemy.y, enemy.x)
        
        
        try:
            sprite : SpriteSet = enemy_sprites[(type(enemy), enemy.color)]
            dz = max(0, 0.5 * (sprite.w - sprite.scale * sprite.w), 0.5 * (sprite.h - sprite.scale * sprite.h))
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, model.config.width / model.config.cols, model.config.height / model.config.rows, enemy.color.value)
    
    def draw_tower(self, model: Model, tower: Tower):
        y, x = model.get_position(tower.y, tower.x)
        
        try:
            sprite : SpriteSet = tower_sprites[(type(tower), tower.level)]
            dz = 0.5 * (sprite.w - model.config.width / model.config.cols)
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, model.config.width / model.config.cols, model.config.height / model.config.rows, BGColor.YELLOW)
            
    
    def draw_shooter(self, model: Model):
        y, x = model.get_position(model.player.shooter.y, model.player.shooter.x)
        theta = atan2(pyxel.mouse_y - y, pyxel.mouse_x - x) * 180 / pi - 90
        
        try:
            sprite : SpriteSet = tower_sprites[(type(model.player.shooter), None)]
            dz = 0.5 * (sprite.w - model.config.width / model.config.cols)
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, rotate=theta, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, model.config.width / model.config.cols, model.config.height / model.config.rows, BGColor.STEEL_BLUE)
