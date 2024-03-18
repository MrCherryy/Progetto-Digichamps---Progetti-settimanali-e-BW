class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età
    def stampa_informazioni(self):
        print ("Nome:", self.nome)
        print ("Cognome", self.cognome)
        print ("Età", self.età)

# Provo la classe Persona
        
test1 = Persona ("Marco", "Cerri", 35)
test1.stampa_informazioni()