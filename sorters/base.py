from abc import ABC, abstractmethod
class BaseSorter(ABC):
    def __init__(self,name: str):
        self.name = name
        self.comparisons = 0
        self.swaps = 0
    def resetmetrics(self):
        self.comparisons = 0
        self.swaps = 0
    @abstractmethod
    def sort(self,array: list) -> list:
        pass