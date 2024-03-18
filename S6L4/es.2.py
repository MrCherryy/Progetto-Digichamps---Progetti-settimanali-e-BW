import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stockdata.csv')

# Estraggo le prime 20 istanze della colonna AAPL
aapl_values = df["AAPL"].head(20)

# Creo il grafico. Richieste esercizio: grafico rosso, linea tratteggiata, pallino come marker
#  l'asse delle ascisse si chiami "Data" e delle ordine "Valore". Titolo grafico: "Azioni Apple"
# il markerfacecolor sia nero e la linea spessore uguale a 2 
plt.plot(aapl_values, linestyle="--", marker="o", color="red", markerfacecolor="black", linewidth=2)

# Imposto i nomi degli assi
plt.xlabel("Data")
plt.ylabel("Valore")

# Imposto il titolo del grafico
plt.title("Azioni Apple")

# Mostro il grafico
plt.show()