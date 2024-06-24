from ucimlrepo import fetch_ucirepo 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
import numpy as np 
real_estate_evaluation=fetch_ucirepo(id=477)
X=real_estate_evaluation.data.features
Y=real_estate_evaluation.data.targets
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=3)
model=LinearRegression()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))