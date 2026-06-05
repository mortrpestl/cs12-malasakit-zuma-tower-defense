# pyright: strict

import pyxel

from view.renderer import Renderer
from model.game_config import GameConfig
from model.model import Model
from model.utils import BGColor, Screen
from model.sprites import menu_sprites

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager

class ConfigureRenderer(Renderer):

    """
    Title: Game Settings

    Number of enemies: button (1-10)
    Number of lives: button (1-10)
    Number of h for Regenerators: button (1-10)
    Frequency of chameleon color change: button (1-10)
    """

    LABELS = ["Enemies", "Lives", "Regen HP", "Chameleon Freq"]

    def __init__(self, model : Model, screen_manager: ScreenManager):
        super().__init__(model, screen_manager)
        
        self.WIDTH = 600
        self.HEIGHT = 840
        
        config = self.model.config

        self._exit_button: ButtonComponent = ButtonComponent( \
            assoc_func = self.leave_screen,
            pyxel_set=menu_sprites["blank"],
            x=10, y=10,
            w=40, h=40,
            text="EXIT"
        )
        self._buttons: list[tuple[ButtonComponent, ButtonComponent]] = [
            (
                ButtonComponent( \
                    assoc_func=config.decrement_enemies, 
                    pyxel_set=menu_sprites["blank"],
                    x=300, y=150, 
                    w=40, h=40, 
                    text="-"),
                ButtonComponent( \
                    assoc_func=config.increment_enemies, 
                    pyxel_set=menu_sprites["blank"],
                    x=350, y=150, 
                    w=40, h=40, 
                    text="+"),
            ),
            (
                ButtonComponent( \
                    assoc_func=config.decrement_lives, 
                    pyxel_set=menu_sprites["blank"],
                    x=300, y=250,
                    w=40, h=40, 
                    text="-"),
                ButtonComponent( \
                    assoc_func=config.increment_lives, 
                    pyxel_set=menu_sprites["blank"],
                    x=350, y=250, 
                    w=40, h=40, 
                    text="+"),
            ),
            (
                ButtonComponent( \
                    assoc_func=config.decrement_regen_hp, 
                    pyxel_set=menu_sprites["blank"],
                    x=300, y=350, 
                    w=40, h=40, 
                    text="-"),
                ButtonComponent( \
                    assoc_func=config.increment_regen_hp, 
                    pyxel_set=menu_sprites["blank"],
                    x=350, y=350, 
                    w=40, h=40, 
                    text="+"),
            ),
            (
                ButtonComponent( \
                    assoc_func=config.decrement_chameleon_freq, 
                    pyxel_set=menu_sprites["blank"],
                    x=300, y=450, 
                    w=40, h=40, text="-"),
                ButtonComponent( \
                    assoc_func=config.increment_chameleon_freq, 
                    pyxel_set=menu_sprites["blank"],
                    x=350, y=450, 
                    w=40, h=40, 
                    text="+"),
            ),
        ]

    def leave_screen(self) -> None:
        self.screen_manager.screen = Screen.MENU
    
    def draw_background(self) -> None:
        pyxel.cls(BGColor.BLACK)

    def draw_text(self) -> None:
        values = [self.model.config.enemies, self.model.config.lives, self.model.config.regen_hp, self.model.config.chameleon_freq]

        pyxel.text(200, 100, "Game Configuration", BGColor.WHITE)
        for i, (label, value) in enumerate(zip(self.LABELS, values)):
            pyxel.text(200, 165 + i * 100, f"{label}: {value}", BGColor.WHITE)

    def update(self) -> None:
        self._exit_button.update()
        for dec, inc in self._buttons:
            dec.update()
            inc.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_text()
        self._exit_button.draw()
        for dec, inc in self._buttons:
            dec.draw()
            inc.draw()