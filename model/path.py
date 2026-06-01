# pyright: strict

from model.cell import Cell

class Path:
    def __init__(self, cells: list[Cell]):
        self.__cells = cells
        assert len(self.__cells) > 0 # non-empty
        self.__start = cells[0]
        self.__end = cells[-1]

    @property
    def cells(self) -> list[Cell]: 
        return self.__cells

    @property
    def start(self) -> Cell:
        return self.__start
    
    @property
    def end(self) -> Cell:
        return self.__end
    