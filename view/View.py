from __future__ import annotations

from model.utils import (
    BGColor, Screen
)
from model.sprites import menu_sprites
from view.entity_renderer import EntityRenderer
from view.components.button import ButtonComponent

import pyxel

# from view.configure_renderer import ConfigureRenderer
# from view.confirm_renderer import ConfirmRenderer
# from view.hud_renderer import HUDRenderer
# # from view.leaderboard_renderer import LeaderboardRenderer

# from view.Renderer import Renderer

from typing import ClassVar

class Sound:
    SOUNDSET : ClassVar[list[int]] = list(range(6))

    # TODO rename all functions below to more useful names
    # OST plays on CH 0, Sound effects on CH 3
    @property
    def is_music_playing(self) -> bool:
        return bool(pyxel.play_pos(0))
    
    def sfx_0(self):
        pyxel.play(3, self.SOUNDSET[0])

    def hit_sound(self):
        pyxel.play(3, self.SOUNDSET[4])

    def kill_sound(self):
        pyxel.play(3, self.SOUNDSET[5])

    def ost_0(self):
        pyxel.playm(0, loop=True)

    def stop_music(self):
        pyxel.stop

MENU_X = 0
MENU_Y = 0
MENU_W = 600
MENU_H = 840

BTN_X  = MENU_X + MENU_W // 2 - 75
BTN_W  = 150
BTN_H  = 30
BTN_GAP = 40

class View:

    def __init__(self, width : int, height : int, frames : int):
        self._bg_color : int = BGColor.PEACH
        self._screen_w : int = width
        self._screen_h : int = height
        self._frames_s : int = frames
        self._sound_fx : Sound = Sound()

    def init(self):
        pyxel.load("view/pyxres_files/pyxel_basic_resources.pyxres")
        pyxel.mouse(True)

    @property
    def sound_fx(self) -> Sound:
        return self._sound_fx

    @property
    def screen_h(self) -> int:
        return self._screen_h

    @property
    def screen_w(self) -> int:
        return self._screen_w

    def reset_screen(self, screen: Screen) -> None:
        col : BGColor = BGColor.PEACH if screen is Screen.GAME \
                   else BGColor.BLACK
        
        pyxel.cls(col)