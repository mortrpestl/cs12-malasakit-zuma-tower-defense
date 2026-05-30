# pyright: strict
from model.player import Player
from model.stage import Stage
from model.round import Round
from model.utils import *
from model.game_config import GameConfig
from random import Random

class PendingAction(Enum):
    NONE             = "none"
    QUIT_GAME        = "quit_game"
    VIEW_LEADERBOARD = "view_leaderboard"
    VIEW_MENU        = "view_menu"
    
class Model:
    def __init__(self, config: GameConfig, mode: GameMode):
        
                
        self.__player = Player(config)
        self.__stage = Stage(config)
        self.__enemies = config.enemies
        self.__current_round = 0
        self.__exp = 0
        self.__mode = mode
        self.__rng = Random(12) # fixed seed
        self.__rounds: list[Round] = [self.create_round() for _ in range(12)] # at least 12 rounds
        self.__pending_action : PendingAction = PendingAction.NONE
        
        self.__config = config # TODO! please check if the config here actually reflects on the Players, Stage, and Enemies


    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @property
    def player(self) -> GameConfig:
        return self.__config
    
    @property
    def config(self) -> GameConfig:
        return self.__config
    
    @property
    def current_round(self) -> int:
        return self.__current_round
    
    @property
    def rng(self) -> Random:
        return self.__rng

    @property
    def rounds(self) -> list[Round]:
        return self.__rounds

    def create_round(self) -> Round:
        config = WaveConfig(
            self.rng.choices(list(Color), k=self.__enemies),
            [self.rng.randint(0, len(self.__stage.paths) - 1) for _ in range(self.__enemies)],
            self.rng.choices(list(EnemyType), k=self.__enemies)
        )
        return Round(config, self.__stage.paths)
    
    # TODO update, is_game_over
    
    # inserted by Diogn on May 30, 2026
    
    def quit(self):
        ... 
        
    def open_leaderboard(self):
        ...
        
    def open_menu(self):
        ...
        
    # how this works -- if player presses some button in the main menu (like "Leaderboard"), that should change the pending action into the corresponding action (check Enum above).
    
    # in the update loop, when this is detected, there should be a mechanism that freezes the game and checks for confirmation if they'll actually proceed with that decision. 
    
    # if so, a window is opened (unless we're talking about "Quit Game", which closes the window of the game). if this newly opened window is closed, the game is unpaused again.
    
    # ONLY ONE OPENED WINDOW. SO IF THE CURRENT PENDING ACTION IS NOT FINISHED, NO NEW WINDOWS CAN OPEN
    
    @property
    def pending_action(self) -> PendingAction:
        return self.__pending_action

    def set_pending_action(self, action: PendingAction) -> None:
        if self.__pending_action is PendingAction.NONE:
            self.__pending_action = action

    def reset_pending_action(self) -> None:
        self.__pending_action = PendingAction.NONE

    def confirm(self, result: bool) -> None:
        if result:
            match self.__pending_action:
                case PendingAction.QUIT_GAME:
                    self.quit()
                case PendingAction.VIEW_LEADERBOARD:
                    self.open_leaderboard()
                case PendingAction.VIEW_MENU:
                    self.open_menu()
                case PendingAction.NONE:
                    ...
                    
        self.reset_pending_action()