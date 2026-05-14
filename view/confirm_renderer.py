# pyright: strict
from renderer import Renderer
from model.model import Model

class ConfirmRenderer(Renderer):
    def __init__(self):
        self.HEIGHT = 860
        self.WIDTH = 600
        
        
    def draw(self, model: Model):
        ...
        # renders the game