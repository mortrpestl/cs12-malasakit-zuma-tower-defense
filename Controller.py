from __future__ import annotations

from dataclasses import dataclass
from model.model import Model
from view.View import View

import pyxel

@dataclass
class Controller:
    _model: Model
    _view: View
    
    def start_game(self):
        pyxel.init(self._view.screen_w, self._view.screen_h)
        self._view.init()
        pyxel.run(self.update, self.draw)
        
    def update(self):
        view: View = self._view
        
        view.convert_mouse_click_color()
        view.convert_mouse_pos_rotation()
        view.reset_screen()
        
    def draw(self):
        view : View = self._view
        
        view.draw_game_map()
        view.draw_zuma_tower()
        view.draw_ball_to_shoot()