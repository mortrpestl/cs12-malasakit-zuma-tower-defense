from model.model import Model
from model.utils import *
from model.game_config import GameConfig

from view.View import View

from Controller import Controller

config = GameConfig()
g = Model(config, GameMode.CAMPAIGN)
v = View(600, 820, 30)
c = Controller(g, v)

if __name__ == "__main__":
    c.start_game()