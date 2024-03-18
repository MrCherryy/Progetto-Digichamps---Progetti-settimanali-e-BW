
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.countplot(x='class', data=titanic)
plt.title('Numero di passeggeri per classe di imbarco')
plt.show()

sns.countplot(x='alive', data=titanic)
plt.title('Numero di passeggeri sopravvissuti')
plt.show()

plt.hist(titanic['fare'], bins=30)
plt.title('Distribuzione delle tariffe')
plt.xlabel('Fare')
plt.ylabel('Numero di passeggeri')
plt.show()

sns.boxplot(x='class', y='age', data=titanic)
plt.title('Distribuzione delle età rispetto alla classe di imbarco')
plt.show()

sns.swarmplot(x='class', y='age', data=titanic)
plt.title('Distribuzione delle età rispetto alla classe di imbarco')
plt.show()

sns.boxplot(x='fare', y='survived', data=titanic)
plt.title('Relazione tra fare e survived')
plt.show()

sns.lmplot(x='fare', y='survived', data=titanic)
plt.title('Relazione tra fare e survived')
plt.show()