
import seaborn as sns

import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

num_ponti = titanic['deck'].nunique()
print("Il numero di ponti sulla nave è:", num_ponti)

dati_mancanti = titanic.isnull().sum()
print("Dati mancanti:")
print(dati_mancanti)

sns.lmplot(x='age', y='fare', data=titanic)