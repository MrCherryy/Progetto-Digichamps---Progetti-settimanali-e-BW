import math as matematica

class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
    
    def calcolo_area(self):
        return matematica.pi * self.raggio**2

    def calcolo_circonferenza(self):
        return 2 * matematica.pi * self.raggio

testCerchio = Cerchio(3)
print("Area del cerchio:", testCerchio.calcolo_area())
print("Circonferenza del cerchio:", testCerchio.calcolo_circonferenza())
