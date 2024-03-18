import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

df_air = pd.read_csv("https://github.com/andreapas79/COVID-19/raw/master/df_air.csv", index_col=0)

df_comuni = pd.read_csv("comuni_clean.csv", sep=";")


# sostituisco P.A. di Bolzano e P.A. Trento con Trentino Alto Adige
df_air['Regione'] = df_air.iloc[:,2].replace('P.A. Trento', 'Trentino Alto Adige')
df_air['Regione'] = df_air.iloc[:,2].replace('P.A. Bolzano', 'Trentino Alto Adige')

# faccio un df in cui ho la somma dei decessi per regione
tot_deaths = df_regioni.groupby('RegionName')['Daily_Deaths'].sum()
df_deaths = tot_deaths.to_frame().reset_index()

# faccio un dataframe sul totale della popolazione
tot_popolazione = df_comuni.groupby("Regione")["Popolazione2011"].sum()
df_pop = tot_popolazione.to_frame().reset_index()

# unisco i dati delle due tabelle
df_summary = df_deaths.merge(tot_popolazione, left_on='RegionName', right_on='Regione')

# aggiungo una colonna sul tasso di mortalita
df_summary['death%'] = (df_summary['Daily_Deaths']/df_summary['Popolazione2011'])*100
print(df_summary.head())


# costruisco un df sull'inquinamento dell'aria
df_air_med = df_air.groupby('Regione').agg({'max media annuale (mg/m3)': ['count', 'mean', 'median']}).reset_index()
df_air_med.columns = ['Regione', 'max', 'mean', 'median']
print(df_air_med)

df_summary = df_summary.sort_values(by='death%', ascending=False).merge(df_air_med, left_on='RegionName',right_on='Regione')


df_summary = df_summary.iloc[:,[0,1,2,3,7]]
df_summary.columns = ['Regione',
                        'deaths',
                        'popolazione2011',
                        'death%',
                        'air_poll_median']

heatmapshow = df_summary[['deaths',
                            'popolazione2011',
                            'death%',
                            'air_poll_median']].corr()
print(heatmapshow)

plt.figure(figsize=(18,10))
plt.subplot(122)
sns.scatterplot(x=df_summary.iloc[:,4], y= df_summary['death%'], data=df_summary, hue='air_poll_median', s=500)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.subplot(121)
sns.heatmap(heatmapshow, annot=True, annot_kws={'size':20})

plt.show()