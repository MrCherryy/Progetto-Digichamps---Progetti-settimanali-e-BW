class Prodotto:
    def __init__(self, nome, prezzo, quantità_disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.quantità_disponibile = quantità_disponibile
    
    def calcolo_costo_totale(self):
        return self.prezzo * self.quantità_disponibile

    def verifica_disponibilità(self):
        if self.quantità_disponibile > 0:
            return "Ci sono prodotti disponibili"
        else:
            return "Non ne abbiamo più, mi dispiace"

testProdotto1 = Prodotto("Bibbia d'oro", 2300, 0)

costo_totale = testProdotto1.calcolo_costo_totale()
print("Il costo totale è di:", costo_totale)

disponibilità = testProdotto1.verifica_disponibilità()
print (disponibilità)
