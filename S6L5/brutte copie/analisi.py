import pandas as pd

# Carico il dataset
data = pd.read_csv('insurance.csv')

# Rimuovo le righe con valori mancanti
data = data.dropna()

# Sostituisco i valori mancanti con un valore specifico
data = data.fillna(0)

# Rimuovo duplicati
data = data.drop_duplicates()

# Salvo il dataset pulito
data.to_csv('analisi_pulite.csv', index=False)

