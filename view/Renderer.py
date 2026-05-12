# pyright: strict

from abc import ABC, abstractmethod
from model.Model import Model

class Renderer(ABC):
    @abstractmethod
    def draw(self, model: Model):
        ...