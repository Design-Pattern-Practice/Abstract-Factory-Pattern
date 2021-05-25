from .productA import ProductA

class ConcreteProductA(ProductA):

    def __init__(self,data):
        self.data = data 

    def show(self):
        print("Family 2 : Product A response raised to power:",self.data*self.data)
        print("Data Supplied : ",self.data)