import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carico il df pulito
df = pd.read_csv("dataset_pulito.csv")
df['data_osservazione'] = pd.to_datetime(df['data_osservazione'])

df.set_index('data_osservazione', inplace=True)
d1 = df.resample("ME")["temperatura_media"].mean().plot(kind="bar")
# Calcolo delle statistiche descrittive
statistiche = df.describe()
print(statistiche)

# Creazione degli istogrammi e box plots
for column in df.columns:
    plt.figure()
    sns.histplot(df[column])
    plt.title(column)
    plt.show()
    
    plt.figure()
    sns.boxplot(data=df[column])
    plt.title(column)
    plt.show()

'''
# Creazione della matrice di correlazione
correlation_matrix = df.corr()
plt.figure()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlazione tra variabili meteorologiche")
plt.show()

# Identificazione delle correlazioni significative
significant_correlations = correlation_matrix[abs(correlation_matrix) > 0.7].stack().reset_index()
significant_correlations = significant_correlations[significant_correlations['level_0'] != significant_correlations['level_1']]
significant_correlations.columns = ['Variabile 1', 'Variabile 2', 'Correlazione']
significant_correlations = significant_correlations.dropna()
print("Correlazioni significative:")
print(significant_correlations)

# Esempio di interpretazione dei risultati
print("L'umidità e le precipitazioni mostrano una correlazione significativa di", significant_correlations['Correlazione'][0], "che potrebbe suggerire una relazione tra la quantità di precipitazioni e l'umidità dell'aria.")
'''