class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def stampa(self):
        print("Nome:", self.nome)
        print("Cognome:", self.cognome)
        print("Età:", self.età)

test1 = Persona("Mario", "Rossi", 28)
test1.stampa()