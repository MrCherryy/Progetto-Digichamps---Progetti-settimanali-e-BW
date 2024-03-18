import pandas as pd
df = pd.read_json(r'C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\S7L4\Es2\link_di_wikipedia\link_della_pagina.json')
link_ripetuti = df['link'].value_counts()
print(link_ripetuti)
link_unici = df['link'].unique()
print(link_unici)
link_ripetuti = link_ripetuti[link_ripetuti > 10]
print(link_ripetuti)
massimo = df["link"].value_counts().idxmax()
print(massimo)