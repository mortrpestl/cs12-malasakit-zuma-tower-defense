# pyright: strict
from entities.entity import Entity

class Cell:
    def __init__(self, x: int, y: int, is_tunnel: bool = False):
        self.__y = y
        self.__x = x
        self.__is_tunnel = is_tunnel
        self.__entity: None | Entity = None
    
    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y
    
    @property
    def is_tunnel(self) -> bool:
        return self.__is_tunnel
    
    @property
    def entity(self) -> None | Entity:
        return self.__entity