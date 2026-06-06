# pyright: strict

import pyxel

from view.renderer import Renderer
from model.model import Model
from model.utils import BGColor, Screen
from view.sprites import menu_sprites

from view.components.button import ButtonComponent
from view.screen_manager import ScreenManager

PANEL_X = 0
PANEL_Y = 0
PANEL_W = 600
PANEL_H = 840
CENTER_X = PANEL_X + PANEL_W // 2

class CreditsRenderer(Renderer):
    def __init__(self, m : Model, screen_manager : ScreenManager):
        super().__init__(m, screen_manager)
        
        self._exit_button: ButtonComponent = ButtonComponent( \
            assoc_func = self.leave_screen,
            pyxel_set=menu_sprites["blank"],
            x=10, y=10,
            w=40, h=40,
            text="EXIT"
        )
        
    def draw_background(self) -> None:
        pyxel.cls(BGColor.BLACK)
    
    def draw_credits(self) -> None:
        pyxel.text(CENTER_X - 15, PANEL_Y + 20, "CREDITS", BGColor.WHITE)
        pyxel.text(CENTER_X - 15, PANEL_Y + 60, "MEMBERS", BGColor.WHITE)
        
        membs: list[str] = ["DANIEL JACOB CALIM", "JUSTIN NICOLAS CAMACHO", "DIOGN LEI MORTERA", "IEUAN DAVID VINLUAN"]
        
        for i, name in enumerate(membs):
            pyxel.text(CENTER_X - len(name) * 15/7, PANEL_Y + 80 + 10 * i, name, BGColor.WHITE) 
        
        contribs: list[list[str]] = [
            [
                "Creatives",
                "Background music and sound effects",
                "Map, round, level generation",
                "Project management"
            ],
            [
                "View, Creatives, Controller", 
                "Sprites of towers and enemies", 
                "Sprite integration and optimization",
                "Major improvements of renderers",
                "Advanced tower placement system integration",
                "Advanced view switching logic integration",
                "LLM Transcription",
            ],
            [
                "View, Controller",
                "Button component for use in different renderers",
                "Mockups and blueprints for the Renderers (Leaderboard, Game Over, Start, HUD, Start)",
                "draw() and update() of Renderers (Leaderboard, Game Over, Start, HUD, Start)",
                "Preparation of Renderer parameters for Controller",
                "Tower placement base logic",
                "View switching base logic",
            ],
            [
                "Model, View, Controller",
                "implementation of entity (bullet, enemies, etc.) behavior in-game",
                "Implementations of round controller, collision controller, controller",
                "Leaderboard renderer, entity renderer, grid renderer",
                "JSON processing",
                "Leaderboard handling"
            ]
        ]
        
        pyxel.text(CENTER_X - 13 * 15/7, PANEL_Y + 160, "CONTRIBUTIONS", BGColor.WHITE)
        
        new_y : int = PANEL_Y + 180
        for i, (name, lines) in enumerate(zip(membs, contribs)):
            pyxel.text(CENTER_X - len(name) * 15/7, new_y, name, BGColor.WHITE)
            
            for j, line in enumerate(lines):
                pyxel.text(CENTER_X - len(line) * 15/7, new_y + 20 + 10 * j, line, BGColor.WHITE)
                
            new_y += 30 + 10 * len(lines)
        
        pyxel.text(CENTER_X - 14 * 15/7, new_y + 40, "SPECIAL THANKS", BGColor.WHITE)
            
        thanks: list[str] = [
            "Anthropic", 
            "Battle of Polytopia", 
            "Claude", 
            "Kevin Atienza", 
            "Mrekk",
            "\"Myself for Living\"",
            "Kuya Basti Ortiz", 
            "OpenAI",
            "Risa Hontiveros",
            "Win Gatchalian"
        ]
        
        new_y += 60
        for line in thanks:
            pyxel.text(CENTER_X - len(line) * 15/7, new_y + 10, line, BGColor.WHITE)
            new_y += 10
              
        pyxel.text(CENTER_X - 39 * 15/7, new_y + 50, "Thanks for playing ZUMA: TOWER DEFENSE!", BGColor.WHITE)
           
        
    def leave_screen(self) -> None:
        self.screen_manager.screen = Screen.START
        
    def update(self) -> None:
        self._exit_button.update()
        
    def draw(self) -> None:
        self.draw_background()
        self.draw_credits()
        self._exit_button.draw()