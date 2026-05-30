# pyright: strict
from renderer import Renderer
from model.model import Model

class MenuRenderer(Renderer):
    def draw(self, model: Model):
        ...
        # renders the game