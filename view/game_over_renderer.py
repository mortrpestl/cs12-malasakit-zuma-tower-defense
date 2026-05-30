# pyright: strict

import pyxel

from renderer import Renderer
from model.model import Model
from model.utils import BGColor
from view.components.button import ButtonComponent

PANEL_X = 200
PANEL_Y = 50
PANEL_W = 660
PANEL_H = 500
CENTER_X = PANEL_X + PANEL_W // 2

BTN_W = 80
BTN_H = 30


class GameOverRenderer(Renderer):

    def __init__(self, model: Model):
        super().__init__(model)
        self._name_input: str = ""

        self._btn_yes = ButtonComponent(
            assoc_func=lambda: self._model.restart_game,
            x=CENTER_X - 90, y=PANEL_Y + 380,
            w=BTN_W, h=BTN_H,
            text="Yes"
        )
        self._btn_exit = ButtonComponent(
            assoc_func=lambda: self._model.quit(),
            x=CENTER_X + 10, y=PANEL_Y + 380,
            w=BTN_W, h=BTN_H,
            text="Exit"
        )

    def draw_background(self) -> None:
        pyxel.rect(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.BLACK)
        pyxel.rectb(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.WHITE)

    def draw_result(self) -> None:
        if self._model.is_winner:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Congrats!", BGColor.WHITE)
        else:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Game Over!", BGColor.WHITE)

        mode_str = self._model.mode.value
        pyxel.text(CENTER_X - len(mode_str) * 2, PANEL_Y + 100, f"({mode_str})", BGColor.LIGHT_GRAY)

    def draw_name_input(self) -> None:
        pyxel.text(CENTER_X - 10, PANEL_Y + 200, "Name", BGColor.WHITE)
        pyxel.rectb(CENTER_X - 40, PANEL_Y + 215, 80, 25, BGColor.WHITE)
        pyxel.text(CENTER_X - 35, PANEL_Y + 222, self._name_input, BGColor.WHITE)

    def draw_play_again(self) -> None:
        pyxel.text(CENTER_X - 25, PANEL_Y + 350, "Play again?", BGColor.WHITE)
        self._btn_yes.draw()
        self._btn_exit.draw()

    def _update_name_input(self) -> None:
        for char_code in range(ord('A'), ord('Z') + 1):
            if pyxel.btnp(char_code):
                if len(self._name_input) < 12:
                    self._name_input += chr(char_code)
        if pyxel.btnp(pyxel.KEY_BACKSPACE) and self._name_input:
            self._name_input = self._name_input[:-1]

    def update(self) -> None:
        self._update_name_input()
        self._btn_yes.update()
        self._btn_exit.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_result()
        self.draw_name_input()
        self.draw_play_again()