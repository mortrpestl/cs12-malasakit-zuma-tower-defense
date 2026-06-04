# pyright: strict

from model.model import Model
from view.View import Sound
HIT_RADIUS = 40

def in_bounds(y: float, x: float, height: float, width: float) -> bool:
    return 0 <= y <= height and 0 <= x <= width

def within_radius(by: float, bx: float, ey: float, ex: float, radius: float) -> bool:
    return (bx - ex)**2 + (by - ey)**2 <= radius**2

class CollisionController:
    def __init__(self, m: Model, s: Sound):
        self.__model = m
        self.__sound = s
    
    def update(self):
        self.move_bullets()
        self.check_hits()
        self.remove_out_of_bounds()
    
    def move_bullets(self):
        for bullet in self.__model.bullets:
            bullet.update_position()

    def check_hits(self):
        current_round = self.__model.rounds[self.__model.current_round]
        for bullet in self.__model.bullets[:]:
            for enemy in current_round.current_enemies[:]:
                enemy_y, enemy_x = self.__model.get_position(enemy.y, enemy.x)
                cell = self.__model.stage.grid.grid[enemy.y][enemy.x]
                if within_radius(bullet.y_abs, bullet.x_abs, enemy_y, enemy_x, HIT_RADIUS) and not cell.is_tunnel:
                    enemy.take_hit(bullet.color)
                    self.__model.bullets.remove(bullet)
                    if enemy.lives <= 0:
                        current_round.current_enemies.remove(enemy)
                        self.__model.add_exp(enemy.exp)
                        self.__sound.kill_sound()
                    else:
                        self.__sound.hit_sound()


    def remove_out_of_bounds(self):
        self.__model.bullets = [
            b for b in self.__model.bullets
            if in_bounds(b.y_abs, b.x_abs, self.__model.config.height, self.__model.config.width)
        ]