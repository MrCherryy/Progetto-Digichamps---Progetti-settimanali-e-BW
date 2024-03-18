# Media spese mediche a seconda della fascia di BMI

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('analisi_pulite.csv')

persone_sottopeso = data[(data['bmi'] <= 18.5) & ((data['sex'] == 'male') | (data['sex'] == 'female'))]
persone_normopeso = data[(data['bmi'] >= 18.5) & (data['bmi'] <= 24.9) & ((data['sex'] == 'male') | (data['sex'] == 'female'))]
persone_sovrappeso = data[(data['bmi'] >= 25) & (data['bmi'] <= 29) & ((data['sex'] == 'male') | (data['sex'] == 'female'))]
persone_obese = data[(data['bmi'] >= 30) & (data['bmi'] <= 34.9) & ((data['sex'] == 'male') | (data['sex'] == 'female'))]
persone_severamente_obese = data[(data['bmi'] >= 35) & ((data['sex'] == 'male') | (data['sex'] == 'female'))]

# Creo una lista di colori, il primo elemento rappresenta il colore delle colonne maschili e il secondo delle colonne femminili
colori = ['blue', 'pink']

fasce_di_peso = ['Sottopeso', 'Normopeso', 'Sovrappeso', 'Obesi', 'Fortemente obesi']

# Calcolo la media delle charges per le persone sovrappeso, obese e molto obese per genere
media_sottopeso_maschi = persone_sottopeso[persone_sottopeso['sex'] == 'male']['charges'].mean()
media_sottopeso_femmine = persone_sottopeso[persone_sottopeso['sex'] == 'female']['charges'].mean()
media_normopeso_maschi = persone_normopeso[persone_normopeso['sex'] == 'male']['charges'].mean()
media_normopeso_femmine = persone_normopeso[persone_normopeso['sex'] == 'female']['charges'].mean()
media_sovrappeso_maschi = persone_sovrappeso[persone_sovrappeso['sex'] == 'male']['charges'].mean()
media_sovrappeso_femmine = persone_sovrappeso[persone_sovrappeso['sex'] == 'female']['charges'].mean()
media_obesi_maschi = persone_obese[persone_obese['sex'] == 'male']['charges'].mean()
media_obesi_femmine = persone_obese[persone_obese['sex'] == 'female']['charges'].mean()
media_severamente_obesi_maschi = persone_severamente_obese[persone_severamente_obese['sex'] == 'male']['charges'].mean()
media_severamente_obese_femmine = persone_severamente_obese[persone_severamente_obese['sex'] == 'female']['charges'].mean()

# Creo una lista di valori medi per entrambi i generi
valori_medie_maschi = [media_sottopeso_maschi, media_normopeso_maschi, media_sovrappeso_maschi, media_obesi_maschi, media_severamente_obesi_maschi]
valori_medie_femmine = [media_sottopeso_femmine, media_normopeso_femmine, media_sovrappeso_femmine, media_obesi_femmine, media_severamente_obese_femmine]

# Creo il grafico a barre specificando i colori per le colonne maschili e femminili
plt.figure(figsize=(10,6))
bar_width = 0.35
plt.bar(fasce_di_peso, valori_medie_maschi, width=bar_width, color=colori[0], label='Maschi')
plt.bar([x + bar_width for x in range(len(fasce_di_peso))], valori_medie_femmine, width=bar_width, color=colori[1], label='Femmine')
plt.xlabel('Fasce di peso')
plt.ylabel('Media delle spese mediche')
plt.title('Media delle spese mediche per fasce di peso e genere')
plt.xticks([x + bar_width/2 for x in range(len(fasce_di_peso))], fasce_di_peso)
plt.legend()
plt.show()