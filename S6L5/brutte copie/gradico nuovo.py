import pandas as pd

# Carica il dataset
df = pd.read_csv('insurance.csv')

# Definisci le variabili del BMI
df['bmi_category'] = pd.cut(df['bmi'],
                            bins=[0, 25, 30, float('inf')],
                            labels=['sovrappeso', 'obeso', 'molto obeso'])

# Raggruppa per la variabile del BMI e calcola la media delle charges per ogni categoria
charges_by_bmi = df.groupby('bmi_category')['charges'].mean()

print(charges_by_bmi)

import matplotlib.pyplot as plt

# Crea una figura e un'area degli assi
fig, ax = plt.subplots()

# Crea il grafico a barre
ax.bar(charges_by_bmi.index, charges_by_bmi)

# Aggiungi etichette agli assi
ax.set_xlabel('BMI Category')
ax.set_ylabel('Mean Charges')
ax.set_title('Mean Charges by BMI Category')

# Ruota le etichette dell'asse x di 45 gradi per una migliore leggibilità
plt.xticks(rotation=45)

# Mostra il grafico
plt.show()