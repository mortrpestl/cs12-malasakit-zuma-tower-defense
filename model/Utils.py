# pyright: strict

from enum import Enum, auto
from dataclasses import dataclass

class Color(Enum):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = auto()

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class GameMode(Enum):
    CAMPAIGN = "campaign"
    ENDLESS = "endless"

@dataclass
class LeaderboardEntry:
    name: str
    score: int
    mode: GameMode

@dataclass
class Settings:
    enemies_count: int
    player_lives: int