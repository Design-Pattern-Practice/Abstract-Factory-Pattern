from .productA import ProductA

class ConcreteProductA(ProductA):

    def __init__(self,data):
        self.data = data 

    def show(self):
        print("Family 1 : Product A response squared:",self.data*self.data)