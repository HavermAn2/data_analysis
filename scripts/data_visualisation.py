import pandas as pd
import matplotlib.pyplot as plt

gdp = pd.read_csv("./data/clean_gdp.csv")


row = gdp.loc[1]#row of the nasessary country
print(gdp.columns)
countrys_name = row["country"]# get countrys name
print(countrys_name)
gdp_cols = [col for col in gdp.columns if '_gdp' in col and col != 'country']# leave only columns with "GDP"
Albania = row[gdp_cols]
Albania.index = [col.replace('_gdp', '')for col in gdp_cols] #Remove "GDP" becouse we must have only numbers without any letters
Albania = Albania.replace({ ',': '', ' ': ''}, regex=True)# remove all commas and holes
Albania = pd.to_numeric(Albania, errors='coerce') #turn all objects to numbers( all values were objects but for visualisation we need numbers)


print(Albania)
Albania.plot(kind ='bar')
plt.title(countrys_name)
plt.show()