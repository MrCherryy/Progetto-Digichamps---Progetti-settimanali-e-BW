import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

plt.figure(figsize=(12,6))
df_regioni["Date"] = pd.to_datetime (df_regioni["Date"], dayfirst= True)
df_regioni.set_index("Date", inplace=True)

plt.subplot(121)
df_regioni.resample("M")["Daily_Deaths"].sum().plot(kind = "line", color = 'r')
plt.title("Andamento Temporale dei Decessi")

plt.subplot(122)
df_regioni.resample("M")["NewPositiveCases"].sum().plot(kind = "line")
plt.title("Andamento Temporale dei Decessi e dei Contagi")
#plt.savefig("Andamento Temporale dei Casi Positivi vs Decessi.png", dpi= 600)
plt.show()

