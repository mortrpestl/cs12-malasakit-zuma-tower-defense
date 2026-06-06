# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.utils import BGColor, LeaderboardEntry, GameMode, Screen
from view.screen_manager import ScreenManager
from view.components.button import ButtonComponent
from view.sprites import menu_sprites

BOARD_W = 500
BOARD_H = 500
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 30
BUTTON_GAP = 80
BOTTOM_MARGIN = 60

TOP_MARGIN = 60
MIDDLE_GAP = 60
ENTRY_GAP = 20
COLUMN_WIDTH = 150

class LeaderboardRenderer(Renderer):

    def __init__(self, model : Model, sm: ScreenManager):
        super().__init__(model, sm)
        self.__config = model.config
        self.__sm = sm
        x = (self.__config.screen_width - BOARD_W) // 2 + (BOARD_W - 2 * BUTTON_WIDTH - BUTTON_GAP) // 2
        
        y_end = (self.__config.height + BOARD_H) // 2
        self.__go_home_btn = ButtonComponent(
            assoc_func=self.go_start,
            pyxel_set=menu_sprites["misc"],
            x=x, y=y_end-BOTTOM_MARGIN,
            w=BUTTON_WIDTH, h=BUTTON_HEIGHT,
            text="Back to Home"
        )
        self.__go_menu_btn = ButtonComponent(
            assoc_func=self.go_menu,
            pyxel_set=menu_sprites["misc"],
            x=x, y=y_end-BOTTOM_MARGIN,
            w=BUTTON_WIDTH, h=BUTTON_HEIGHT,
            text="Back to Menu"
        )
        
    @property
    def model(self):
        return self._model
    
    def draw_background(self) -> None:
        x = (self.__config.width - BOARD_W) / 2
        y = (self.__config.height - BOARD_H) / 2
        pyxel.rectb(x, y, BOARD_W, BOARD_H, BGColor.WHITE)

    def draw_column(self, entries: list[LeaderboardEntry], x: int, label: str) -> None:
        HEADER_Y = (self.__config.height - BOARD_H) // 2 + TOP_MARGIN
        ENTRY_Y = HEADER_Y + TOP_MARGIN
        pyxel.text(x, HEADER_Y, label, BGColor.WHITE)

        if not entries:
            pyxel.text(x, ENTRY_Y, "No players yet!", BGColor.LIGHT_GRAY)
            return

        for i, entry in enumerate(entries[:7]): # cap to Top 7 to avoid overflow?
            # TODO ! also cap the inpu tof player name
            y = ENTRY_Y + i * ENTRY_GAP
            pyxel.text(x, y, f"{i + 1}  {entry.name}  {entry.score}", BGColor.WHITE)

    def draw(self) -> None:
        COL_CAMPAIGN_X = (self.__config.width - BOARD_W) // 2 + (BOARD_W - 2 * COLUMN_WIDTH - MIDDLE_GAP) // 2
        COL_ENDLESS_X = COL_CAMPAIGN_X + MIDDLE_GAP + COLUMN_WIDTH
        self.draw_background()
        self.draw_column(self._model.leaderboards[GameMode.CAMPAIGN].get_winners(), COL_CAMPAIGN_X, "Campaign")
        self.draw_column(self._model.leaderboards[GameMode.ENDLESS].get_winners(), COL_ENDLESS_X, "Endless")
        if self.screen_manager.previous_screen is Screen.MENU:
            self.__go_menu_btn.draw()
        else:
            self.__go_home_btn.draw()
        
    def update(self):
        if self.screen_manager.previous_screen is Screen.MENU:
            self.__go_menu_btn.update()
        else:
            self.__go_home_btn.update()

    def go_start(self):
        self.__sm.screen = Screen.START

    def go_menu(self):
        self.__sm.screen = Screen.MENU