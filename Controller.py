from __future__ import annotations

from model.utils import Screen
from model.model import Model
from view.View import View, Sound
from round_controller import RoundController
from collision_controller import CollisionController

from view.grid_renderer import GridRenderer
from view.hud_renderer import HUDRenderer
import pyxel

class Controller:
    def __init__(self, m: Model, v: View):
        self.__model: Model = m
        self.__view: View = v
        self.__sound: Sound = Sound()
        self.__fps = m.config.fps

        self.__collision_controller = CollisionController(m, self.__sound)
        self.__round_controller = RoundController(m)
        self.__grid_renderer = GridRenderer(m)
        self.__hud_renderer = HUDRenderer(m)
    
    def start_game(self):
        pyxel.init(self.__view.screen_w, self.__view.screen_h, fps=self.__fps)
        self.__view.init()
        pyxel.run(self.update, self.draw_game)
        
    def update(self):   
        match self.__view.get_current_screen:
            case Screen.GAME:
                if not self.__sound.is_music_playing:
                    self.__sound.ost_0()

                if not self.__model.is_game_over:
                    self.__collision_controller.update()
                    self.__round_controller.update()
                    self.__view.reset_screen()
                    self.__hud_renderer.update()
                else:
                    print("GAME DONE")
            case Screen.MENU:
                ...
            case Screen.LEADERBOARD:
                ...
            case Screen.GAME_OVER:
                ...
            case _:
                pass

    def draw_game(self):
        self.__view.reset_screen()
        self.__grid_renderer.draw()
        if not self.__model.is_game_over:
            self.__view.entity_renderer.draw(self.__model)
        self.__hud_renderer.draw()

    def ask_confirmation(self):
        ...

    def draw_leaderboard(self):
        ... 

    def draw_menu(self):
        ...

    def draw_game_over(self):
        ...

