class CalcolaCodiceFiscale:
    def __init__(self, nome, cognome, data_di_nascita, sesso, comune_di_nascita):
        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.sesso = sesso
        self.comune_di_nascita = comune_di_nascita
    
    def calcola_codice_fiscale(self):
        vocali = ['A', 'E', 'I', 'O', 'U']
        
        nome = self.nome.upper().replace(' ', '')
        cognome = self.cognome.upper().replace(' ', '')

        codice_cognome = cognome[:3]

        consonanti_cognome = [lettera for lettera in codice_cognome if lettera not in vocali]

        if len(consonanti_cognome) < 3:
            consonanti_cognome.append('X')

        anno = self.data_di_nascita[-2:]
        mese = self.data_di_nascita[3:5]
        giorno = self.data_di_nascita[:2]

        mesi = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'T']
        codice_mese = mesi[int(mese) - 1]

        if self.sesso == 'F':
            giorno = str(int(giorno) + 40)

        codice_sesso = self.sesso
        codice_data_di_nascita = anno + codice_mese + giorno

        codice_comune = self.comune_di_nascita.upper()

        cifra_di_controllo = 0

        codice_fiscale_intero = (
            codice_cognome +
            consonanti_cognome[0] +
            codice_data_di_nascita +
            codice_comune
        )

        for i, char in enumerate(codice_fiscale_intero):
            if i % 2 == 0:
                cifra_di_controllo += ord(char) - ord('0')
            else:
                cifra_di_controllo += sum(divmod((ord(char) - ord('0')) * 2, 10))

        cifra_di_controllo = chr((10 - (cifra_di_controllo % 10)) % 10 + ord('0'))

        codice_fiscale = codice_cognome + consonanti_cognome[0] + codice_data_di_nascita + codice_comune + cifra_di_controllo

        return codice_fiscale

# Esempio di utilizzo
persona = CalcolaCodiceFiscale("Mario", "Rossi", "01/01/1990", "M", "Roma")
codice_fiscale = persona.calcola_codice_fiscale()
print(codice_fiscale)