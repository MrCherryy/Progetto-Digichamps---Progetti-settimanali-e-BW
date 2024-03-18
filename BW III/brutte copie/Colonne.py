import csv

# Apre il file CSV in modalità lettura
with open('Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency_7212563912390016675 (1).csv', 'r') as file:
    reader = csv.reader(file)
    
    # Legge la prima riga del file CSV che contiene i nomi delle colonne
    columns = next(reader)
    
    # Stampare i nomi delle colonne
    for column in columns:
        print(column)