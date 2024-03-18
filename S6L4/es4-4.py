import pandas as pd
import matplotlib.pyplot as plt

# Caricamento del dataset
df = pd.read_csv('election.csv')

# Grafico a barre dei voti totali per ogni candidato
totals = df[['Coderre', 'Bergeron', 'Joly']].sum()
totals.plot(kind='bar')
plt.ylabel('Voti totali')
plt.xlabel('Candidati')
plt.title('Voti totali per ogni candidato')
plt.show()

# Grafico a barre del numero di votanti per distretto
df.plot(x='district', y='total', kind='bar')
plt.ylabel('Numero di votanti')
plt.xlabel('Distretti')
plt.title('Numero di votanti per distretto')
plt.show()

# Grafico a barre comparativo dei voti per i primi 4 distretti
first_4_districts = df[:4]
first_4_districts[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar')
plt.ylabel('Voti')
plt.xlabel('Distretti')
plt.title('Voti nei primi 4 distretti per ogni candidato')
plt.legend(loc='upper right')
plt.show()

# Grafico a barre comparativo dei voti per i primi 4 distretti, impilato (stacked)
first_4_districts[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar', stacked=True)
plt.ylabel('Voti')
plt.xlabel('Distretti')
plt.title('Voti nei primi 4 distretti per ogni candidato (impilato)')
plt.legend(loc='upper right')
plt.show()

# Salvataggio dei grafici su disco in alta risoluzione
totals_plot = totals.plot(kind='bar')
totals_plot.figure.savefig('voti_totali.png', dpi=300)

districts_plot = df.plot(x='district', y='total', kind='bar')
districts_plot.figure.savefig('votanti_distretti.png', dpi=300)

first_4_districts_plot = first_4_districts[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar')
first_4_districts_plot.figure.savefig('voti_primi_4_distretti.png', dpi=300)

first_4_districts_stacked_plot = first_4_districts[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar', stacked=True)
first_4_districts_stacked_plot.figure.savefig('voti_primi_4_distretti_impilato.png', dpi=300)