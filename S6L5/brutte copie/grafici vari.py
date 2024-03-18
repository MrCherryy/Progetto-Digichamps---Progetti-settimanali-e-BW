import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")

region_count = df['region'].value_counts()

plt.bar(region_count.index, region_count.values)
plt.xlabel('Regione')
plt.ylabel('Conteggio')
plt.title('Distribuzione delle regioni nel dataset')
plt.show()

# Grafico a torta per il numero dei figli

numero_figli = df['children'].value_counts()

plt.pie(numero_figli, labels=numero_figli.index, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Distribuzione del numero di figli nel dataset')
plt.show()

# Grafico a barre per il numero dei fumatori 
smoker_count = df['smoker'].value_counts()

plt.bar(smoker_count.index, smoker_count.values)
plt.xlabel('Fumatore')
plt.ylabel('Conteggio')
plt.title('Distribuzione dei fumatori nel dataset')
plt.show()

# Calcolo spese medie per ciascun numero di figli
spese_medie_per_numero_figli = df.groupby('children')['charges'].mean()
plt.bar(spese_medie_per_numero_figli.index, spese_medie_per_numero_figli.values)
plt.xlabel('Numero di figli')
plt.ylabel('Spese medie')
plt.title('Distribuzione delle spese mediche per numero di figli')
plt.show()

# Grafico a dispersione 
plt.scatter(df['bmi'], df['charges'])
plt.xlabel('BMI')
plt.ylabel('Spese mediche')
plt.title('Correlazione tra BMI e spese mediche')
plt.show()