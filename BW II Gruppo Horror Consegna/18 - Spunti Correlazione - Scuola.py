import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del file CSV
campioni_invalsi_df = pd.read_csv("Dati-campione-2013-2023.csv", sep=";")

# Pulizia dei dati (conversione del formato dei numeri)
campioni_invalsi_df.replace({',': '.'}, regex=True, inplace=True)
num_aggiustamento = ['Punteggio_WLE', 'ES', 'Deviazione_standard_WLE', 'ES_SD', 'Percentile5', 
                  'Percentile25', 'Percentile75', 'Percentile95']
campioni_invalsi_df[num_aggiustamento] = campioni_invalsi_df[num_aggiustamento].apply(pd.to_numeric, errors='coerce')

# Conversione dei tipi di dati
campioni_invalsi_df['Anno'] = campioni_invalsi_df['Anno'].astype(str)
campioni_invalsi_df['Grado'] = campioni_invalsi_df['Grado'].astype(str)

# Filtraggio per il grado 5 e la materia Matematica
filtro_grado_materia = (campioni_invalsi_df['Grado'] == '5') & (campioni_invalsi_df['Materia'] == 'Italiano')
df_filtrato = campioni_invalsi_df[filtro_grado_materia]

# Raggruppamento dei dati per Anno, Ripartizione_geografica e Materia
grouped_data = df_filtrato.groupby(['Anno', 'Ripartizione_geografica', 'Materia'])['Punteggio_WLE'].mean().reset_index()

# Filtraggio dei dati per includere solo le regioni di interesse
regioni_interesse = ['Lombardia', 'Veneto', 'Piemonte', 'Emilia Romagna', 'Lazio', 'Valle d\'Aosta', 'Marche']
grouped_data_filtrato = grouped_data[grouped_data['Ripartizione_geografica'].isin(regioni_interesse)]

# Visualizzazione dei dati filtrati
plt.figure(figsize=(12, 8))
sns.lineplot(x='Anno', y='Punteggio_WLE', hue='Ripartizione_geografica', style='Materia', data=grouped_data_filtrato)
plt.title("Media dei Punteggi WLE per Regione, Anno e Materia (Grado 5, Matematica)")
plt.ylabel("Media Punteggio WLE")
plt.xlabel("Anno")
plt.xticks(rotation=45)
plt.legend(title='Regione e Materia', loc='upper left')
plt.tight_layout()
plt.show()
