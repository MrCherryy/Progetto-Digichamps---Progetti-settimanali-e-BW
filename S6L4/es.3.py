import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stockdata.csv')

# Creo il grafico per le azioni di tutte le aziende
df.drop(columns=["Date"]).plot()

# Imposto i nomi degli assi
plt.xlabel("Data")
plt.ylabel("Valore")

# Imposto il titolo del grafico
plt.title("Andamento Azioni")

# Sposto la legenda in basso a destra
plt.legend(loc="lower right")

# Mostro il grafico
plt.show()