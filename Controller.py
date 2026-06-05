from __future__ import annotations

from model.utils import Screen
from model.model import Model
from view.View import View, Sound
from round_controller import RoundController
from collision_controller import CollisionController

from view.entity_renderer import EntityRenderer
from view.grid_renderer import GridRenderer
from view.hud_renderer import HUDRenderer
from view.menu_renderer import MenuRenderer

from view.screen_manager import ScreenManager

import pyxel

class Controller:
    def __init__(self, m: Model, v: View):
        self.__model: Model = m
        self.__view: View = v
        self.__sound: Sound = Sound()
        self.__fps = m.config.fps

        self.__collision_controller = CollisionController(m, self.__sound)
        self.__round_controller = RoundController(m)
        
        self.__screen_manager = ScreenManager(Screen.GAME)
        
        self.__entity_renderer = EntityRenderer()
        self.__grid_renderer = GridRenderer(m, self.__screen_manager)
        self.__hud_renderer = HUDRenderer(m, self.__screen_manager)
        self.__menu_renderer = MenuRenderer(m, self.__screen_manager, self.handle_restart)
    
    def start_game(self):
        pyxel.init(self.__view.screen_w, self.__view.screen_h, fps=self.__fps)
        self.__view.init()
        pyxel.run(self.update, self.draw)
        
    def update(self):   
        match self.__screen_manager.screen:
            case Screen.GAME:
                if not self.__sound.is_music_playing:
                    self.__sound.ost_0()

                if not self.__model.is_game_over:
                    self.__collision_controller.update()
                    self.__round_controller.update()
                    self.__hud_renderer.update()
                else:
                    ...
            case Screen.MENU:
                self.__menu_renderer.update()
            case Screen.LEADERBOARD:
                ...
            case Screen.GAME_OVER:
                ...
            case _:
                pass

    def draw(self):
        self.__view.reset_screen(self.__screen_manager.screen)
        
        match self.__screen_manager.screen:
            case Screen.GAME:
                self.__grid_renderer.draw()
                if not self.__model.is_game_over:
                    self.__entity_renderer.draw(self.__model)
                self.__hud_renderer.draw()
            case Screen.MENU:
                self.__menu_renderer.draw()
            case Screen.LEADERBOARD:
                ...
            case Screen.GAME_OVER:
                ...
            case _:
                pass

    def handle_restart(self):
        self.__model.restart_game()
        self.__round_controller.reset()
        self.__screen_manager.screen = Screen.GAME