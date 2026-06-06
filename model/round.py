# pyright: strict

from model.entities.enemy import Enemy
from model.entities.chameleon import Chameleon
from model.entities.regenerator import Regenerator
from model.path import Path
from model.game_config import GameConfig
from model.utils import *

def make_enemy(enemy_type: EnemyType, color: Color, path: Path, config: GameConfig) -> Enemy:
    # add new enemies here
    enemy_dict = {
        EnemyType.NORMAL: Enemy(color, path),
        EnemyType.CHAMELEON: Chameleon(color, path, config.chameleon_freq),
        EnemyType.REGENERATOR: Regenerator(color, path, config.regen_hp)
    }
    return enemy_dict[enemy_type]

class Round:
    def __init__(self, config: WaveConfig, paths: list[Path], game_config: GameConfig):
        self.__config = config
        self.__enemies = [
            make_enemy(enemy_type, color, path, game_config) for enemy_type, color, path in zip(config.special_types, config.colors, [paths[idx] for idx in config.paths])
        ][:game_config.enemies]
        self.__current_enemies: list[Enemy] = []

    @property
    def config(self) -> WaveConfig:
        return self.__config
    
    @property 
    def enemies(self) -> list[Enemy]:
        return self.__enemies
    
    @property
    def current_enemies(self) -> list[Enemy]:
        return self.__current_enemies