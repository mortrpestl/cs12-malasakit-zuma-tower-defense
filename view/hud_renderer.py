# pyright: strict
from renderer import Renderer
from model.Model import Model

class HUDRenderer(Renderer):
    def draw(self, model: Model):
        ...
        # renders the game