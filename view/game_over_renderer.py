# pyright: strict

import pyxel

from string import ascii_uppercase
from view.renderer import Renderer

from model.model import Model
from model.utils import BGColor

from typing import Callable

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager
from view.sprites import menu_sprites

PANEL_X = 0
PANEL_Y = 0
PANEL_W = 600
PANEL_H = 840
CENTER_X = PANEL_X + PANEL_W // 2

BTN_W = 80
BTN_H = 30

KEYS = [ pyxel.KEY_A
       , pyxel.KEY_B
       , pyxel.KEY_C
       , pyxel.KEY_D
       , pyxel.KEY_E
       , pyxel.KEY_F
       , pyxel.KEY_G
       , pyxel.KEY_H
       , pyxel.KEY_I
       , pyxel.KEY_J
       , pyxel.KEY_K
       , pyxel.KEY_L
       , pyxel.KEY_M
       , pyxel.KEY_N
       , pyxel.KEY_O
       , pyxel.KEY_P
       , pyxel.KEY_Q
       , pyxel.KEY_R
       , pyxel.KEY_S
       , pyxel.KEY_T
       , pyxel.KEY_U
       , pyxel.KEY_V
       , pyxel.KEY_W
       , pyxel.KEY_X
       , pyxel.KEY_Y
       , pyxel.KEY_Z
       ]
CHAR = [char for char in ascii_uppercase]

class GameOverRenderer(Renderer):

    def __init__(self, model: Model, sm: ScreenManager, on_restart: Callable[[], None]):
        super().__init__(model, sm)
        self._name_input: str = ""
        self.__on_restart = on_restart

        self._btn_yes = ButtonComponent(
            assoc_func=self.__on_restart,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X - 90, y=PANEL_Y + 380,
            w=BTN_W, h=BTN_H,
            text="Yes"
        )
        self._btn_exit = ButtonComponent(
            assoc_func=self.quit,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X + 10, y=PANEL_Y + 380,
            w=BTN_W, h=BTN_H,
            text="Exit"
        )

    def draw_background(self) -> None:
        pyxel.rect(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.BLACK)
        pyxel.rectb(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.WHITE)

    def draw_result(self) -> None:
        if self._model.player.lives > 0:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Congrats!", BGColor.WHITE)
        else:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Game Over!", BGColor.WHITE)

        mode_str = self._model.mode.value
        pyxel.text(CENTER_X - len(mode_str) * 3, PANEL_Y + 100, f"({mode_str})", BGColor.LIGHT_GRAY)

    def draw_name_input(self) -> None:
        pyxel.text(CENTER_X - 10, PANEL_Y + 200, "Name", BGColor.WHITE)
        pyxel.rectb(CENTER_X - 40, PANEL_Y + 215, 80, 25, BGColor.WHITE)
        pyxel.text(CENTER_X - 35, PANEL_Y + 222, self._name_input, BGColor.WHITE)

    def draw_play_again(self) -> None:
        pyxel.text(CENTER_X - 25, PANEL_Y + 350, "Play again?", BGColor.WHITE)
        self._btn_yes.draw()
        self._btn_exit.draw()

    def _update_name_input(self) -> None:
        for char_code, output in zip(KEYS, CHAR):
            if pyxel.btnp(char_code):
                if len(self._name_input) < 12:
                    self._name_input += output
        if pyxel.btnp(pyxel.KEY_BACKSPACE) and self._name_input:
            self._name_input = self._name_input[:-1]

    def quit(self) -> None:
        pyxel.quit()
    
    def update(self) -> None:
        self._update_name_input()
        self._btn_yes.update()
        self._btn_exit.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_result()
        self.draw_name_input()
        self.draw_play_again()