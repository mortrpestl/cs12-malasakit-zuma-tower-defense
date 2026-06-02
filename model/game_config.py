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
        self.__paths_count = 2
        
        self.__regen_hp = 1 # TODO: maybe GameConfig should take in an "h" parameter? right now the default is 1
        self.__chameleon_freq = 3 # TODO: maybe GameConfig should take in an "f" parameter? right now the default is 3

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

    @property
    def paths_count(self) -> int:
        return self.__paths_count
    
    @property
    def regen_hp(self) -> int:
        return self.__regen_hp

    @property
    def chameleon_freq(self) -> int:
        return self.__chameleon_freq

    def fetch_config(self, file: str) -> None:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                self.__enemies = data["enemies"]
                self.__lives = data["lives"]
                self.__rows = data["rows"]
                self.__cols = data["cols"]
                self.__width = data["width"]
                self.__height = data["height"]
                self.__paths_count = data["paths_count"]
        except FileNotFoundError:
            print(f"Config file {file} not found!")

    # added May 30, 2026 by Diogn
    
    def increment_enemies(self) -> None:
        if self.__enemies < 10:
            self.__enemies += 1

    def decrement_enemies(self) -> None:
        if self.__enemies > 1:
            self.__enemies -= 1

    def increment_lives(self) -> None:
        if self.__lives < 10:
            self.__lives += 1

    def decrement_lives(self) -> None:
        if self.__lives > 1:
            self.__lives -= 1

    def increment_regen_hp(self) -> None:
        if self.__regen_hp < 10:
            self.__regen_hp += 1

    def decrement_regen_hp(self) -> None:
        if self.__regen_hp > 1:
            self.__regen_hp -= 1

    def increment_chameleon_freq(self) -> None:
        if self.__chameleon_freq < 10:
            self.__chameleon_freq += 1

    def decrement_chameleon_freq(self) -> None:
        if self.__chameleon_freq > 1:
            self.__chameleon_freq -= 1