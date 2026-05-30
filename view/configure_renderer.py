# pyright: strict

import pyxel

from renderer import Renderer
from model.game_config import GameConfig
from model.utils import BGColor

from view.components.button import ButtonComponent

class ConfigureRenderer(Renderer):

    """
    Title: Game Settings

    Number of enemies: button (1-10)
    Number of lives: button (1-10)
    Number of h for Regenerators: button (1-10)
    Frequency of chameleon color change: button (1-10)
    """

    LABELS = ["Enemies", "Lives", "Regen HP", "Chameleon Freq"]

    def __init__(self, config: GameConfig):
        self.HEIGHT = 600
        self.WIDTH = 860

        self._buttons: list[tuple[ButtonComponent, ButtonComponent]] = [
            (
                ButtonComponent(assoc_func=config.decrement_enemies, x=300, y=150, w=40, h=40, text="-"),
                ButtonComponent(assoc_func=config.increment_enemies, x=350, y=150, w=40, h=40, text="+"),
            ),
            (
                ButtonComponent(assoc_func=config.decrement_lives, x=300, y=250, w=40, h=40, text="-"),
                ButtonComponent(assoc_func=config.increment_lives, x=350, y=250, w=40, h=40, text="+"),
            ),
            (
                ButtonComponent(assoc_func=config.decrement_regen_hp, x=300, y=350, w=40, h=40, text="-"),
                ButtonComponent(assoc_func=config.increment_regen_hp, x=350, y=350, w=40, h=40, text="+"),
            ),
            (
                ButtonComponent(assoc_func=config.decrement_chameleon_freq, x=300, y=450, w=40, h=40, text="-"),
                ButtonComponent(assoc_func=config.increment_chameleon_freq, x=350, y=450, w=40, h=40, text="+"),
            ),
        ]

    def draw_background(self) -> None:
        pyxel.cls(BGColor.BLACK)

    def draw_text(self, config: GameConfig) -> None:
        values = [config.enemies, config.lives, config.regen_hp, config.chameleon_freq]

        pyxel.text(200, 100, "Game Configuration", BGColor.WHITE)
        for i, (label, value) in enumerate(zip(self.LABELS, values)):
            pyxel.text(200, 165 + i * 100, f"{label}: {value}", BGColor.WHITE)

    def update(self) -> None:
        for dec, inc in self._buttons:
            dec.update()
            inc.update()

    def draw(self, config: GameConfig) -> None:
        self.draw_background()
        self.draw_text(config)
        for dec, inc in self._buttons:
            dec.draw()
            inc.draw()