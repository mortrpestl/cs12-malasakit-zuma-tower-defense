from __future__ import annotations

from model.utils import Screen
from model.model import Model
from view.View import View
from round_controller import RoundController
from collision_controller import CollisionController

from view.grid_renderer import GridRenderer
from view.hud_renderer import HUDRenderer

import pyxel

class Controller:
    def __init__(self, m: Model, v: View):
        self.__model: Model = m
        self.__view: View = v
        self.__collision_controller = CollisionController(m)
        self.__round_controller = RoundController(m)
        self.__grid_renderer = GridRenderer(m)
        self.__hud_renderer = HUDRenderer(m)
    
    def start_game(self):
        pyxel.init(self.__view.screen_w, self.__view.screen_h, fps=240)
        self.__view.init()
        pyxel.run(self.update, self.draw_game)
        
    def update(self):   
        self.__view.reset_screen()
        self.__round_controller.update()
        self.__collision_controller.update()
        self.__hud_renderer.update()
        match self.__view.get_current_screen:
            case Screen.GAME:
                if not self.__model.is_game_over:
                    if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                        self.__model.bullets.append(self.__model.player.shoot(pyxel.mouse_x, pyxel.mouse_y))
                else:
                    ...
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
        # self.__grid_renderer.draw_game_map()
        # self.__grid_renderer.draw_zuma_tower()
        # self.__grid_renderer.draw_ball_to_shoot()
        self.__view.entity_renderer.draw(self.__model)
        self.__hud_renderer.draw()

    def ask_confirmation(self):
        # essentially draw confirmation but we need a bool as response
        ...

    def draw_leaderboard(self):
        ... 

    def draw_menu(self):
        ...

    def draw_game_over(self):
        ...