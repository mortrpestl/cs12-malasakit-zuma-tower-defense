# pyright: strict

from dataclasses import dataclass

from model.utils import Screen


@dataclass
class ScreenManager:
    _screen: Screen
    
    @property
    def screen(self) -> Screen:
        return self._screen
    
    @screen.setter
    def screen(self, s : Screen) -> None:
        if s is not self._screen:
            self._screen = s
        else:
            raise ValueError("self pointing")