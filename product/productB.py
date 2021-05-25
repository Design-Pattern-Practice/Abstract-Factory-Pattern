from abc import ABC, abstractmethod

class ProductB(ABC):
    
    @abstractmethod
    def show(self,data,factor):
        pass