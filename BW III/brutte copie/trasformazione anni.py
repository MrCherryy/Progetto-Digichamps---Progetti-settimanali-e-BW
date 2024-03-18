import pandas as pd 

csv = pd.read_csv("Indicator_11_1_Physical_Risks_Climate_related_disasters_frequency_7212563912390016675 (1).csv", encoding='latin1')
csv.columns
anni = ['1995', '1996', '1997', '1998', '1999',
       '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
       '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
       '2018']
print(anni)
years = pd.DataFrame()
for y in anni:
    df = pd.DataFrame()
    df["Country"] = csv["Country"].replace(",","",regex=True)
    df["Value"]= csv[y]
    df["Year"] = y
    years = pd.concat([years,df], ignore_index=True)
print(years)

years.to_csv("Indicator_3_1_Climate_Indicators_Annual_transformed2.csv",index=False, encoding='utf-8')