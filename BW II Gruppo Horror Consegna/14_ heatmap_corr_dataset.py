import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

# Analizzo la presenza di eventuali correlazioni all'interno del dataset
# Nello specifico mi aspetto di trovare una correlazione positiva 
# tra i pazienti covid ospedalizzati e i decessi

# Prima mi seleziono solo le colonne di interesse
df_regioni = df_regioni.iloc[:,[3, 4, 5, 12]]
df_regioni.columns = ['Ricoveri',
                      'Intensiva',
                      'TotRicoveri',
                      'Decessi']

# Eseguo correlazioni sulle varibiali di interesse
corr= df_regioni.corr()

# Poi costruisco la heatmap delle correlazione
# per vedere subito la presenza di eventuali correlazione da approfondire

plt.figure(figsize=(18, 10))
plt.subplot(121)
sns.heatmap(corr, cmap='magma', annot=True)
plt.xticks(rotation = 90) 
plt.title('Correlazione tra Variabili del dataset regioni')
#plt.savefig("Correlazione.png", dpi=300)
# plt.show()

plt.subplot(122)
sns.scatterplot(x=df_regioni.iloc[:,1], y= df_regioni['Decessi'], data=df_regioni, hue='Intensiva', s=100)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()