import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

# Calcolo i totali positivi per regione
totali_positivi_regione = df_regioni.groupby("RegionName")["NewPositiveCases"].sum()
tot_pos_sorted = totali_positivi_regione.sort_values(ascending=False)

# Calcolo i totali guariti per regione
totali_recovered_regione = df_regioni.groupby("RegionName")["TotalHospitalizedPatients"].sum()
tot_rec_sorted = totali_recovered_regione.sort_values(ascending=False)

# Calcolo i decessi per regione
totali_death_regione = df_regioni.groupby('RegionName')['Daily_Deaths'].sum()
tot_death_sorted = totali_death_regione.sort_values(ascending=False)


plt.figure (figsize=(12, 6))
sns.barplot (x = tot_pos_sorted.index, y = tot_pos_sorted.values, palette="plasma")
plt.xticks (rotation = 30)
plt.xlabel("Regione")
plt.ylabel("Totale positivi")
plt.title ("Totale positivi per regione")
plt.show()

plt.figure (figsize=(12,6))
sns.barplot (x = tot_rec_sorted.index, y = tot_rec_sorted.values, palette = "plasma")
plt.xticks (rotation = 30)
plt.xlabel("Regione")
plt.ylabel("Totale pazienti ospedalizzati")
plt.title ("Totale pazienti ospedalizzati per regione")
plt.show()

plt.figure (figsize=(12,6))
sns.barplot (x = tot_death_sorted.index, y = tot_death_sorted.values, palette = "plasma")
plt.xticks (rotation = 30)
plt.xlabel("Regione")
plt.ylabel("Decessi")
plt.title ("Decessi per regione")
plt.show()