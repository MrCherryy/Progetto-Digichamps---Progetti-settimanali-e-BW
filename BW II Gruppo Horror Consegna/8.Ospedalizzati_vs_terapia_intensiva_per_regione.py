import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

df_regioni.describe()
print(df_regioni)

totali_ospedalizzati_regione = df_regioni.groupby(['RegionName'])['HospitalizedPatients'].sum() 
totali_terapia_intensiva_regione = df_regioni.groupby(['RegionName'])['IntensiveCarePatients'].sum() 
proporzioni_ospedalizzati_regione = totali_ospedalizzati_regione / totali_ospedalizzati_regione.sum()
proporzioni_terapia_intensiva_regione = totali_terapia_intensiva_regione / totali_ospedalizzati_regione.sum()

pos = np.arange(len(totali_ospedalizzati_regione)) 
regions = totali_ospedalizzati_regione.index

fig, ax = plt.subplots(figsize=(12, 6)) 
Ospedalizzati = ax.barh(pos, proporzioni_ospedalizzati_regione, color="#5302A3", label='Ospedalizzati', alpha=0.5) 
Pazienti_Terapia_Intensiva = ax.barh(pos, proporzioni_terapia_intensiva_regione, color='Blue', label='Terapia Intensiva', alpha=0.5) 
ax.set_yticks(pos) 
ax.set_yticklabels(regions) 
ax.invert_yaxis() 
ax.set_xlabel('Proporzione') 
ax.set_title('Distribuzione degli Ospedalizzati totali e in Terapia Intensiva per Regione') 
ax.legend() 
plt.savefig('8.Ospedalizzati vs pazienti in terapia intensiva per regione.png', dpi=200)
plt.show()