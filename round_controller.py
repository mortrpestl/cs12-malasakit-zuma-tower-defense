# pyright: strict

from model.model import Model

class RoundController:
    def __init__(self, model: Model):
        self.__model = model
        self.__tick = 0
    
    @property
    def spawn_timer(self) -> int:
        return 60 # every 60 ticks, 1 enemy spawns

    @property
    def tick(self) -> int:
        return self.__tick

    def update(self):
        self.__tick += 1
        if self.tick % self.spawn_timer == 0:
            self.spawn_enemy()
        current_round = self.__model.rounds[self.__model.current_round]
        for enemy in current_round.current_enemies:
            enemy.go_next_tile()
            last_cell = enemy.path.cells[-1]
            if enemy.y == last_cell.y and enemy.x == last_cell.x:
                current_round.current_enemies.remove(enemy)
        for tower in self.__model.towers:
            bullets = tower.shoot()
            self.__model.bullets.append(*bullets)
        if self.is_round_over:
            self.__model.advance_next_round()

    def spawn_enemy(self):
        current = self.__model.rounds[self.__model.current_round]
        if len(current.current_enemies) < self.__model.enemy_count:
            idx = len(current.current_enemies)
            current.current_enemies.append(current.enemies[idx])
    @property
    def is_round_over(self) -> bool:
        current = self.__model.rounds[self.__model.current_round]
        return len(current.current_enemies) >= self.__model.enemy_count and all(not enemy.is_alive for enemy in current.enemies)