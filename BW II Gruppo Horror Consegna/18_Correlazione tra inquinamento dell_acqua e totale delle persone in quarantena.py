import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#importazione file fiumi
df_fiumi=pd.read_csv("fiumi_clean.csv", sep = ";")

#importazione file regioni
df_regioni=pd.read_csv("covid19_region _python.csv", sep = ";")

#metto lo zero al posto dei nan in modo tale che si possono sommare i valori (anche quelli nulli)
df_fiumi = df_fiumi.fillna(0)

tab_unite = df_regioni.merge(df_fiumi, left_index=True, right_index=True)

sns.color_palette("plasma", as_cmap=True)
corr= tab_unite[["Macrobenthos_2020", "Pesci_2020", "HomeConfinement_y"]].corr()
# poi definisco la heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True)
plt.title("Correlazione tra inquinamento dell'acqua e totale delle persone in quarantena")
plt.show()