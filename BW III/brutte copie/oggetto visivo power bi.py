import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('02 modern-renewable-energy-consumption.csv')

# Filtra i dati considerando solo i nomi dei paesi
world_countries = ["Austria", "Canada", "China", "France", "Germany", "India", "Italy", "Japan", "Netherlands", "Spain", "Sweden", "Switzerland", "United Kingdom", "United States", "Brazil", "Turkey", "South Korea", "Russian Federation"]

data = data[data['Entity'].isin(world_countries)]

data['Total Generation'] = data['Solar Generation - TWh'] + data['Wind Generation - TWh'] + data['Hydro Generation - TWh'] + data['Geo Biomass Other - TWh']

grouped_data = data.groupby('Entity')['Total Generation'].sum().nlargest(10)

plt.figure(figsize=(12, 6))
grouped_data.plot(kind='bar', color='skyblue')
plt.xlabel('Entity')
plt.ylabel('Total Generation (TWh)')
plt.title('Top 10 Total Generation by Entity (World Countries)')
plt.xticks(rotation=45)

plt.savefig('bar_chart_top10_countries.png')

from PIL import Image
import base64

with open("bar_chart_top10_countries.png", "rb") as image_file:
    encoded_string_top10_countries = base64.b64encode(image_file.read()).decode('utf-8')

print(f'<img src="data:image/png;base64,{encoded_string_top10_countries}"/>')