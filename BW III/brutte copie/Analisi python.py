import pandas as pd

# Carica il dataset in un DataFrame
df = pd.read_csv('nuovo climate disastri.csv')

# Unisce tutte le colonne di date in una unica colonna
df['Date_raggruppate'] = df['F1995'].astype(str) + '/' + df['F1996'].astype(str) + '/' + df['F1997'].astype(str)

# Salva il dataframe con la nuova colonna in un nuovo file CSV
df.to_csv('nuovo_file.csv', index=False)