import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
plt.style.use('ggplot')
pd.set_option('display.precision',2)
df=pd.read_csv('C:/Samay/Week3/breast_cancer_coimbra.csv')
df=df.drop(['Classification'],axis=1)
df=df.rename(columns={'MCP.1':'MCP-1'})
graph=df['Age'].plot(kind='hist',title='Age Distribution')
graph.set_xlabel('Age')
plt.show()
df.plot(kind='scatter',x='Glucose',y='Insulin',title='Glucose vs Insulin')
plt.show()
sns.scatterplot(x='Glucose',y='Insulin',hue='HOMA',data=df,title='Glucose vs Insulin')
plt.show()
sns.pairplot(df,vars=['BMI','Adiponectin','Resistin','MCP-1'])
plt.show()
df_corr=df[['BMI','Adiponectin','Resistin','MCP-1']].dropna().corr()
sns.heatmap(df_corr,annot=True)
plt.show()