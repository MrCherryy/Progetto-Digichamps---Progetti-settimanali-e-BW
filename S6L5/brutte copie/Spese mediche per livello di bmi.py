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

# Creo le liste delle fasce di peso e dei valori di media
fasce_di_peso = ['Sovrappeso M', 'Sovrappeso', 'Obesi', 'Obesi', 'Fortemente obesi', 'Fortemente obesi']
valori_medie = [media_sovrappeso_maschi, media_sovrappeso_femmine, media_obesi_maschi, media_obesi_femmine, media_molto_obesi_maschi, media_molto_obesi_femmine]

# Creo una lista di colori, il primo elemento rappresenta il colore delle colonne maschili e il secondo delle colonne femminili
colori = ['blue', 'pink']

# Creo il grafico a barre specificando i colori per le colonne maschili e femminili
plt.figure(figsize=(10,6))
plt.bar(fasce_di_peso, valori_medie, color=colori)
plt.xlabel('Fasce di peso - Genere')
plt.ylabel('Media delle spese mediche')
plt.title('Media delle spese mediche per fasce di peso e genere')
plt.xticks(rotation=45, fontsize=8)
plt.legend(labels=['Maschi', 'Femmine'], loc='upper center')
plt.show()

'''
# Creazione del subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Creazione delle liste dei valori medi
valori_medie_maschi = [media_sovrappeso_maschi, media_obesi_maschi, media_molto_obesi_maschi]
valori_medie_femmine = [media_sovrappeso_femmine, media_obesi_femmine, media_molto_obesi_femmine]

# Creazione dei colori per i grafici maschili e femminili
colori_maschi = ['blue', 'blue', 'blue']
colori_femmine = ['pink', 'pink', 'pink']

# Creazione dei grafici per i maschi
ax.bar([0, 1, 2], valori_medie_maschi, color=colori_maschi, label='Maschi')
# Creazione dei grafici per le femmine
ax.bar([0, 1, 2], valori_medie_femmine, color=colori_femmine, label='Femmine', bottom=valori_medie_maschi)

# Aggiunta delle etichette agli assi e al grafico
ax.set_xlabel('Fasce di peso')
ax.set_ylabel('Media delle spese mediche')
ax.set_title('Media delle spese mediche per fasce di peso e genere')

# Aggiunta delle etichette ai ticks dell'asse X
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['Sovrappeso', 'Obesi', 'Fortemente obesi'])

# Aggiunta delle etichette alla legenda
ax.legend()

# Visualizzazione del subplot
plt.show()
'''