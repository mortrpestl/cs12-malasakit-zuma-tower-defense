# pyright: strict
from renderer import Renderer
from ..model.model import Model
from ..model.utils import BGColor

from components.button import ButtonComponent

import pyxel

    
class ConfirmRenderer(Renderer):
    def __init__(self, model: Model):
        super().__init__(model)
        self.HEIGHT = 860
        self.WIDTH = 600
        self.BUTTONS = \
            [ButtonComponent(assoc_func, x, y, w, h, button_col, text_col, text) 
                for (assoc_func, x, y, w, h, button_col, text_col, text) 
                in [
                    (self.confirm_yes, 100, 500, 150, 50, BGColor.GREEN, BGColor.WHITE, "Yes"),
                    (self.confirm_no, 350, 500, 150, 50, BGColor.RED, BGColor.WHITE, "No")
                ]
            ]
        
    def confirm_yes(self) -> None:
        self._model.confirm(True)

    def confirm_no(self) -> None:
        self._model.confirm(False)
        
    def draw(self) -> None:
        pyxel.cls(BGColor.BLACK)
        pyxel.text(self.WIDTH // 2, self.HEIGHT // 3,
                   f"Are you sure you want to {self._model.pending_action}?", BGColor.WHITE)
        for button in self.BUTTONS:
            button.draw()

    def update(self) -> None:
        for button in self.BUTTONS:
            button.update()