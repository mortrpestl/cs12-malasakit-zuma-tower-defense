# pyright: strict

from model.model import Model
from model.entities.enemy import Enemy
from model.entities.chameleon import Chameleon
from model.entities.regenerator import Regenerator
from model.entities.normaltower import NormalTower
from model.entities.tower import Tower
from model.utils import BGColor, Color
from math import atan2, pi
from dataclasses import dataclass
import pyxel

@dataclass
class SpriteSet:
    img: int
    x: int
    y: int
    w: int
    h: int
    bg: BGColor
    scale: float

SPRITES: dict[tuple[type, Color], SpriteSet] = {
    (Enemy, Color.RED): SpriteSet(0, 8, 0, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.BLUE): SpriteSet(0, 8, 48, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.PURPLE): SpriteSet(0, 8, 96, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.ORANGE): SpriteSet(0, 8, 144, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.GREEN): SpriteSet(0, 8, 192, 48, 48, BGColor.PEACH, 0.833),
    (Enemy, Color.STEEL_BLUE): SpriteSet(0, 72, 0, 48, 48, BGColor.PEACH, 0.833),
    (Chameleon, Color.RED): SpriteSet(2, 8, 8, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.BLUE): SpriteSet(2, 8, 56, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.PURPLE): SpriteSet(2, 8, 104, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.ORANGE): SpriteSet(2, 8, 152, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.GREEN): SpriteSet(2, 8, 200, 48, 32, BGColor.PEACH, 0.833),
    (Chameleon, Color.STEEL_BLUE): SpriteSet(2, 72, 8, 48, 32, BGColor.PEACH, 0.833),
    (Regenerator, Color.RED): SpriteSet(1, 16, 0, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.BLUE): SpriteSet(1, 16, 48, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.PURPLE): SpriteSet(1, 16, 96, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.ORANGE): SpriteSet(1, 16, 144, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.GREEN): SpriteSet(1, 16, 192, 32, 48, BGColor.PEACH, 0.833),
    (Regenerator, Color.STEEL_BLUE): SpriteSet(1, 80, 0, 32, 48, BGColor.PEACH, 0.833),
}

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
        
        pyxel.load("view/pyxres_files/zuma_basic_enemies.pyxres", exclude_sounds=True, exclude_musics=True)
        sprite = SPRITES[(type(enemy), enemy.color)]
        pyxel.blt(x, y + 30, sprite.img, sprite.x, sprite.y, sprite.w, sprite.h, sprite.bg, scale=sprite.scale)
        
        # pyxel.rect(x, y + 30, model.config.width / model.config.cols, model.config.height / model.config.rows, enemy.color.value) # replace with sprites
    
    def draw_tower(self, model: Model, tower: Tower):
        y, x = model.get_position(tower.y, tower.x)
        
        pyxel.load("view/pyxres_files/zuma_basic_towers.pyxres", exclude_sounds=True, exclude_musics=True)
        
        if isinstance(tower, NormalTower):
            dy, dx = tower.halfway[1], tower.halfway[0]
            pyxel.blt(x - dx, y + 30 - dy, *tower.pyxel_set, scale=tower.pyxel_scale)
        
        # pyxel.rect(x, y + 30, model.config.width / model.config.cols, model.config.height / model.config.rows, 10) # replace with sprites
    
    def draw_shooter(self, model: Model):
        y, x = model.get_position(model.player.shooter.y, model.player.shooter.x)
        theta = atan2(pyxel.mouse_y - y, pyxel.mouse_x - x) * 180 / pi - 90
        
        pyxel.load("view/pyxres_files/zuma_basic_towers.pyxres", exclude_sounds=True, exclude_musics=True)
        
        pyxel.blt(x - 0.5 * model.config.width / model.config.cols, y - 0.5 * model.config.height / model.config.rows, 0, 0, 0, 64, 64, 8, rotate=theta, scale=0.625)
