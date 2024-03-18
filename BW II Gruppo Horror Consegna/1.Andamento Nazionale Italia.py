# Andamento per mese dei nuovi casi positivi senza dividerlo per regione. Com'è andato in Italia il covid, e.g trovare il picco 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 
import calendar

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

df_regioni['Date'] = pd.to_datetime(df_regioni['Date'], dayfirst=True)

df_regioni['Month'] = df_regioni['Date'].dt.month

andamento_casi_anno = df_regioni.groupby('Month')['NewPositiveCases'].sum() 

# variabile per vedere il nome dei mesi in termini di pulizia presentazione
nomi_mesi = [calendar.month_name[month] 
             for month in andamento_casi_anno.index]

plt.figure(figsize=(12, 6))
sns.barplot(x=nomi_mesi, y=andamento_casi_anno.values, color='b')
plt.xlabel('Mese')
plt.ylabel('Nuovi casi positivi')
plt.title('Andamento Mensile dei Nuovi Casi Positivi in Italia')
plt.savefig('Andamento nuovi positivi per mese in Italia.png', dpi=200)
plt.show()