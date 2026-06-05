from model.model import Model
from model.utils import GameMode
from model.game_config import GameConfig

from view.View import View

from Controller import Controller

config = GameConfig()
config.fetch_config("settings.json")

g = Model(config=config, mode=GameMode.CAMPAIGN, campaign_file="campaign_round_1.json")

v = View(600, 840, 30)
c = Controller(g, v)

if __name__ == "__main__":
    c.start_game()