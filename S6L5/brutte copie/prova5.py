import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# from seaborn import set
df = pd.read_csv("analisi_pulite.csv")

numero_figli = df['children'].value_counts()

sns.set(style="whitegrid") 
plt.pie(numero_figli, labels=numero_figli.index, autopct='%1.1f%%') 
plt.axis('equal') 
plt.title('Distribuzione del numero di figli nel dataset') 
plt.savefig('Grafico_torta_distruzione_numero_figli') 
plt.show()