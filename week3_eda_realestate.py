import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
plt.style.use('classic')
pd.set_option('display.max_rows',100)
ds=pd.read_csv('C:/Samay/Week3/Real_estate_valuation_data_set.csv')
print(ds.head())
ds=ds.drop(['X5 latitude','X6 longitude'],axis=1)
ds=ds.rename(columns={'X2 house age':'X2 house age(yr)','Y house price of unit area':'Y house price per unit area($)','X3 distance to the nearest MRT station':'X3 distance to the nearest MRT station(m)'})
graph=ds['Y house price per unit area($)'].plot(kind='kde',title='House Price Per Unit Area Frequency')
graph.set_xlabel('Price Per Unit Area ($)')
plt.show()
graph=sns.scatterplot(x='X3 distance to the nearest MRT station(m)',y='Y house price per unit area($)',hue='X4 number of convenience stores',data=ds)
graph.set_title('Effect of house price on the nearest MRT station')
plt.show()