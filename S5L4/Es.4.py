class ContoBancario:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def prelevare(self, importo):
        if importo <= self.saldo:
            self.saldo -= importo
        else:
            print("Sei senza soldi, pezzente!")
    
    def depositare (self, importo):
        self.saldo += importo

TestConto = ContoBancario(50)
print ("Saldo di partenza:", TestConto.saldo)

TestConto.prelevare(1000)
print("Saldo dopo il prelievo:", TestConto.saldo)

TestConto.depositare(1500)
print("Il saldo dopo il prelievo è:", TestConto.saldo)

TestConto.prelevare(100)
print("Saldo dopo il prelievo:", TestConto.saldo)