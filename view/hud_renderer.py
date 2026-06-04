# pyright: strict

import pyxel

from copy import deepcopy

from view.renderer import Renderer
from model.model import Model
from model.cell import Cell
from model.entities.tower import Tower
from model.utils import BGColor, GameMode
from view.components.button import ButtonComponent

"""
HUD should have:
- Lives left: progress bar + "current/max" text
- Towers: selectable buttons (grayed out + disabled if count is 0)
- Title: "ZUMA: TOWER DEFENSE" on the right
"""

HUD_Y = 0
HUD_H = 40
HUD_W = 600

CELL_HEIGHT = 40
CELL_WIDTH = 40
TOP_BOTTOM_PADDING = 40

#tower placement:
    # click button for tower
    # click cell for tower
        # if not a valid cell placement 
            # if element at a certain Cell is not part of the Grid bounds -> "break tower placement mode"
            # if Cell in that certain coordinate is ( Path / not of Same tower type ) -> "break tower placement mode"
        # if valid cell placement  
            # if same Tower type   
                # if enough XP for tower upgrade, upgrade. otherwise, do nothing and "break tower placement mode"
            # if not same Tower type
                # "break tower placement mode"

class HUDRenderer(Renderer):

    def __init__(self, model: Model):
        self._model = model
        self._selected_tower: Tower | None = None
        self._path_cells: set[Cell] = {
            cell
            for path in model.stage.paths
            for cell in path.cells
        }
        self._tower_buttons: list[ButtonComponent] = [
            ButtonComponent( \
                assoc_func=lambda i=i: self._select_tower(i), 
                pyxel_set=model.towers[i].pyxel_set,
                pyxel_scale=model.towers[i].pyxel_scale,
                x=400 + i * 45, 
                y=HUD_Y, 
                w=40, h=40, 
                text=f"{model.towers[i].cost}") for i in range(len(self.model.towers))
        ]

    @property
    def model(self):
        return self._model

    def _select_tower(self, i: int) -> None:
        self._selected_tower = deepcopy(self.model.towers[i])
        
        # TROUBLESHOOTING CODE

    def _deselect_tower(self) -> None:
        self._selected_tower = None

    def _get_cell_from_click(self) -> Cell | None:
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        col = mx // CELL_WIDTH
        row = (my - TOP_BOTTOM_PADDING) // CELL_HEIGHT
        rows = self.model.config.rows
        cols = self.model.config.cols
        
        if 0 <= row < rows and 0 <= col < cols:
            return self.model.stage.grid.grid[row][col]
        
        
        return None

    def _handle_cell_click(self) -> None:
        if self._selected_tower is None:
            return
        if not pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            return

        cell = self._get_cell_from_click()

        # out of bounds
        if cell is None:
            self._deselect_tower()
            return

        # path cell (invalid)
        if cell in self._path_cells:
            self._deselect_tower()
            return

        # valid cell
        if cell.entity is None:
            # empty cell: place tower if enough XP
            if self.model.exp >= self._selected_tower.cost:
                self._selected_tower.x, self._selected_tower.y = cell.x, cell.y
                self._model.exp -= self._selected_tower.cost
                cell.entity = self._selected_tower
                self._model.bought_towers.append(self._selected_tower)
            
            self._deselect_tower()

        elif isinstance(cell.entity, Tower):
            existing: Tower = cell.entity
            if isinstance(existing, type(self._selected_tower)) and existing.level < 2:
                # same tower type (upgrade if >XP)
                if self.model.exp >= existing.cost:
                    self._model.exp -= self._selected_tower.cost
                    existing.upgrade()
                self._deselect_tower()
            else:
                # different tower type
                self._deselect_tower()

        else:
            # cell occupied by non-tower entity
            self._deselect_tower()

    def draw_background(self) -> None:
        pyxel.rect(0, HUD_Y, HUD_W, HUD_H, BGColor.DARK_GRAY)

    def draw_exp(self) -> None:
        pyxel.text(200, HUD_Y + 18, f"EXP: {self._model.exp}", BGColor.WHITE)
        
    def draw_rounds(self) -> None:
        pyxel.text(250, HUD_Y + 18, \
                   f"ROUND {self._model.current_round + 1} / {len(self._model.rounds)}" \
                   if self._model.mode is GameMode.CAMPAIGN else f" ROUND {self._model.current_round} / ∞",
                   BGColor.WHITE)    
        
    def draw_lives(self) -> None:
        lives = self.model.player.lives
        max_lives = self.model.config.lives

        bar_x, bar_y, bar_w, bar_h = 60, HUD_Y + 18, 100, 10
        pyxel.rect(bar_x, bar_y, bar_w, bar_h, BGColor.DARK_GRAY)
        filled = int(bar_w * lives / max_lives)
        pyxel.rect(bar_x, bar_y, filled, bar_h, BGColor.GREEN)

        pyxel.text(10, HUD_Y + 18, "Lives left", BGColor.WHITE)
        pyxel.text(bar_x, bar_y + 12, f"{lives}/{max_lives}", BGColor.WHITE)

    def draw_towers(self) -> None:
        for i, btn in enumerate(self._tower_buttons):
            tower = self.model.towers[i]
            disabled: bool = self.model.exp < tower.cost
            btn.button_col = BGColor.NAVY if disabled else BGColor.LIGHT_GRAY
            btn.draw()

    def draw_title(self) -> None:
        pyxel.text(550, HUD_Y + 10,  "ZUMA:", BGColor.WHITE)
        pyxel.text(550, HUD_Y + 18, "TOWER", BGColor.WHITE)
        pyxel.text(550, HUD_Y + 26, "DEFENSE", BGColor.WHITE)

    def update(self) -> None:
        for i, btn in enumerate(self._tower_buttons):
            if self.model.exp >= self.model.towers[i].cost:
                btn.update()
        self._handle_cell_click()
        
    def draw_bottom(self) -> None:
        pyxel.rect(0, HUD_Y + 800, HUD_W, HUD_H, BGColor.DARK_GRAY)

    def draw(self) -> None:
        self.draw_background()
        self.draw_lives()
        self.draw_exp()
        self.draw_rounds()
        self.draw_towers()
        self.draw_title()
        
        self.draw_bottom()
        