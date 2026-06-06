# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.utils import BGColor, GameMode, Screen
from view.sprites import menu_sprites

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager

PANEL_X = 0
PANEL_Y = 0
PANEL_W = 600
PANEL_H = 840
CENTER_X = PANEL_X + PANEL_W // 2


class StartRenderer(Renderer):

    def __init__(self, model: Model, screen_manager: ScreenManager):
        super().__init__(model, screen_manager)

        self._btn_campaign = ButtonComponent(
            assoc_func=self.set_campaign,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X - 165, y=PANEL_Y + 260,
            w=150, h=30,
            text="Campaign"
        )
        self._btn_endless = ButtonComponent(
            assoc_func=self.set_endless,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X + 15, y=PANEL_Y + 260,
            w=150, h=30,
            text="Endless"
        )
        self._btn_leaderboard = ButtonComponent(
            assoc_func=self.view_leaderboard,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X - 165, y=PANEL_Y + 320,
            w=330, h=30,
            text="Leaderboard"
        )
        self._btn_credits = ButtonComponent(
            assoc_func=self.view_credits,
            pyxel_set=menu_sprites["misc"],
            x=CENTER_X - 165, y=PANEL_Y + 380,
            w=330, h=30,
            text="Credits"
        )

    def draw_background(self) -> None:
        pyxel.rect(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.BLACK)
        pyxel.rectb(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.WHITE)

    def draw_title(self) -> None:
        pyxel.text(CENTER_X - 30, PANEL_Y + 80,  "ZUMA:",    BGColor.WHITE)
        pyxel.text(CENTER_X + 10, PANEL_Y + 80,  "TOWER",   BGColor.WHITE)
        pyxel.text(CENTER_X + 10, PANEL_Y + 100, "DEFENSE", BGColor.WHITE)

    def set_campaign(self) -> None:
        if self.model.mode is GameMode.ENDLESS:
            self.model.switch_mode()
        self.screen_manager.screen = Screen.GAME
        
    def set_endless(self) -> None:
        if self.model.mode is GameMode.CAMPAIGN:
            self.model.switch_mode()
        self.screen_manager.screen = Screen.GAME
        
    def view_leaderboard(self) -> None:
        self.screen_manager.screen = Screen.LEADERBOARD
        
    def view_credits(self) -> None:
        self.screen_manager.screen = Screen.CREDITS
    
    def update(self) -> None:
        self._btn_campaign.update()
        self._btn_endless.update()
        self._btn_leaderboard.update()
        self._btn_credits.update()

    def draw(self) -> None:
        self.draw_background()
        self.draw_title()
        self._btn_campaign.draw()
        self._btn_endless.draw()
        self._btn_leaderboard.draw()
        self._btn_credits.draw()