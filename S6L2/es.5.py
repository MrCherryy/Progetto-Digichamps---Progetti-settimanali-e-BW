import numpy as np

matrice = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = len(matrice)  # dimensione della matrice

# Inizializzare un ndarray con dimensione n x n, contenente zeri
ndarray = np.zeros((n, n))

# Inserire i valori originali nelle posizioni adatte
for i in range(n):
    for j in range(n):
        ndarray[i, j] = matrice[i][j]

print(ndarray)

# metodo casting

import numpy as np

matrice2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Creare una lista di liste
lista = [row[:] for row in matrice2]

# Effettuare un casting per ottenere un ndarray
ndarray2 = np.array(lista)

print(ndarray2)