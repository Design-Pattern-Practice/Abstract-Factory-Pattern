from .creator import Creator
from product.productAFamily2 import ConcreteProductA
from product.productBFamily2 import ConcreteProductB

class ConCreatorFamily2(Creator):

    def createProduct(self,data,factor):
        return ConcreteProductA(data),ConcreteProductB(data,factor)