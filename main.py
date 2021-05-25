from math import prod
from creator.conCreatorFamily1 import ConCreatorFamily1
from creator.conCreatorFamily2 import ConCreatorFamily2

a = ConCreatorFamily1()
b = ConCreatorFamily2()


prodA1,prodB1 = a.createProduct(5,6)
prodA2,prodB2 = b.createProduct(7,4)


prodA1.show()
prodB1.show()
prodA2.show()
prodB2.show()