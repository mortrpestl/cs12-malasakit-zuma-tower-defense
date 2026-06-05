# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.utils import (
    BGColor
)

from view.screen_manager import ScreenManager

TUNNEL_COLOR = BGColor.PINK
PATH_COLOR = BGColor.BROWN

class GridRenderer(Renderer):
    def __init__(self, m: Model, screen_manager: ScreenManager):
        super().__init__(m, screen_manager)
        self.__cell_width = m.config.width / m.config.cols
        self.__cell_height = m.config.height / m.config.rows
    
    def draw(self):
        for path in self._model.stage.paths:
            for cell in path.cells:
                color = TUNNEL_COLOR if cell.is_tunnel else PATH_COLOR
                pyxel.rect(cell.x * self.__cell_width, cell.y * self.__cell_height + 40, self.__cell_width, self.__cell_height, color)
    
    def update(self):
        pass