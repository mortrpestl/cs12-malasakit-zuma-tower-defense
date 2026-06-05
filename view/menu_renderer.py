# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.sprites import menu_sprites
from model.utils import BGColor, GameMode, Screen

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager

MENU_X = 0
MENU_Y = 0
MENU_W = 600
MENU_H = 840

BTN_X  = MENU_X + MENU_W // 2 - 75
BTN_W  = 150
BTN_H  = 30
BTN_GAP = 40


class MenuRenderer(Renderer):

    def __init__(self, model: Model, screen_manager: ScreenManager):
        super().__init__(model, screen_manager)
        
        self._clicked: bool = False
        self._buttons: list[ButtonComponent] = [
            ButtonComponent(
                assoc_func= self.restart_game,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80,
                w=BTN_W, h=BTN_H,
                text="Restart Game"
            ),
            ButtonComponent(
                assoc_func= self.view_leaderboard,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP,
                w=BTN_W, h=BTN_H,
                text="View Leaderboard"
            ),
            ButtonComponent(
                assoc_func= self.switch_game_mode,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 2,
                w=BTN_W, h=BTN_H,
                text="Switch Game Mode"
            ),
            ButtonComponent(
                assoc_func= self.open_configure,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 3,
                w=BTN_W, h=BTN_H,
                text="Configure Game Settings"
            ),
            ButtonComponent(
                assoc_func= self.to_start_menu,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 4,
                w=BTN_W, h=BTN_H,
                text="Go to Start Menu"
            ),
            ButtonComponent(
                assoc_func= self.close_menu,
                pyxel_set = menu_sprites["misc"],
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 5,
                w=BTN_W, h=BTN_H,
                text="Back"
            ),
        ]
        
    def restart_game(self) -> None:
        print("work?")
        
    def view_leaderboard(self) -> None:
        self.screen_manager.screen = Screen.LEADERBOARD
        
    def switch_game_mode(self) -> None:
        self._model.switch_mode()
        self._clicked = True
        
    def open_configure(self) -> None:
        self.screen_manager.screen = Screen.CONFIGURE
        
    def to_start_menu(self) -> None:
        self.screen_manager.screen = Screen.START
        
    def close_menu(self) -> None:
        self.screen_manager.screen = Screen.GAME
    
    def draw_background(self) -> None:
        pyxel.rectb(MENU_X, MENU_Y, MENU_W, MENU_H, BGColor.WHITE)

    def draw_title(self) -> None:
        pyxel.text(MENU_X + MENU_W // 2 - 10, MENU_Y + 30, "MENU", BGColor.WHITE)

    def update(self) -> None:
        for btn in self._buttons:
            btn.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_title()
        for btn in self._buttons:
            btn.draw()
        if self._clicked:
            pyxel.text(MENU_X + MENU_W // 2 - 60, MENU_Y + 320, \
                f"Switched game mode to {'CAMPAIGN' if self._model.mode is GameMode.CAMPAIGN else 'ENDLESS'}",
                BGColor.WHITE
            )