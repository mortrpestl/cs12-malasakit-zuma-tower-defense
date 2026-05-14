# pyright: strict

import pyxel 

from renderer import Renderer
from model.model import Model
from model.utils import BGColor

class ConfigureRenderer(Renderer):
    
    """
    Title: Game Settings
    
    Number of enemies: button (1-10)
    Number of lives: button (1-10)
    Numberf of h for Regenerators: button (1-10)
    Frequency of chameleon color change: button (1-10)
    """
    
    def __init__(self):
        self.HEIGHT = 860
        self.WIDTH = 600
        
    def draw_text(self):
        pyxel.text(200, 100, "Game Configuration", BGColor.WHITE)
        pyxel.text(300, 100, "Number of enemies", BGColor.WHITE)
        pyxel.text(400, 100, "Number of lives", BGColor.WHITE)
        pyxel.text(500, 100, "Numberf of h for Regenerators", BGColor.WHITE)
        pyxel.text(600, 100, "Frequency of chameleon color change",  BGColor.WHITE)
        
    def draw_background(self):
        pyxel.cls(BGColor.BLACK)
       
    def draw_buttons(self):
        # to add. maybe even make this a textbox?
        
    def draw(self, model: Model):
        self.draw_text()
        self.draw_background()