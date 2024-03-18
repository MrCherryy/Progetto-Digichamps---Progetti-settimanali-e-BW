import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")
df_comuni = pd.read_csv("comuni_clean.csv", sep=";")

# Calcolo il tasso di mortalità, di contagi e di ospedalizzazione
# Per calcolare i rapporti, prima
# calcolo la popolazione totale

tot_popolazione = df_comuni["Popolazione2011"].sum()
print("La popolazione totale del 2011 è di:", tot_popolazione)

# tot deceduti
deceduti = df_regioni["Daily_Deaths"].sum()

# tot newpositive
guariti = df_regioni["NewPositiveCases"].sum()

# tot ospedalizzati
hosp = df_regioni["TotalHospitalizedPatients"].sum()

# tasso di mortalità
death_prop = (deceduti/tot_popolazione) * 100
print("Il tasso di mortalità in Italia è di:", death_prop)

# tasso di contagio
positive_prop = (guariti/tot_popolazione) * 100
print("Il tasso di contagio è di:", positive_prop)

# tasso di ospedalizzazione
hosp_prop = (hosp/tot_popolazione) * 100 
print("Il tasso di ospedalizzazione è di:", hosp_prop)