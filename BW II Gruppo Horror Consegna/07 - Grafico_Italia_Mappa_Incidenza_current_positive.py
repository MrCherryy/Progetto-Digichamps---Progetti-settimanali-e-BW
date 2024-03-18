import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
import geopandas as gpd  #ricordarsi di fare pip install

# Carico il dataset Comuni
df_comuni = pd.read_csv("comuni_clean.csv", sep=";")

# Carico il dataset Regione
df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

# Carico i dati geografici delle regioni italiane da un file shapefile(!ricordati da allegare in caso sennò non visualizza)
italy_regions = gpd.read_file("ITA_adm1_modified.shp")

#---------Analisi Dell'incidenza dei Decessi sul totale della popolazione regionare
#Gruppo Regione
Popolazione_tot_regione = df_comuni.groupby("Regione")["Popolazione2011"].sum()
#print(Popolazione_tot_regione)

#Decessi per regione
current_positive_regione = df_regioni.groupby("RegionName")["CurrentPositiveCases"].sum()

#Faccio la proporzione
proporzione= (current_positive_regione/Popolazione_tot_regione)
print(proporzione)

# Unione tra i dati geografici e la "proporzione"
italy_regions = italy_regions.merge(proporzione.reset_index(), left_on='NAME_1', right_on='RegionName', how='left')

# Creazione del grafico a mappa dell'Italia su base regionale
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

#Colorazione in base ai dati
italy_regions.plot(column=0, cmap='GnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Personalizzazione
ax.set_title('Proporzione Nuovi Casi per Regione in Italia')
ax.set_axis_off()
leg = ax.get_legend()
    
#Mostra
plt.show()
