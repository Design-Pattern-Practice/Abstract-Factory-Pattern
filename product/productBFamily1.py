from .productB import ProductB
import math

class ConcreteProductB(ProductB):

    def __init__(self,data,factor):
        self.data = data
        self.factor = factor

    def show(self):
        print("Family 1 : Product B response squared:",math.pow(self.data,self.factor))