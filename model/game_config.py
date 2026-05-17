# pyright: strict

import json

class GameConfig:
    def __init__(self):
        # default settings; width and height is for the grid itself (not the entire game screen)
        self.__enemies = 5
        self.__lives = 2
        self.__rows = 2
        self.__cols = 10
        self.__width = 1280
        self.__height = 720

    @property
    def enemies(self) -> int:
        return self.__enemies

    @property
    def lives(self) -> int:
        return self.__lives

    @property
    def rows(self) -> int:
        return self.__rows
    
    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def height(self) -> int:
        return self.__height

    def fetch_config(self, file: str):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                self.__enemies = data["enemies"]
                self.__lives = data["lives"]
                self.__rows = data["rows"]
                self.__cols = data["cols"]
                self.__width = data["width"]
                self.__height = data["height"]
        except FileNotFoundError:
            print(f"Config file {file} not found!")