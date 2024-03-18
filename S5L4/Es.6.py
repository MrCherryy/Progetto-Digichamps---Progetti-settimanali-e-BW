import csv

class AnalizzatoreCSV:
    def __init__(self, file_csv):
        self.file_csv = file_csv
    
    def analizza(self):
        with open(self.file_csv, 'r') as file:
            reader = csv.reader(file)
            dati = list(reader)
            
            # Calcola il numero totale di righe nel file
            numero_righe = len(dati)
            
            # Calcola il numero totale di colonne nel file
            numero_colonne = len(dati[0])
            
            # Calcola la somma dei valori in una colonna specifica
            somma_colonna = 0
            indice_colonna = 2  # Indice della colonna da considerare (inizia da 0)
            for riga in dati[1:]:  # Ignora l'intestazione
                valore = float(riga[indice_colonna])
                somma_colonna += valore
            
            # Restituisci i risultati
            risultati = {
                "Numero righe": numero_righe,
                "Numero colonne": numero_colonne,
                "Somma colonna {}: {}".format(indice_colonna, somma_colonna):
                        }
            return risultati

# Utilizzo della classe
analizzatore = AnalizzatoreCSV("file.csv")
risultati = analizzatore.analizza()
for chiave, valore in risultati.items():
    print(chiave + ": " + str(valore))