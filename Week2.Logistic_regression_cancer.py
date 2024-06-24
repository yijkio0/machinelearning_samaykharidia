from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from ucimlrepo import fetch_ucirepo 
cancer_dataset=fetch_ucirepo(id=451)
X=cancer_dataset.data.features
Y=cancer_dataset.data.targets
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
model=LogisticRegression()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))