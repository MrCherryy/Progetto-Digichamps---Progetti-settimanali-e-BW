import pandas as pd

# Scarica il file csv
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = pd.read_csv(url, header=None)

# Stampa le prime cinque righe
print(iris_data.head())

# Stampa i nomi delle colonne
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data.columns = column_names
print(iris_data.columns)

species = iris_data['species']
print(species)