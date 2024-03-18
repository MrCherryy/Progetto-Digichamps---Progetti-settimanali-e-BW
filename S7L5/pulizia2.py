from scipy import stats
import pandas as pd

df = pd.read_csv("dataset_climatico.csv")

df.dropna(inplace=True)

normalizzazione_colonne = ["temperatura_media", "precipitazioni", "umidita", "velocita_vento"]

df[normalizzazione_colonne] = stats.zscore(df[normalizzazione_colonne])
print(df.head())
df.to_csv("dataset_pulito.csv", index=False)