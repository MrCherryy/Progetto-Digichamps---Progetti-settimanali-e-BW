import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

df_comuni = pd.read_csv("comuni_clean.csv", sep=";")

# Popolazione totale per regione
tot_popolazione = df_comuni.groupby("Regione")["Popolazione2011"].sum()

# Grafico lineare
df_regioni['Date'] = pd.to_datetime(df_regioni['Date'])
df_regioni_pivot = df_regioni.pivot_table(index='Date', columns='RegionName', values='Deaths')

# Percentuale di decessi
df_regioni_percent = df_regioni_pivot.div(tot_popolazione, axis=1) * 100
print(df_regioni_percent)

# Creazione del grafico lineare
fig = plt.figure(figsize=(24, 15))
ax1 = fig.add_subplot(121)

list_Regions = tot_popolazione.index  # Lista delle regioni
for region in list_Regions:
    ax1 = sns.lineplot(data=df_regioni_percent[region].dropna(), label=region)

ax1.grid(color='gray', linestyle='-', linewidth=0.3)
ax1.legend()
plt.xticks(rotation=90)
plt.title('Percentuale Decessi nel tempo per regione')

# Creazione della tabella
ax2 = fig.add_subplot(122)
font_size = 14
bbox = [0, 0, 1, 1]
ax2.axis('off')
mpl_table = ax2.table(cellText=df_regioni_percent.iloc[-1].sort_values(ascending=False).reset_index().values, colLabels=['RegionName', 'Death %'], bbox=bbox)
mpl_table.auto_set_font_size(False)
mpl_table.set_fontsize(font_size)

plt.show()