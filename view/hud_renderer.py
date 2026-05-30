# pyright: strict

import pyxel

from renderer import Renderer
from model.model import Model
from model.utils import BGColor
from view.components.button import ButtonComponent

"""
HUD should have:
- Lives left: progress bar + "current/max" text
- Towers: selectable buttons (grayed out + disabled if count is 0)
- Title: "ZUMA: TOWER DEFENSE" on the right
"""

HUD_Y = 0
HUD_H = 30
HUD_W = 600


class HUDRenderer(Renderer):

    def __init__(self, model: Model):
    # TODO: Integrate XP cost of towers in the text 
        
        self._model = model 
        self._tower_buttons: list[ButtonComponent] = [
            ButtonComponent(assoc_func=lambda: model.select_tower(0), x=400, y=HUD_Y+5, w=40, h=40, text=f"{model.select_tower(0).cost}"),
            ButtonComponent(assoc_func=lambda: model.select_tower(1), x=450, y=HUD_Y+5, w=40, h=40, text=f"{model.select_tower(1).cost}"),
            ButtonComponent(assoc_func=lambda: model.select_tower(2), x=500, y=HUD_Y+5, w=40, h=40, text=f"{model.select_tower(2).cost}"),
        ]

    @property
    def model(self):
        return self._model    

    def draw_background(self) -> None:
        pyxel.rect(0, HUD_Y, HUD_W, HUD_H, BGColor.DARK_GRAY)

    def draw_lives(self) -> None:
        lives = self.model.player.lives
        max_lives = self.model.config.lives

        # progress bar
        bar_x, bar_y, bar_w, bar_h = 100, HUD_Y + 8, 100, 10
        pyxel.rect(bar_x, bar_y, bar_w, bar_h, BGColor.DARK_GRAY)
        filled = int(bar_w * lives / max_lives)
        pyxel.rect(bar_x, bar_y, filled, bar_h, BGColor.GREEN)

        pyxel.text(50, HUD_Y + 8, "Lives left", BGColor.WHITE)
        pyxel.text(bar_x, bar_y + 12, f"{lives}/{max_lives}", BGColor.WHITE)

    def draw_towers(self) -> None:
        for i, btn in enumerate(self._tower_buttons):
            count = self.model.tower_counts[i]
            disabled = count == 0
            btn._button_col = BGColor.DARK_GRAY if disabled else BGColor.LIGHT_GRAY
            btn.draw()
            # count below button
            pyxel.text(btn.x + 15, btn.y + btn.h + 2, str(count), BGColor.WHITE)

    def draw_title(self) -> None:
        pyxel.text(750, HUD_Y + 5,  "ZUMA:", BGColor.WHITE)
        pyxel.text(750, HUD_Y + 13, "TOWER", BGColor.WHITE)
        pyxel.text(750, HUD_Y + 21, "DEFENSE", BGColor.WHITE)

    def update(self) -> None:
        for i, btn in enumerate(self._tower_buttons):
            if self.model.tower_counts[i] > 0:
                btn.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_lives()
        self.draw_towers()
        self.draw_title()
        
        