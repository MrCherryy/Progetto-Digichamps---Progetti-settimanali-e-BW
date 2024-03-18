import pandas as pd

df_regioni = pd.read_csv("Regioni_clean_venerdì_2.csv", sep=";")

df_regioni['Date'] = pd.to_datetime(df_regioni['Date']) 
df_regioni['Daily_Deaths'] = df_regioni.groupby('RegionName')['Deaths'].diff() 
df_regioni['Daily_Deaths'] = df_regioni['Daily_Deaths'].fillna(df_regioni['Deaths']) 
print(df_regioni[['Date', 'RegionName', 'Daily_Deaths']]) 
df_regioni.to_csv("covid19_region_python_w_daily_deaths.csv", index=False) 


# Esecuzione di un controllo per verificare i dati ottenuti tramite la nuova colonna
somma_morti_giornaliere = df_regioni.groupby('RegionName')['Daily_Deaths'].sum() 
print(somma_morti_giornaliere)
somma_morti_giornaliere = df_regioni['Daily_Deaths'].sum() 
print(somma_morti_giornaliere)