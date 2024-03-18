import numpy as np

# Creazione dell'ndarray 5x5
arr = np.array([[10, 20, 15, 30, 25],
                [5, 8, 12, 18, 9],
                [7, 4, 11, 6, 14],
                [22, 17, 23, 29, 27],
                [16, 13, 19, 21, 24]])

# Calcolo del minimo e massimo
min_val = np.min(arr)
max_val = np.max(arr)

# Sottrazione del minimo e divisione per il massimo - minimo
result = (arr - min_val) / (max_val - min_val)

print(result)