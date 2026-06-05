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
from pathlib import Path as FilePath
import json

class Model:
    def __init__(self, config: GameConfig, mode: GameMode):
        self.__player = Player(config)
        self.__stage = Stage(config)
        self.__enemies = config.enemies
        self.__current_round = 0
        self.__exp = 0
        self.__mode = mode
        self.__rng = Random(12) # fixed seed
        self.__config = config
        self.__towers: list[Tower] = [NormalTower()]
        self.__bought_towers: list[Tower] = []
        self.__bullets: list[Bullet] = []
        self.__stage.grid.grid[config.rows >> 1][config.cols >> 1].entity = self.__player.shooter

        self.__rounds: list[Round] = [] 

        if GameMode.ENDLESS:
            self.create_endless_round()

    @property
    def mode(self) -> GameMode:
        return self.__mode
    
    @mode.setter
    def mode(self, new_mode: GameMode) -> None:
        self.__mode = new_mode
    
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
    def bullets(self) -> list[Bullet]:
        return self.__bullets
    
    @bullets.setter
    def bullets(self, lst: list[Bullet]):
        self.__bullets = lst
    
    def switch_mode(self):
        self.__rounds = []
        self.__current_round = 0

        if self.__mode is GameMode.ENDLESS:
            self.__mode = GameMode.CAMPAIGN # Must load_campaign still
        else:
            self.__mode = GameMode.ENDLESS 
            self.create_endless_round()
      
    def load_campaign(self, file: str):
        if self.__mode is GameMode.ENDLESS:
            return None
        
        path = FilePath(__file__).parent / "rounds" / file

        with open(path, "r") as d:
            data = json.load(d)
            
            for round in range(12):
                path_list: list[int] = []
                enemy_list: list[EnemyType]= []

                for n, path in enumerate(data["waves"][round]):
                    for enemy in path:
                        path_list.append(n)
                        enemy_list.append(EnemyType(enemy))

                config = WaveConfig(
                    self.rng.choices(list(Color), k=len(enemy_list)),
                    path_list,
                    enemy_list
                )

                self.__rounds.append(Round(config, self.__stage.paths))
    
    def create_endless_round(self):
        print("SHELDON COOPER YOU DOG")

        if self.__mode is GameMode.CAMPAIGN:
            return None
        
        cham_ratio = min(
            self.config.endless_cham_ratio, 
            (self.current_round/ 40) * self.config.endless_cham_ratio
            )
        
        regen_ratio = min(
            self.config.endless_cham_ratio, 
            (self.current_round/ 40) * self.config.endless_cham_ratio
            )
        
        normal_ratio = 1 - (cham_ratio + regen_ratio)
        count = (self.current_round + 1) * 3 
        enemy_list = [EnemyType(i) for i in self.rng.choices([1, 2, 3], weights= [normal_ratio, cham_ratio, regen_ratio], k=count)]

        config = WaveConfig(
            self.rng.choices(list(Color), k = count),
            self.rng.choices([0, 1], k = count), 
            enemy_list
        ) 

        self.__rounds.append(Round(config, self.__stage.paths))

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
        
    # gives (y, x) of top left corner of (i, j)
    def get_position(self, i: int, j: int) -> tuple[float, float]:
        cell_width = self.config.width / self.config.cols
        cell_height = self.config.height / self.config.rows
        return i * cell_height, j * cell_width