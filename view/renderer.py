# pyright: strict

from abc import ABC, abstractmethod
from model.model import Model
from view.screen_manager import ScreenManager

class Renderer(ABC):
    def __init__(self, model : Model, screen_manager : ScreenManager):
        self._model : Model = model
        self.__screen_manager = screen_manager
        
    @property 
    def model(self) -> Model:
        return self._model
    
    @property
    def screen_manager(self) -> ScreenManager:
        return self.__screen_manager
        
    @abstractmethod
    def draw(self):
        ...
        
    @abstractmethod
    def update(self):
        ...