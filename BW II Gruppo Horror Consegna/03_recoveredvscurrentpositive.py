import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv("covid19_region_python_w_daily_deaths.csv", sep=",")

plt.figure(figsize=(12,6))
df_regioni["Date"] = pd.to_datetime (df_regioni["Date"], dayfirst= True)
df_regioni.set_index("Date", inplace=True)

df_regioni.resample("M")["Recovered"].sum().plot(kind = "line")
df_regioni.resample("M")["CurrentPositiveCases"].sum().plot(kind = "line")

plt.legend(["Recovered","CurrentPositiveCases"], loc = "best")
plt.title("Andamento Temporale dei Guariti vs Current Positive")
plt.show()