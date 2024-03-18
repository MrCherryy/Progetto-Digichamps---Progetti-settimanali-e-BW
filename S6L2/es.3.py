import numpy as np

linear_data = np.array([x for x in range(27)])
print(linear_data)
reshaped_data = linear_data.reshape((3, 3, 3))
print(reshaped_data)

# Il nuovo array ha tre dimensioni.
# Per accedere ai singoli elementi devo utilizzare le parentesi quadre indicizzate.