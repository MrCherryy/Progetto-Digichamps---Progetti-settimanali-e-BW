import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency_7212563912390016675 (1).csv')

df['Date raggruppate'] = df[['1990', '1991', '1992', '1993', '1994']].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)

flood_storm = df[df['Indicator'].str.contains('Flood|Storm')][['Date raggruppate', 'Indicator']]

flood_storm['Date raggruppate'] = pd.to_datetime(flood_storm['Date raggruppate'], errors='coerce')
flood_storm = flood_storm.pivot_table(index='Date raggruppate', columns='Indicator', aggfunc='size', fill_value=0)

flood_storm.plot(kind='bar', stacked=True, color=['blue', 'red'])
plt.title('Disastri naturali per data (Flood vs Storm)')
plt.xlabel('Date')
plt.ylabel('Numero di disastri')
plt.legend(title='Tipo di disastro')

plt.tight_layout()
plt.show()