import prova5 as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a scatter plot using Seaborn
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Set plot title and axis labels using Matplotlib
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

# Display the plot
plt.show()