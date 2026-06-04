from __future__ import annotations

from model.utils import (
    BGColor, Direction, GameMode, Screen,
    EnemyType, LeaderboardEntry,
    Settings, WaveConfig, get_next_color
)
from view.entity_renderer import EntityRenderer
from view.grid_renderer import GridRenderer
from view.hud_renderer import HUDRenderer
import pyxel

# from view.configure_renderer import ConfigureRenderer
# from view.confirm_renderer import ConfirmRenderer
# from view.hud_renderer import HUDRenderer
# # from view.leaderboard_renderer import LeaderboardRenderer
# from view.menu_renderer import MenuRenderer
# from view.Renderer import Renderer

from typing import ClassVar

class Sound:
    SOUNDSET : ClassVar[list[int]] = list(range(6))

    def init(self):
        pyxel.load("view/pyxres_files/sounds.pyxres", exclude_tilemaps=True, exclude_images=True)

    # TODO rename all functions below to mor    e useful names
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

class View:

    def __init__(self, width : int, height : int, frames : int):
        self._bg_color : int = BGColor.PEACH
        self._screen_w : int = width
        self._screen_h : int = height
        self._frames_s : int = frames
        self._sound_fx : Sound = Sound()
        self._current_screen: Screen = Screen.GAME
        self.entity_renderer = EntityRenderer()

        # self._hud_renderer = 
        # self._grid_renderer = 
        # self._leaderboard_renderer = 
        # self._menu_renderer = 
        # self._start_renderer = 
        # self._configure_renderer = 
        # self._confirm_renderer = 




        self._current_screen: Screen = Screen.GAME

    def init(self):
        self._sound_fx.init()
        pyxel.load("view/pyxres_files/pyxel_basic_resources.pyxres", exclude_sounds=True, exclude_musics=True)
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

    @property
    def get_current_screen(self) -> Screen:
        return self._current_screen

    def set_current_screen(self, s: Screen):
        self._current_screen = s

    def reset_screen(self) -> None:
        pyxel.cls(BGColor.PEACH)
        
   