# pyright: strict
from model.player import Player
from model.stage import Stage
from model.round import Round
from model.utils import Color, EnemyType, GameMode, WaveConfig
from model.game_config import GameConfig
from model.entities.tower import Tower
from model.entities.bullet import Bullet
from random import Random
from model.entities.normaltower import NormalTower
from model.leaderboard import Leaderboard

CAMPAIGN_SEED = sum(ord(_) for _ in "May 05 1948")

class Model:
    def __init__(self, config: GameConfig, mode: GameMode, campaign_file: str = ""):
        self.__original_campaign = campaign_file # rounds 
        self.__config = config
        self.__mode = mode
        self.__enemies = config.enemies
        self.__leaderboards = {mode: Leaderboard(mode) for mode in list(GameMode)}
        self.__leaderboard = self.__leaderboards[mode]
        self.__leaderboard.read_file("")

        self.__campaign_stages = [Stage(self.__config, f"campaign_map_{i}.json") for i in range(1, 13)]
        self.__endless_stage = Stage(self.__config, f"campaign_map_10.json")
        
        self.restart_game()

    def restart_game(self):
        self.__player = Player(self.__config)
        self.__stage = self.__campaign_stages[0] if self.__mode == GameMode.CAMPAIGN else self.__endless_stage
        self.__current_round = 0
        self.__exp = 0
        self.__towers: list[Tower] = [NormalTower(self.__config)]
        self.__bought_towers: list[Tower] = []
        self.__bullets: list[Bullet] = []
        self.__rounds: list[Round] = []
        self.__stage.grid.grid[self.__config.rows >> 1][self.__config.cols >> 1].entity = self.__player.shooter

        if self.__mode == GameMode.ENDLESS:
            self.__rng = Random()
            self.create_endless_round()
            
        else:
            self.__rng = Random(CAMPAIGN_SEED)
            self.create_campaign_rounds()

    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @property
    def exp(self) -> int:
        return self.__exp
    
    @exp.setter
    def exp(self, new_exp: int):
        self.__exp = max(0, new_exp)
    
    @property
    def player(self) -> Player:
        return self.__player
    
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
    
    @property
    def stage(self) -> Stage:
        return self.__stage

    @property
    def enemy_count(self) -> int:
        return self.__enemies
    
    @property
    def towers(self) -> list[Tower]:
        return self.__towers
    
    @property
    def bought_towers(self) -> list[Tower]:
        return self.__bought_towers
    
    @property
    def leaderboard(self) -> Leaderboard:
        return self.__leaderboard
    
    @property
    def leaderboards(self) -> dict[GameMode, Leaderboard]:
        return self.__leaderboards

    @property
    def bullets(self) -> list[Bullet]:
        return self.__bullets

    @bullets.setter
    def bullets(self, lst: list[Bullet]):
        self.__bullets = lst
    
    def switch_mode(self, enemy_file: str = "campaign_round_1.json"):
        self.__rounds = []
        self.__current_round = 0

        if self.__mode is GameMode.ENDLESS:
            self.__mode = GameMode.CAMPAIGN # Must load_campaign still
            self.create_campaign_rounds()
        else:
            self.__mode = GameMode.ENDLESS 
            self.create_endless_round()

        self.restart_game()
        self.__leaderboard = self.__leaderboards[self.__mode]
    
    def create_campaign_rounds(self):
        if self.__mode is GameMode.ENDLESS:
            return None
        
        for rnd in range(12):
            cham_ratio = min(
                self.config.endless_cham_ratio, 
                (rnd / 12) * self.config.endless_cham_ratio
                )
            
            regen_ratio = min(
                self.config.endless_cham_ratio, 
                (rnd / 12) * self.config.endless_cham_ratio
                )
            
            normal_ratio = 1 - (cham_ratio + regen_ratio)
            count = min(self.__config.enemies, (self.current_round + 1) * 3)
            enemy_list = [EnemyType(i) for i in self.rng.choices([1, 2, 3], weights= [normal_ratio, cham_ratio, regen_ratio], k=count)]

            config = WaveConfig(
                self.rng.choices(list(Color), k = count),
                self.rng.choices(range(self.__stage.path_count), k = count), 
                enemy_list
            ) 

            self.__rounds.append(Round(config, self.__stage.paths, self.__config))


    def create_endless_round(self):
        if self.__mode is GameMode.CAMPAIGN:
            return None
        
        cham_ratio = min(
            self.config.endless_cham_ratio, 
            (self.current_round / 40) * self.config.endless_cham_ratio
            )
        
        regen_ratio = min(
            self.config.endless_cham_ratio, 
            (self.current_round / 40) * self.config.endless_cham_ratio
            )
        
        normal_ratio = 1 - (cham_ratio + regen_ratio)
        count = min(self.__config.enemies, (self.current_round + 1) * 3)
        enemy_list = [EnemyType(i) for i in self.rng.choices([1, 2, 3], weights= [normal_ratio, cham_ratio, regen_ratio], k=count)]

        config = WaveConfig(
            self.rng.choices(list(Color), k = count),
            self.rng.choices(range(self.__stage.path_count), k = count), 
            enemy_list
        ) 

        self.__rounds.append(Round(config, self.__stage.paths, self.__config))

    @property
    def is_game_over(self) -> bool:
        return self.__current_round >= len(self.__rounds) \
            or self.player.lives <= 0 if self.mode == GameMode.CAMPAIGN \
          else self.player.lives <= 0
    
    def add_exp(self, amount: int):
        self.__exp += amount

    def lose_life(self):
        self.__player.lose_life()
    
    def advance_next_round(self):
        self.__current_round += 1
        self.__bullets.clear()

        if self.mode is GameMode.CAMPAIGN:
            self.__stage = self.__campaign_stages[self.current_round]
        else:
            self.create_endless_round()
        
    # gives (y, x) of top left corner of (i, j)
    def get_position(self, i: int, j: int) -> tuple[float, float]:
        cell_width = self.config.width / self.config.cols
        cell_height = self.config.height / self.config.rows
        return i * cell_height, j * cell_width