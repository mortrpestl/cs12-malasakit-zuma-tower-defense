from __future__ import annotations

from model.utils import Screen
from model.model import Model
from view.View import View
from round_controller import RoundController
from collision_controller import CollisionController

import pyxel

class Controller:
    def __init__(self, m: Model, v: View):
        self.__model: Model = m
        self.__view: View = v
        self.__collision_controller = CollisionController(m)
        self.__round_controller = RoundController(m)
    
    def start_game(self):
        pyxel.init(self.__view.screen_w, self.__view.screen_h, fps=240)
        self.__view.init()
        pyxel.run(self.update, self.draw_game)
        
    def update(self):   
        self.__view.reset_screen()
        self.__round_controller.update()
        self.__collision_controller.update()
        match self.__view.get_current_screen:
            case Screen.GAME:
                if not self.__model.is_game_over:
                    self.__view.convert_mouse_click_color()
                    self.__view.convert_mouse_pos_rotation()
                    self.draw_game()
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        self.__model.bullets.append(self.__model.player.shoot(pyxel.mouse_x, pyxel.mouse_y))
                        print([(bullet.x_abs, bullet.y_abs) for bullet in self.__model.bullets])
                    self.__view.entity_renderer.draw(self.__model)
                else:
                    ...
            case Screen.MENU:
                ...
            case Screen.LEADERBOARD:
                self.draw_leaderboard()
            case Screen.GAME_OVER:
                self.draw_menu()
            case _:
                pass

    def draw_game(self):
        self.__view.draw_game_map()
        self.__view.draw_zuma_tower()
        self.__view.draw_ball_to_shoot()
        self.__view.entity_renderer.draw(self.__model)
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