import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_comuni = pd.read_csv("comuni_clean.csv", sep=";")
#print(df_comuni.head())

df_province = pd.read_csv("covid19_province _python.csv",sep=";")
#print(df_province.head())

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")
#print(df_regioni.head())

df_rip_geo = pd.read_csv("Ripartizione-geografica _python.txt", delimiter="\t", encoding="latin-1")
#print(df_rip_geo)

print(df_regioni.describe())

# Calcolo la popolazione totale dal dataset comuni
tot_popolazione = df_comuni["Popolazione2011"].sum()
print("La popolazione totale del 2011 è di:", tot_popolazione, "abitanti")

# Calcolo il totale di tutte le colonne presenti nel dataset Regioni

# Totali dei pazienti ospedalizzati
tot_ospedalizzati = df_regioni["TotalHospitalizedPatients"].sum()
print("In totale, i pazienti ricoverati sono:", tot_ospedalizzati)

# Totali dei pazienti semplice ricovero
tot_ricovero = df_regioni["HospitalizedPatients"].sum()
print("Di cui semplici ricoveri sono:", tot_ricovero)

# Totali dei pazienti in cura intensiva
tot_intensive = df_regioni["IntensiveCarePatients"].sum()
print("E in cura intensiva sono:", tot_intensive)

# Totali dei decessi
tot_deaths = df_regioni["Daily_Deaths"].sum()
print("In totale, i decessi sono:", tot_deaths)

# Totali dei nuovi contagi
tot_contagi = df_regioni["NewPositiveCases"].sum()
print("In totale, i contagi sono:", tot_contagi)

# Totali dei contagi, comprensi di quarantena e ospedalizzazione
tot_current = df_regioni["CurrentPositiveCases"].sum()
print("In totale, i pazienti in quarantena e ricoverati sono:", tot_current)

# Totali di positivi in quarantena
tot_lockdown = df_regioni["HomeConfinement"].sum()
print("In totale, i pazienti in quarantena sono:", tot_lockdown)

# Totali di pazienti guariti
tot_guariti = df_regioni["Recovered"].sum()
print("In totale, i pazienti guariti sono:", tot_guariti)

# Totali di pazienti con tampone positivo
tot_positive = df_regioni["TotalPositiveCases"].sum()
print("In totale, i pazienti contagiati sono:", tot_positive)

# Calcolo il picco per regione 
# e trovo in quale data si è registrato

# Converto la colonna "Date" in formato datetime
df_regioni["Date"] = pd.to_datetime(df_regioni["Date"], dayfirst=False)

# Trovo il giorno in cui c'è il picco dei contagi

indice_max_positivi = df_regioni["NewPositiveCases"].idxmax()

data_massimo_positivi = df_regioni.loc[indice_max_positivi, "Date"]

print("La data con il numero massimo dei contagi è:", data_massimo_positivi)

# Trovo il giorni di picco per isolamento

indice_max_confinment = df_regioni["HomeConfinement"].idxmax()

data_massimo_confinment = df_regioni.loc[indice_max_confinment, "Date"]

print("La data con il numero massimo dei pazienti in isolamento è:", data_massimo_positivi)

# Trovo il giorno di piccolo delle ospedalizzazioni

indice_max_hosp = df_regioni["TotalHospitalizedPatients"].idxmax()

data_massimo_hosp = df_regioni.loc[indice_max_hosp, "Date"]

print("La data con il numero massimo di ospedalizzazioni è:", data_massimo_positivi)

# Trovo il giorno di piccolo dei decessi

indice_max_death = df_regioni["Daily_Deaths"].idxmax()

data_massimo_death = df_regioni.loc[indice_max_hosp, "Date"]

print("La data con il picco di decessi è:", data_massimo_death)

