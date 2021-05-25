from .creator import Creator
from product.productAFamily1 import ConcreteProductA
from product.productBFamily1 import ConcreteProductB

class ConCreatorFamily1(Creator):

    def createProduct(self,data,factor):
        return ConcreteProductA(data),ConcreteProductB(data,factor);