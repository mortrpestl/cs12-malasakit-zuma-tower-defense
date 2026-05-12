# pyright: strict
from Renderer import Renderer
from model.Model import Model

class MenuRenderer(Renderer):
    def draw(self, model: Model):
        ...
        # renders the game