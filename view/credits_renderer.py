# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.utils import BGColor, Screen
from model.sprites import menu_sprites

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager

class CreditsRenderer(Renderer):
    def __init__(self, m : Model, screen_manager : ScreenManager):
        super().__init__(m, screen_manager)
        
        self._exit_button: ButtonComponent = ButtonComponent( \
            assoc_func = self.leave_screen,
            pyxel_set=menu_sprites["blank"],
            x=10, y=10,
            w=40, h=40,
            text="EXIT"
        )
        
    def draw_background(self) -> None:
        ...
    
    def draw_credits(self) -> None:
        ...    
        
    def leave_screen(self) -> None:
        self.screen_manager.screen = Screen.START
        
    def update(self) -> None:
        self._exit_button.update()
        
    def draw(self) -> None:
        self.draw_background()
        self.draw_credits()
        self._exit_button.draw()