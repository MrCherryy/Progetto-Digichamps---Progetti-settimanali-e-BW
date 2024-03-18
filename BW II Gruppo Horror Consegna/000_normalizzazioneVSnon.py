import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv('covid19_region_python_w_daily_deaths.csv')
df_comuni = pd.read_csv('comuni_clean.csv', sep=";")

#Calcola i totali positivi per regione
totali_positivi_regione = df_regioni.groupby("RegionName")["NewPositiveCases"].sum()
tot_pos_sorted = totali_positivi_regione.sort_values(ascending=False)
#print(tot_pos_sorted)

# Calcola i totali guariti per regione
totali_recovered_regione = df_regioni.groupby("RegionName")["TotalHospitalizedPatients"].sum()
tot_rec_sorted = totali_recovered_regione.sort_values(ascending=False)
#print(tot_rec_sorted)

# Calcolo i decessi per regione
totali_death_regione = df_regioni.groupby('RegionName')['Daily_Deaths'].sum()
tot_death_sorted = totali_death_regione.sort_values(ascending=False)
#print(tot_death_sorted)

# popolazione regionale
pop_regionale = df_comuni.groupby('Regione')['Popolazione2011'].sum()
#print("La popolazione regionale è", pop_regionale)

tasso_positivi = tot_pos_sorted/pop_regionale * 100
tasso_positivi_sorted = tasso_positivi.sort_values(ascending=False)
print(tasso_positivi_sorted)

tasso_ospedalizzati = tot_rec_sorted/pop_regionale * 100
tasso_ospedalizzati_sorted = tasso_ospedalizzati.sort_values(ascending=False)
print(tasso_ospedalizzati_sorted)


tasso_decessi = tot_death_sorted/pop_regionale * 100
tasso_decessi_sorted = tasso_decessi.sort_values(ascending=False)
print(tasso_decessi_sorted)

