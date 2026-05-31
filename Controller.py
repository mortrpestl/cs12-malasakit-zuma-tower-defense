from __future__ import annotations

from model.utils import Screen
from model.model import Model
from view.View import View

import pyxel

class Controller:
    def __init__(self, m: Model, v: View):
        self.__model: Model = m
        self.__view: View = v
    
    def start_game(self):
        pyxel.init(self.__view.screen_w, self.__view.screen_h)
        self.__view.init()
        pyxel.run(self.update, self.draw_game)
        
    def update(self):   
        self.__view.reset_screen()

        match self.__view.get_current_screen:
            case Screen.GAME:
                if not self.__model.is_game_over:
                    self.__view.convert_mouse_click_color()
                    self.__view.convert_mouse_pos_rotation()
                    self.draw_game()
                else:
                    ...
            case Screen.MENU:
                ...
            case Screen.LEADERBOARD:
                self.draw_leaderboard()
            case Screen.GAME_OVER:
                self.draw_menu()

    def draw_game(self):
        self.__view.draw_game_map()
        self.__view.draw_zuma_tower()
        self.__view.draw_ball_to_shoot()
        # self._view.draw hud()

    def ask_confirmation(self):
        # essentially draw confirmation but we need a bool as response
        ...

    def draw_leaderboard(self):
        ... 

    def draw_menu(self):
        ...

    def draw_game_over(self):
        ...