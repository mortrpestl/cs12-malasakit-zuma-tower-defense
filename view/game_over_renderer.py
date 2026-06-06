# pyright: strict

import pyxel

from string import ascii_uppercase
from view.renderer import Renderer

from model.model import Model
from model.utils import BGColor, LeaderboardEntry

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
       , pyxel.KEY_0
       , pyxel.KEY_1
       , pyxel.KEY_2
       , pyxel.KEY_3
       , pyxel.KEY_4
       , pyxel.KEY_5
       , pyxel.KEY_6
       , pyxel.KEY_7
       , pyxel.KEY_8
       , pyxel.KEY_9
       ]
CHAR = [char for char in ascii_uppercase] + list("123456789")

class GameOverRenderer(Renderer):

    def __init__(self, model: Model, sm: ScreenManager, on_restart: Callable[[], None]):
        super().__init__(model, sm)
        self._name_input: str = ""
        
        self._inputted: bool = False
        self._twoclick: bool = False
        self._no_name: bool = False
        self._charnot: bool = False
        
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
        if self._model.is_winner:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Congrats!", BGColor.WHITE)
        else:
            pyxel.text(CENTER_X - 20, PANEL_Y + 80,  "Game Over!", BGColor.WHITE)

        mode_str = self._model.mode.value
        pyxel.text(CENTER_X - 20, PANEL_Y + 100, f"({mode_str})", BGColor.LIGHT_GRAY)
        pyxel.text(CENTER_X - 45, PANEL_Y + 110, f"You survived {self._model.current_round} {'round' if self._model.current_round == 1 else 'rounds'}!", BGColor.WHITE)

    def draw_name_input(self) -> None:
        pyxel.text(CENTER_X - 10, PANEL_Y + 200, "Name", BGColor.WHITE)
        pyxel.rectb(CENTER_X - 40, PANEL_Y + 215, 80, 25, BGColor.WHITE)
        pyxel.text(CENTER_X - len(self._name_input) * 2, PANEL_Y + 226, self._name_input, BGColor.WHITE)

    def draw_char_exceeded(self) -> None:
        pyxel.text(CENTER_X - 72.5, PANEL_Y + 250, "Entries cannot exceed 12 characters!", BGColor.WHITE)

    def draw_no_name_error(self) -> None:
        pyxel.text(CENTER_X - 73, PANEL_Y + 250, "Add a name for the leaderboard entry!", BGColor.WHITE)
        
    def draw_inputted_notif(self) -> None:
        pyxel.text(CENTER_X - 55, PANEL_Y + 260, "Entry passed to leaderboard!", BGColor.WHITE)
        
    def draw_twoclick_notif(self) -> None:
        pyxel.text(CENTER_X - 72.5, PANEL_Y + 270, "Cannot pass two entries at one time!", BGColor.WHITE)

    def draw_play_again(self) -> None:
        pyxel.text(CENTER_X - 25, PANEL_Y + 350, "Play again?", BGColor.WHITE)
        self._btn_yes.draw()
        self._btn_exit.draw()

    def _update_name_input(self) -> None:
        for char_code, output in zip(KEYS, CHAR):
            if pyxel.btnp(char_code):
                self._no_name = False
                if len(self._name_input) < 12:
                    self._name_input += output
                else:
                    self._charnot = True
        if pyxel.btnp(pyxel.KEY_BACKSPACE) and self._name_input:
            self._charnot = False
            self._name_input = self._name_input[:-1]
        if pyxel.btnp(pyxel.KEY_RETURN):
            if not self._name_input:
                self._no_name = True
            
            elif not self._inputted:    
                entry = LeaderboardEntry(self._name_input, self._model.current_round, self._model.mode)
                self._model.leaderboards[self._model.mode].add_winner(entry)
                self._no_name = False
                self._inputted = True
                
            elif self._inputted:
                self._twoclick = True
    
    def reset(self) -> None:
        self._name_input = ""
        self._inputted = False
        self._twoclick = False
        self._no_name = False
        self._charnot = False

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
        if self._charnot:
            self.draw_char_exceeded()
        if self._no_name:
            self.draw_no_name_error()
        if self._inputted:
            self.draw_inputted_notif()
        if self._twoclick:
            self.draw_twoclick_notif()
        self.draw_play_again()