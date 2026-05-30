# pyright: strict

import pyxel

from renderer import Renderer
from model.model import Model
from model.utils import BGColor, GameMode
from view.components.button import ButtonComponent

PANEL_X = 200
PANEL_Y = 50
PANEL_W = 660
PANEL_H = 500
CENTER_X = PANEL_X + PANEL_W // 2


class StartRenderer(Renderer):

    def __init__(self, model: Model):
        super().__init__(model)

        self._btn_campaign = ButtonComponent(
            assoc_func=lambda: self._model.start_game(GameMode.CAMPAIGN),
            x=CENTER_X - 160, y=PANEL_Y + 260,
            w=120, h=40,
            text="Campaign"
        )
        self._btn_endless = ButtonComponent(
            assoc_func=lambda: self._model.start_game(GameMode.ENDLESS),
            x=CENTER_X + 40, y=PANEL_Y + 260,
            w=120, h=40,
            text="Endless"
        )
        self._btn_leaderboard = ButtonComponent(
            assoc_func=lambda: self._model.set_pending_action(PendingAction.VIEW_LEADERBOARD),
            x=CENTER_X - 160, y=PANEL_Y + 330,
            w=320, h=40,
            text="Leaderboard"
        )
        self._btn_credits = ButtonComponent(
            assoc_func=self._model.open_credits,
            x=CENTER_X - 160, y=PANEL_Y + 390,
            w=320, h=40,
            text="Credits"
        )

    def draw_background(self) -> None:
        pyxel.rect(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.BLACK)
        pyxel.rectb(PANEL_X, PANEL_Y, PANEL_W, PANEL_H, BGColor.WHITE)

    def draw_title(self) -> None:
        pyxel.text(CENTER_X - 30, PANEL_Y + 80,  "ZUMA:",    BGColor.WHITE)
        pyxel.text(CENTER_X + 10, PANEL_Y + 80,  "TOWER",   BGColor.WHITE)
        pyxel.text(CENTER_X + 10, PANEL_Y + 100, "DEFENSE", BGColor.WHITE)

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