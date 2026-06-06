# pyright: strict

from view.renderer import Renderer
from model.model import Model
from model.entities.enemy import Enemy
from model.entities.tower import Tower
from model.utils import BGColor, SpriteSet

from view.screen_manager import ScreenManager
from view.sprites import enemy_sprites, tower_sprites


from math import atan2, pi

import pyxel

class EntityRenderer(Renderer):
    def __init__(self, m: Model, sm: ScreenManager):
        super().__init__(m, sm)
    
    def draw(self):
        for bullet in self.model.bullets:
            pyxel.circ(bullet.x_abs, bullet.y_abs, 5, bullet.color.value) # circle for now
        current_round = self.model.rounds[self.model.current_round]
        for enemy in current_round.enemies:
            if enemy.is_alive:
                self.draw_enemy(enemy)
        for tower in self.model.bought_towers:
            self.draw_tower(tower)
        self.draw_shooter()
        
    def update(self):
        pass

    def draw_enemy(self, enemy: Enemy):
        if not enemy.is_active:
            return
        y, x = self.model.get_position(enemy.y, enemy.x)
        
        
        try:
            sprite : SpriteSet = enemy_sprites[(type(enemy), enemy.color)]
            dz = max(0, 0.5 * (sprite.w - sprite.scale * sprite.w), 0.5 * (sprite.h - sprite.scale * sprite.h))
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, self.model.config.width / self.model.config.cols, self.model.config.height / self.model.config.rows, enemy.color.value)
    
    def draw_tower(self, tower: Tower):
        y, x = self.model.get_position(tower.y, tower.x)
        
        try:
            sprite : SpriteSet = tower_sprites[(type(tower), tower.level)]
            dz = 0.5 * (sprite.w - self.model.config.width / self.model.config.cols)
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, self.model.config.width / self.model.config.cols, self.model.config.height / self.model.config.rows, BGColor.YELLOW)
            
    
    def draw_shooter(self):
        y, x = self.model.get_position(self.model.player.shooter.y, self.model.player.shooter.x)
        theta = atan2(pyxel.mouse_y - y, pyxel.mouse_x - x) * 180 / pi - 90
        
        try:
            sprite : SpriteSet = tower_sprites[(type(self.model.player.shooter), None)]
            dz = 0.5 * (sprite.w - self.model.config.width / self.model.config.cols)
            pyxel.blt(x - dz, y + 40 - dz, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, rotate=theta, scale=sprite.scale)
        except KeyError:
            pyxel.rect(x, y + 40, self.model.config.width / self.model.config.cols, self.model.config.height / self.model.config.rows, BGColor.STEEL_BLUE)
