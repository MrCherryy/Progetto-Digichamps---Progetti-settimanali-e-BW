import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 

df_province = pd.read_csv('covid19_province _python.csv', sep=";")
df_comuni = pd.read_csv('comuni_clean.csv', sep=";")

# trovo la popolazione per ogni provincia
tot_pop_provincia = df_comuni.groupby("Sigla automobilistica")["Popolazione2011"].sum()

# trovo il totale dei casi positivi in ogni provincia
# in questo caso, invece che sommare, è stato preso il valore massimo
# per via della struttura del dataset (essendo un valore cumulativo)
tot_positivi_provincia = df_province.groupby('ProvinceAbbreviation')['TotalPositiveCases'].max().sort_values(ascending=False)

# calcolo il rapporto con la popolazione
rapporto_pop = tot_positivi_provincia/tot_pop_provincia * 100
rapporto_pop_sorted = rapporto_pop.sort_values(ascending=False)
print(rapporto_pop_sorted.head(26))