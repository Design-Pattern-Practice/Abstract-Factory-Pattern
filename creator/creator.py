from abc import ABC, abstractmethod


class Creator(ABC):
    
    @abstractmethod
    def createProduct(self,data):
        pass