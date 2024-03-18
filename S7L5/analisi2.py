import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("dataset_pulito.csv") 
df['data_osservazione'] = pd.to_datetime(df['data_osservazione']) 
df = df.set_index('data_osservazione')

from scipy.stats import zscore
df['temperatura_media'] = zscore(df['temperatura_media'])
df['precipitazioni'] = zscore(df['precipitazioni'])
df['umidita'] = zscore(df['umidita'])
df['velocita_vento'] = zscore(df['velocita_vento'])

# Statistiche descrittive
df[['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']].describe()
print(df)

# Istogramma
plt.figure(figsize=(10, 8))
sns.histplot(data=df, x='temperatura_media', kde=True)
plt.title('Distribuzione Temperatura Media')
plt.xlabel('Temperatura Media')
plt.ylabel('Frequenza')
plt.savefig('istogramma_temperatura_media.png', dpi=100)
plt.show()


plt.figure(figsize=(10, 8))
sns.histplot(data=df, x='stazione_meteorologica', weights=df['temperatura_media'])
plt.title('Distribuzione Temperatura Media')
plt.xlabel('Stazione Meteorologica')
plt.ylabel('Temperatura Media')
plt.savefig('istogramma_stazione.png')
plt.show()

# Box plots
plt.figure(figsize=(10, 8))
sns.boxplot(data=df[['precipitazioni', 'umidita', 'velocita_vento']])
plt.title('Distribuzione Precipitazioni, umidita, velocita Vento')
plt.xlabel('Variabile')
plt.ylabel('Valore')
plt.savefig('boxplot_precipitazioni.png')
plt.show()

daily_mean_temperatura = df['temperatura_media'].resample('D').mean()
import matplotlib.pyplot as plt

# Istogramma
plt.figure(figsize=(10, 6))
plt.hist(daily_mean_temperatura, bins=20, edgecolor='black')
plt.xlabel('Temperatura Media')
plt.ylabel('Frequenza')
plt.title('Istogramma della Temperatura Media Giornaliera')
plt.savefig('istogramma_media.png')
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(daily_mean_temperatura)
plt.ylabel('Temperatura Media')
plt.title('Boxplot della Temperatura Media Giornaliera')
plt.savefig('boxplotmedia.png')
plt.show()
# Heatmap

plt.figure(figsize=(10, 8))
sns.heatmap(df[['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']].corr(), cmap='coolwarm', annot=True)
plt.title('Correlazione tra Variabili Meteorologiche')

plt.savefig('heatmap.png')
plt.show()
# Identificazione delle correlazioni significative
# Supponiamo che sia stato calcolato una matrice di correlazione e sia stato assegnato a correlation_matrix
print(df[['temperatura_media', 'precipitazioni', 'umidita', 'velocita_vento']].corr())
