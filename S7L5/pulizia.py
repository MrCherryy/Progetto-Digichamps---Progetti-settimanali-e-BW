import pandas as pd

# Carico il dataset
df = pd.read_csv("dataset_climatico.csv")

# Rimuovo le righe con valori mancanti
df.dropna(inplace=True)

# Rimuovo righe con valori errati (se applicabile)
df = df[(df["temperatura_media"] >= -100) & (df["temperatura_media"] <= 100)]

# Applico la normalizzazione Z-score alle colonne desiderate
normalizzazione_colonne = ["temperatura_media", "precipitazioni", "umidita", "velocita_vento"]
df[normalizzazione_colonne] = (df[normalizzazione_colonne] - df[normalizzazione_colonne].mean()) / df[normalizzazione_colonne].std()

# Visualizzo il dataframe pulito
print(df.head())
df.to_csv("dataset_pulito.csv", index=False)