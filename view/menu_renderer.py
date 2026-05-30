# pyright: strict

import pyxel

from renderer import Renderer
from model.model import Model, PendingAction
from model.utils import BGColor
from view.components.button import ButtonComponent

MENU_X = 200
MENU_Y = 50
MENU_W = 660
MENU_H = 500

BTN_X  = MENU_X + MENU_W // 2 - 75
BTN_W  = 150
BTN_H  = 30
BTN_GAP = 40


class MenuRenderer(Renderer):

    def __init__(self, model: Model):
        self._model = model
        
        self._buttons: list[ButtonComponent] = [
            ButtonComponent(
                assoc_func=model.restart_game,
                x=BTN_X, y=MENU_Y + 80,
                w=BTN_W, h=BTN_H,
                text="Restart Game"
            ),
            ButtonComponent(
                assoc_func=lambda: model.set_pending_action(PendingAction.VIEW_LEADERBOARD),
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP,
                w=BTN_W, h=BTN_H,
                text="View Leaderboard"
            ),
            ButtonComponent(
                assoc_func=model.switch_game_mode,
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 2,
                w=BTN_W, h=BTN_H,
                text="Switch Game Mode"
            ),
            ButtonComponent(
                assoc_func=model.open_configure,
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 3,
                w=BTN_W, h=BTN_H,
                text="Configure Game Settings"
            ),
            ButtonComponent(
                assoc_func=model.close_menu,
                x=BTN_X, y=MENU_Y + 80 + BTN_GAP * 4,
                w=BTN_W, h=BTN_H,
                text="Back"
            ),
        ]
    
    def draw_background(self) -> None:
        pyxel.rect(MENU_X, MENU_Y, MENU_W, MENU_H, BGColor.BLACK)
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