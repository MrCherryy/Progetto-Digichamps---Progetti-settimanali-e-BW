'''from matplotlib import pyplot as plt
from numpy import random as rnd
import humanize as h

data = rnd.randint(0, 100, 10)
x = [h.ordinal(i) for i in range (1, 11)]
plt.plot(x, data, color="r", linewidth=3, linestyle="--", marker="x")

others = rnd.randint(0, 100, 15)
ox = [h.ordinal(i) for i in range (1, 16)]
plt.plot(ox, others, color="m", linewidth=2, linestyle="", marker="o")

plt.title("Il mio primo grafico", color="green")

plt.show()
'''

import seaborn as sns
anscombe = sns.load_dataset("anscombe")
print(anscombe.sample(10))

datasetI = anscombe[anscombe.dataset == "I"]
sns.lmplot(data = datasetI)
