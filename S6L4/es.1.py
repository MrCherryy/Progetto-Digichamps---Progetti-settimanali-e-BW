import pandas as pd
import matplotlib.pyplot as plt

# Scarica il dataset
url = "https://github.com/plotly/datasets/raw/master/stockdata.csv"
dataset = pd.read_csv(url)

# Estrai i dati della colonna MSFT
msft_data = dataset['MSFT']

# Visualizza i dati mediante pyplot
plt.plot(msft_data)
plt.xlabel('Indice')
plt.ylabel('Valore Azioni MSFT')
plt.title('Andamento azioni MSFT')
plt.show()

# Estrai le prime 5 righe di MSFT e date
first_5_rows = dataset[['Date', 'MSFT']].head()

# Crea un grafico con le prime 5 righe
plt.plot(first_5_rows['Date'], first_5_rows['MSFT'])
plt.xlabel('Data')
plt.ylabel('Valore Azioni MSFT')
plt.title('Andamento azioni MSFT - prime 5 righe')
plt.show()

# Estrai le ultime 5 righe di MSFT e date
last_5_rows = dataset[['Date', 'MSFT']].tail()

# Crea un grafico con le ultime 5 righe
plt.plot(last_5_rows['Date'], last_5_rows['MSFT'])
plt.xlabel('Data')
plt.ylabel('Valore Azioni MSFT')
plt.title('Andamento azioni MSFT - ultime 5 righe')
plt.show()