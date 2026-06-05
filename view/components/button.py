from dataclasses import dataclass
from typing import TypeVar, Callable
from model.utils import BGColor, SpriteSet

import pyxel

T = TypeVar("T")
U = TypeVar("U")

class ButtonComponent:
    def __init__(
                self,
                assoc_func : Callable[[], U],
                pyxel_set: SpriteSet,
                x : int,
                y : int,
                w : int = 150,
                h : int = 75,
                button_col : int = BGColor.LIGHT_GRAY,
                text_col : int = BGColor.WHITE,
                text : str = "Button Text", 
                ):
        
        self.__pyxel_set = pyxel_set
        
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._button_col = button_col
        self._text_col = text_col
        self._text = text
        self._assoc_func = assoc_func # function triggered when clicked
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def w(self):
        return self._w
    @property
    def h(self):
        return self._h
    @property
    def button_col(self) -> int:
        return self._button_col
    @button_col.setter
    def button_col(self, col : int) -> None:
        if not (0 <= col <= 15):
            raise ValueError("Invalid input")
        else:
            self._button_col = col        
    
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) \
        and self._x <= pyxel.mouse_x <= self._x + self._w \
        and self._y <= pyxel.mouse_y <= self._y + self._h:
            self._assoc_func()
        
    def draw(self):
        mid : float = 0.5 * (self.__pyxel_set.w - self.__pyxel_set.scale * self.__pyxel_set.w)
        
        pyxel.blt(self._x - mid, self._y - mid, 
            self.__pyxel_set.img, 
            self.__pyxel_set.x, 
            self.__pyxel_set.y,
            self.__pyxel_set.w,
            self.__pyxel_set.h,
            self.__pyxel_set.bg,
            scale=self.__pyxel_set.scale)
        pyxel.rectb(self._x, self._y, self._w, self._h, self._button_col)
        pyxel.text(self._x + 20, self._y + 20, self._text, self._text_col)
        
