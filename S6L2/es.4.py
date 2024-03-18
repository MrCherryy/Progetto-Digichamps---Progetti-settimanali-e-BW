import numpy as np
# importo la libreria di Numpy

lunghezza = 28.75
numero_rivetti = 15

# creo le mie variabili 
distanza = lunghezza / (numero_rivetti - 1)

# calcolo la distanza tra i rivetti

punti = np.linspace(0, lunghezza, numero_rivetti)

print(punti)
print(punti.shape[0])

# controllo che abbia calcolati tutti e 15 i rivetti 