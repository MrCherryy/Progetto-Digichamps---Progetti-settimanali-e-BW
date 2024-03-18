import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")


# I dati "TotalPositiveCases" rappresentano la somma dei valori di 3 varibili:
# 1. CurrentPositive Cases = i positivi al momento
# 2. Recovered = guariti
# 3. Deaths = decessi
# Per ogni regione, si esplora l'incidenza delle singole varibili sui dati totali

# 1. Raggruppo per regione i casi positivi totali

tot_positive = df_regioni.groupby(["RegionName"])["TotalPositiveCases"].sum()

# 2. Raggruppo per regione i dati delle tre variabili
tot_current_positive = df_regioni.groupby(["RegionName"])["CurrentPositiveCases"].sum()
tot_recovered = df_regioni.groupby(["RegionName"])["Recovered"].sum()
tot_deaths = df_regioni.groupby(["RegionName"])["Deaths"].sum()

# 3. Trovo la proporzione delle 3 variabili sul totale
prop_current = tot_current_positive / tot_positive
prop_recovered = tot_recovered / tot_positive
prop_death = tot_deaths / tot_positive

# 4. Costruiscono un grafico a barre per rappresentare i risultati

pos = np.arange (len(tot_positive))
regions = tot_positive.index

fig, ax = plt.subplots(figsize=(12, 6))
current_positive = ax.barh(pos, prop_current, color = "#f77f00", label = "Positivi")
positive = ax.barh(pos, prop_recovered, color = "#39A9DB", label = "Guariti")
deaths = ax.barh(pos, prop_death, color = "#d62828", label = "Decessi")

ax.set_yticks(pos) 
ax.set_yticklabels(regions) 
ax.invert_yaxis() 
ax.set_xlabel('Proporzione') 
ax.set_title('Proporzione dei Positivi, Guariti e Decessi per Regione sul totale dei casi positivi') 
ax.legend() 
plt.show()

