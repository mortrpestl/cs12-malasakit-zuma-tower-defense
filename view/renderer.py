# pyright: strict

from abc import ABC, abstractmethod
from model.model import Model

class Renderer(ABC):
    def __init__(self, model : Model):
        self._model : Model = model
        
    @property 
    def model(self) -> Model:
        return self._model
        
    @abstractmethod
    def draw(self):
        ...
        
    @abstractmethod
    def update(self):
        ...