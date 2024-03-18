import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'tipo']

df = pd.read_csv(url, names=column_names)
print(df.columns)
print(df.head())
print(df.tail())
print(df.describe())