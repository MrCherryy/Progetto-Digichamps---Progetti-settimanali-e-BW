import pandas as pd

df = pd.read_csv('analisi_pulite.csv')

persone_sovrappeso = df[(df['bmi'] >= 25) & (df['bmi'] <= 29) & ((df['sex'] == 'male') | (df['sex'] == 'female'))]
print(persone_sovrappeso)
persone_obese = df[(df['bmi'] >= 30) & (df['bmi'] <= 34.9) & ((df['sex'] == 'male') | (df['sex'] == 'female'))]
print(persone_obese)
persone_molto_obese = df[(df['bmi'] >= 35) & ((df['sex'] == 'male') | (df['sex'] == 'female'))]
print(persone_obese)
persone_sovrappeso_per_sesso = persone_sovrappeso['sex'].value_counts()
print(persone_sovrappeso_per_sesso)

import matplotlib.pyplot as plt
# Istogramma
# Calcolo la media delle charges per le persone sovrappeso, obese e molto obese per genere
media_sovrappeso_maschi = persone_sovrappeso[persone_sovrappeso['sex'] == 'male']['charges'].mean()
media_sovrappeso_femmine = persone_sovrappeso[persone_sovrappeso['sex'] == 'female']['charges'].mean()
media_obesi_maschi = persone_obese[persone_obese['sex'] == 'male']['charges'].mean()
media_obesi_femmine = persone_obese[persone_obese['sex'] == 'female']['charges'].mean()
media_molto_obesi_maschi = persone_molto_obese[persone_molto_obese['sex'] == 'male']['charges'].mean()
media_molto_obesi_femmine = persone_molto_obese[persone_molto_obese['sex'] == 'female']['charges'].mean()

# Creazione del subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Creazione dei valori delle fasce di peso
fasce_peso = ['Sovrappeso', 'Obesi', 'Fortemente obesi']

# Creazione delle liste dei valori medi
valori_medie_maschi = [media_sovrappeso_maschi, media_obesi_maschi, media_molto_obesi_maschi]
valori_medie_femmine = [media_sovrappeso_femmine, media_obesi_femmine, media_molto_obesi_femmine]

# Creazione dei grafici per i maschi
ax.hist(fasce_peso, weights=valori_medie_maschi, color='blue', alpha=0.7, label='Maschi')
# Creazione dei grafici per le femmine
ax.hist(fasce_peso, weights=valori_medie_femmine, color='pink', alpha=0.7, label='Femmine')

# Aggiunta delle etichette agli assi e al grafico
ax.set_xlabel('Fasce di peso')
ax.set_ylabel('Media delle spese mediche')
ax.set_title('Media delle spese mediche per fasce di peso e genere')

# Aggiunta delle etichette ai ticks dell'asse X
ax.set_xticks(fasce_peso)
ax.set_xticklabels(fasce_peso, rotation=45)

# Aggiunta delle etichette alla legenda
ax.legend()

# Visualizzazione del subplot
plt.show()