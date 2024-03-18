import pandas as pd
import prova5 as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("analisi_pulite.csv")

# Create the scatter plot
sns.scatterplot(data=df, x="sex", y="bmi", hue="sex", palette=["blue", "pink"])

# Set the plot title and labels
plt.title("Relazione tra Genere e BMI")
plt.xlabel("Genere")
plt.ylabel("BMI")

# Show the plot
plt.show()

# 3. Analisi delle differenze di costo tra fumatori e non fumatori
print("\nAnalisi delle differenze di costo tra fumatori e non fumatori:")
spese_per_fumatori = df[df['smoker'] == 'yes']['charges']
spese_per_non_fumatori = df[df['smoker'] == 'no']['charges']
print("Media spese per fumatori:", spese_per_fumatori.mean())
print("Media spese per non fumatori:", spese_per_non_fumatori.mean())
plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Differenze di costo tra fumatori e non fumatori')
plt.xlabel('Fumatore')
plt.ylabel('Spese mediche')
plt.show()