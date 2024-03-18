import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")
df_comuni = pd.read_csv("comuni_clean.csv", sep=";")

tot_decessi = df_regioni.groupby("RegionName")["Daily_Deaths"].sum().sum()
print(tot_decessi)

tot_popolazione = df_comuni.groupby("Regione")["Popolazione2011"].sum().sum()
rapporto = (tot_decessi / tot_popolazione) *100
print(rapporto)

# Calcolo il numero di decessi per regione
tot_decessi_per_regione = df_regioni.groupby("RegionName")["Daily_Deaths"].sum()
popolazione_per_regione = df_comuni.groupby("Regione")["Popolazione2011"].sum()
mortalita_per_regione = (tot_decessi_per_regione / popolazione_per_regione * 100).sort_values(ascending=False)

# Creo il grafico
plt.figure(figsize=(12, 6))
sns.barplot(x=mortalita_per_regione.index.str[:7], y=mortalita_per_regione.values, color='b')
plt.xticks(rotation=90)
plt.xlabel('Regione')
plt.ylabel('Tasso di mortalità(%)')
plt.title('Tasso di mortalità per regione')
plt.savefig('tasso_mortalità_per_morti_giornaliere.png', dpi=200)
plt.show()