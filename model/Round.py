# pyright: strict

from game_config import GameConfig

class Round:
    def __init__(self, config: GameConfig):
        self.__config = config
        # TODO finish generating enemies