from model.model import Model
from model.utils import *
from model.game_config import GameConfig

from view.View import View

from Controller import Controller

config = GameConfig()
config.fetch_config("settings.json")
g = Model(config, GameMode.CAMPAIGN)
v = View(600, 820, 240)
c = Controller(g, v)

if __name__ == "__main__":
    c.start_game()