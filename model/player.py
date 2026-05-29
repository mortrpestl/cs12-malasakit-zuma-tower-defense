# pyright: strict
from model.game_config import GameConfig
from model.entities.shooter import Shooter
from model.entities.bullet import Bullet

class Player:
    def __init__(self, config: GameConfig):
        self.__lives = config.lives
        self.__score = 0
        self.__shooter = Shooter(config)

    @property
    def lives(self) -> int:
        return self.__lives
    
    @property
    def score(self) -> int:
        return self.__score
    
    # x and y coordinates of cursor
    def shoot(self, x: float, y: float) -> Bullet:
        return self.__shooter.shoot(x, y)
