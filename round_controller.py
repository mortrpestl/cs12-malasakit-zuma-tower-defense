# pyright: strict

from model.model import Model
from model.entities.normaltower import NormalTower
from model.utils import Direction

import pyxel

class RoundController:
    def __init__(self, model: Model, bp: float):
        self.__model = model
        self.__tick = 0
        self.__spawn_index = 0
        self.__bullet_speed: float = bp

    @property
    def spawn_timer(self) -> int:
        return 480

    @property
    def move_timer(self) -> int:
        return 240

    @property
    def tick(self) -> int:
        return self.__tick

    def update(self):
        self.__tick += 1
        if self.__tick % self.spawn_timer == 0:
            self.spawn_enemy()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.__model.bullets.append(self.__model.player.shoot(pyxel.mouse_x, pyxel.mouse_y, self.__bullet_speed))

        if pyxel.btnr(pyxel.KEY_W):
            for tower in self.__model.bought_towers:
                if isinstance(tower, NormalTower):
                    tower.direction = Direction.UP
        if pyxel.btnr(pyxel.KEY_A):
            for tower in self.__model.bought_towers:
                if isinstance(tower, NormalTower):
                    tower.direction = Direction.LEFT
        if pyxel.btnr(pyxel.KEY_S):
            for tower in self.__model.bought_towers:
                if isinstance(tower, NormalTower):
                    tower.direction = Direction.DOWN
        if pyxel.btnr(pyxel.KEY_D):
            for tower in self.__model.bought_towers:
                if isinstance(tower, NormalTower):
                    tower.direction = Direction.RIGHT
        
        for tower in self.__model.bought_towers:
            if self.__tick % tower.shoot_interval == 0:
                self.__model.bullets.extend(tower.shoot(self.__bullet_speed))


        current_round = self.__model.rounds[self.__model.current_round]
        for enemy in current_round.current_enemies[:]:
            if self.__tick % self.move_timer == 0:
                old_y, old_x = enemy.y, enemy.x
                enemy.go_next_tile()
                self.__model.stage.grid.grid[old_y][old_x].entity = None
                self.__model.stage.grid.grid[enemy.y][enemy.x].entity = enemy
            last_cell = enemy.path.cells[-1]
            if enemy.y == last_cell.y and enemy.x == last_cell.x:
                self.__model.stage.grid.grid[enemy.y][enemy.x].entity = None
                current_round.current_enemies.remove(enemy)
                self.__model.player.lose_life()

        if self.is_round_over:
            self.__model.advance_next_round()
            self.__spawn_index = 0

    def spawn_enemy(self):
        current = self.__model.rounds[self.__model.current_round]
        if self.__spawn_index < len(current.enemies):
            enemy = current.enemies[self.__spawn_index]
            enemy.activate()
            current.current_enemies.append(enemy)
            self.__model.stage.grid.grid[enemy.y][enemy.x].entity = enemy
            self.__spawn_index += 1

    @property
    def is_round_over(self) -> bool:
        current = self.__model.rounds[self.__model.current_round]
        return (self.__spawn_index >= len(current.enemies) and len(current.current_enemies) == 0)