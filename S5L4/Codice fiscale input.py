class CodiceFiscale:
    def __init__(self, nome, cognome, data_nascita, sesso, comune):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.sesso = sesso
        self.comune = comune

    def calcola_codice(self):
        # Implementazione dell'algoritmo per calcolare il codice fiscale

        # Conversione del nome e cognome in maiuscolo
        nome_cognome = (self.nome + self.cognome).upper()

        # Calcolo delle prime tre consonanti del cognome
        consonanti_cognome = ""
        for lettera in self.cognome:
            if lettera not in "AEIOU":
                consonanti_cognome += lettera
            if len(consonanti_cognome) == 3:
                break

        # Calcolo delle tre consonanti del nome
        consonanti_nome = ""
        vocali_nome = ""
        for lettera in self.nome:
            if lettera in "AEIOU":
                vocali_nome += lettera
            else:
                consonanti_nome += lettera
            if len(consonanti_nome) == 3:
                break

        # Calcolo degli ultimi due numeri dell'anno di nascita
        anno_nascita = self.data_nascita[-2:]

        # Conversione del mese di nascita in valore numerico
        mesi = {"01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H",
                 "07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T"}
        mese_nascita = mesi[self.data_nascita[3:5]]

        # Calcolo del giorno di nascita e del carattere di controllo
        giorno_nascita = str(int(self.data_nascita[:2]) + (40 if self.sesso == 'F' else 0))
        carattere_controllo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[sum(ord(c) - ord('A') for c in nome_cognome) % 26]

        # Creazione del codice fiscale
        codice_fiscale = consonanti_cognome + consonanti_nome + anno_nascita + mese_nascita + giorno_nascita + self.comune + carattere_controllo

        return codice_fiscale


# Esempio di utilizzo
nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
data_nascita = input("Inserisci la data di nascita (DD/MM/YYYY): ")
sesso = input("Inserisci il sesso (M/F): ")
comune = input("Inserisci il comune di nascita: ")

cf = CodiceFiscale(nome, cognome, data_nascita, sesso, comune)
codice = cf.calcola_codice()
print("Il codice fiscale è:", codice)