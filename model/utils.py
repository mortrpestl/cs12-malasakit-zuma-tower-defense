# pyright: strict

from enum import Enum, auto
from dataclasses import dataclass
from random import Random

RNG = Random(12)

class Color(Enum):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()

from enum import IntEnum

class BGColor(IntEnum):
    BLACK       = 0
    NAVY        = 1
    PURPLE      = 2
    GREEN       = 3
    BROWN       = 4
    DARK_GRAY   = 5
    LIGHT_GRAY  = 6
    WHITE       = 7
    RED         = 8
    ORANGE      = 9
    YELLOW      = 10
    LIME        = 11
    CYAN        = 12
    STEEL_BLUE  = 13
    PINK        = 14
    PEACH       = 15
    
class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class GameMode(Enum):
    CAMPAIGN = "campaign"
    ENDLESS = "endless"

class EnemyType(Enum):
    NORMAL = auto()
    CHAMELEON = auto()
    REGENERATOR = auto()

@dataclass
class LeaderboardEntry:
    name: str
    score: int
    mode: GameMode

@dataclass
class Settings:
    enemies_count: int
    player_lives: int

@dataclass
class WaveConfig:
    colors: list[Color]
    paths: list[int]
    special_types: list[EnemyType]

def get_next_color() -> Color:
    return RNG.choice(list(Color))