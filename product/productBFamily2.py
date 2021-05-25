from .productB import ProductB
import math

class ConcreteProductB(ProductB):

    def __init__(self,data,factor):
        self.data = data
        self.factor = factor

    def show(self):
        print("Family 2 : Product B response raised to power:",math.pow(self.data,self.factor))
        print("Data Supplied : ",self.data,self.factor)