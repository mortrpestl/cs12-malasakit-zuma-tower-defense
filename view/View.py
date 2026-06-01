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

    # TODO rename all functions below to more useful names

    def sfx_0(self):
        pyxel.play(0, self.SOUNDSET[0])

    def sfx_1(self):
        pyxel.play(1, self.SOUNDSET[1])

    def sfx_2(self):
        pyxel.play(2, self.SOUNDSET[2])

    def sfx_3(self):
        pyxel.play(3, self.SOUNDSET[3])

    def sfx_4(self):
        pyxel.play(4, self.SOUNDSET[4])

    def sfx_5(self):
        pyxel.play(5, self.SOUNDSET[5])


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
        pyxel.load("view/pyxres_files/zuma_basic_enemies.pyxres", exclude_sounds=True, exclude_musics=True)
        pyxel.load("view/pyxres_files/zuma_basic_towers.pyxres", exclude_sounds=True, exclude_musics=True)
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

    def draw_game_map(self) -> None:
        for i in range(15):
            for j in range(19):
                pyxel.rect(40 * i, 30 + 40 * j, 40, 40, 7 * (i % 2) + 7 * (j % 2))
        
   