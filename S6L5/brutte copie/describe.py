import pandas as pd
import matplotlib.pyplot as plt

def describe_dataset(analisi_pulite):
    # Carico il dataset in un DataFrame
    df = pd.read_csv(analisi_pulite)

    # Calcolo le statistiche descriptive per le colonne numeriche
    description = df.describe()

    # Stampo le statistiche descriptive
    print(description)

    # Creo un grafico a barre per la colonna 'age'
    df['charges'].value_counts().plot(kind='bar')
    plt.xlabel('Valori')
    plt.ylabel('Conteggio')
    plt.title('Grafico a barre')

    # Mostra il grafico
    plt.show()

    # Creo un istogramma per la colonna 'charges'
    df['charges'].plot(kind='hist', bins=10)
    plt.xlabel('Valori')
    plt.ylabel('Frequenza')
    plt.title('Istogramma')

    # Mostra il grafico
    plt.show()

    # Calcolo la correlazione tra 'age' e 'charges'
    correlation = df['age'].corr(df['charges'])

    # Creo un diagramma di dispersione per visualizzare la correlazione tra 'age' e 'charges'
    plt.scatter(df['age'], df['charges'])
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.title(f'Correlazione tra Age e Charges: {correlation}')

    # Mostra il grafico
    plt.show()

# Esempio di utilizzo
dataset_path = "analisi_pulite.csv"
describe_dataset(dataset_path)