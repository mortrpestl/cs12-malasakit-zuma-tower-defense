# pyright: strict

from dataclasses import dataclass

from model.utils import Screen


@dataclass
class ScreenManager:
    _screen: Screen
    _previous_screen: Screen | None = None
    
    @property
    def screen(self) -> Screen:
        return self._screen
    
    @property
    def previous_screen(self) -> Screen | None:
        return self._previous_screen
    
    @screen.setter
    def screen(self, s : Screen) -> None:
        if s is not self._screen:
            self._previous_screen = self._screen
            self._screen = s
        else:
            raise ValueError("self pointing")