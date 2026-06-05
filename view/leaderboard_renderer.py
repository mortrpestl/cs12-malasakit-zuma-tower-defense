# pyright: strict

import pyxel

from view.renderer import Renderer
from model.leaderboard import Leaderboard
from model.model import Model
from model.utils import BGColor, LeaderboardEntry

BOARD_X = 200
BOARD_Y = 50
BOARD_W = 660
BOARD_H = 500

COL_CAMPAIGN_X = BOARD_X + 50
COL_ENDLESS_X  = BOARD_X + BOARD_W // 2 + 50

HEADER_Y  = BOARD_Y + 30
ENTRY_Y   = BOARD_Y + 70
ENTRY_GAP = 20


class LeaderboardRenderer(Renderer):

    def __init__(self, model : Model, campaign: Leaderboard, endless: Leaderboard):
        self._model = model
        self._campaign_leaderboard = campaign 
        self._endless_leaderboard = endless
        
    @property
    def model(self):
        return self._model
    
    def draw_background(self) -> None:
        pyxel.rectb(BOARD_X, BOARD_Y, BOARD_W, BOARD_H, BGColor.WHITE)

    def draw_column(self, entries: list[LeaderboardEntry], x: int, label: str) -> None:
        pyxel.text(x, HEADER_Y, label, BGColor.WHITE)

        if not entries:
            pyxel.text(x, ENTRY_Y, "No players yet!", BGColor.LIGHT_GRAY)
            return

        for i, entry in enumerate(entries[:7]): # cap to Top 7 to avoid overflow?
            # TODO ! also cap the inpu tof player name
            y = ENTRY_Y + i * ENTRY_GAP
            pyxel.text(x, y, f"{i + 1}  {entry.name}  {entry.score}", BGColor.WHITE)

    def draw(self) -> None:
        self.draw_background()
        self.draw_column(self._campaign_leaderboard.get_winners(), COL_CAMPAIGN_X, "Campaign")
        self.draw_column(self._endless_leaderboard.get_winners(),  COL_ENDLESS_X,  "Endless")