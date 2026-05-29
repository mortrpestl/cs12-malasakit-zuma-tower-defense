# pyright: strict

from utils import *
from model.entities.enemy import Enemy
from model.entities.chameleon import Chameleon
from model.entities.regenerator import Regenerator

def make_enemy(enemy_type: EnemyType, color: Color, path: Path) -> Enemy:
    # add new enemies here
    enemy_dict = {
        EnemyType.NORMAL: Enemy(color, path),
        EnemyType.CHAMELEON: Chameleon(color, path),
        EnemyType.REGENERATOR: Regenerator(color, path)
    }
    return enemy_dict[enemy_type]

class Round:
    def __init__(self, config: WaveConfig):
        self.__config = config
        self.__enemies = [
            make_enemy(enemy_type, color, path) for enemy_type, color, path in zip(config.special_types, config.colors, config.paths)
        ]

    @property 
    def enemies(self) -> list[Enemy]:
        return self.__enemies