import pandas as pd 
import numpy as np

df = pd.read_csv("wine.csv")

df_numerical = df.select_dtypes(include=np.number)

count = df_numerical.count() 
mode = df_numerical.mode().iloc[0] 
median = df_numerical.median() 
quartile_1 = df_numerical.quantile(0.25) 
quartile_3 = df_numerical.quantile(0.75) 
mean = df_numerical.mean() 
variance = df_numerical.var() 
std_deviation = df_numerical.std() 
min_value = df_numerical.min() 
max_value = df_numerical.max() 
summary_statistics = df_numerical.describe()

print("Count:\n", count) 
print("\nMode:\n", mode) 
print("\nMedian:\n", median) 
print("\nQuartile 1:\n", quartile_1) 
print("\nQuartile 3:\n", quartile_3) 
print("\nMean:\n", mean) 
print("\nVariance:\n", variance) 
print("\nStandard Deviation:\n", std_deviation) 
print("\nMin Value:\n", min_value) 
print("\nMax Value:\n", max_value) 
print("\nSummary Statistics:\n", summary_statistics)