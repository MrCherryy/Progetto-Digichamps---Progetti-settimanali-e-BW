import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


data = pd.read_csv("covid19_europe.csv", delimiter=';')

# conversione datetime
data['dateRep'] = pd.to_datetime(data['dateRep'], dayfirst=True)

# Aggiungo una colonna 'month_year' per facilitare l'aggregazione
data['month_year'] = data['dateRep'].dt.to_period('M')

# Aggrego i dati per mese e paese
casi_mensili = data.groupby(['month_year', 'countriesAndTerritories'])['cases'].sum().reset_index()

# Filtro
selezioni_paesi = ['Italy', 'Belgium', 'Spain', 'United_Kingdom', 'France']
filtro_casi = casi_mensili[casi_mensili['countriesAndTerritories'].isin(selezioni_paesi)]

# Conterto la data in stringa, ma da rivedere quest psg
filtro_casi['month_year_str'] = filtro_casi['month_year'].dt.strftime('%B')

# Colori
colors = {
    'Italy': '#5302a3',
    'Belgium': '#000000',
    'Spain': 'red',
    'United_Kingdom': 'blue',
    'France': 'orange'
}

# Grafico
plt.figure(figsize=(15, 8))
sns.lineplot(data=filtro_casi, x='month_year_str', y='cases', hue='countriesAndTerritories', palette=colors)
plt.xticks(rotation=45)
plt.title('Andamento Mensile dei Casi COVID-19 nei Principali Paesi Europei')
plt.xlabel('Mese e Anno')
plt.ylabel('Numero di Casi')
plt.legend(title='Paese', title_fontsize='large', fontsize='large', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

