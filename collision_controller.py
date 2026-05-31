# pyright: strict

from model.model import Model

EPS = 10**-3

def equal(a: float, b: float) -> bool:
    return abs(a - b) < EPS    

def get_position(model: Model, i: int, j: int) -> tuple[float, float]:
    cell_width = model.config.width / model.config.cols
    cell_height = model.config.height / model.config.rows
    return (i + 0.5) * cell_height, (j + 0.5) * cell_width

def in_bounds(y: float, x: float, height: float, width: float):
    return 0 <= y <= height and 0 <= x <= width

class CollisionController:
    def __init__(self, m: Model):
        self.__model = m
    
    def update(self):
        ...
    
    def move_bullets(self):
        for bullet in self.__model.bullets:
            bullet.update_position()

    def check_hits(self):
        round = self.__model.rounds[self.__model.current_round]
        for bullet in self.__model.bullets:
            for enemy in round.enemies:
                enemy_y, enemy_x = get_position(self.__model, enemy.y, enemy.x)
                if equal(bullet.x, enemy_x) and equal(bullet.y, enemy_y):
                    enemy.take_hit(bullet.color)
                    self.__model.bullets.remove(bullet)
                    if enemy.lives <= 0:
                        round.enemies.remove(enemy)
                        self.__model.add_exp(enemy.exp)
                    break

    def remove_out_of_bounds(self):
        self.__model.bullets = [
            b for b in self.__model.bullets if in_bounds(b.y_abs, b.x_abs, self.__model.config.height, self.__model.config.width)
        ]