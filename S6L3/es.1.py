import pandas as pd
import numpy as np

df = pd.read_csv("wine.csv")

# Escludi la colonna "wine_color" dal DataFrame
df_numerical = df.select_dtypes(include=np.number)

# Calcola le informazioni statistiche base sulle colonne numeriche
count = df_numerical.count()
mode = df_numerical.mode().iloc[0]
median = df_numerical.median()
quartile_1 = df_numerical.quantile(0.25)
quartile_3 = df_numerical.quantile(0.75)
mean = df_numerical.mean()
variance = df_numerical.var()
std_deviation = df_numerical.std()
min_value = df_numerical.min()
max_value = df_numerical.max()
summary_statistics = df_numerical.describe()

# Stampa le informazioni statistiche base
print("Numerosità:\n", count)
print("\nModa:\n", mode)
print("\nMediana:\n", median)
print("\nQuartile 1:\n", quartile_1)
print("\nQuartile 3:\n", quartile_3)
print("\nMedia:\n", mean)
print("\nVarianza:\n", variance)
print("\nDeviazione standard:\n", std_deviation)
print("\nValore minimo:\n", min_value)
print("\nValore massimo:\n", max_value)
print("\nRiepilogo statistico:\n", summary_statistics)