import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

data = pd.read_csv("dataset.csv")

y = data["Class"].to_numpy()
x = pd.read_csv("dataset2.csv")

x = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.1, random_state=2)

parameters ={"C":[0.01,0.1,1],'penalty':['l1','l2'], 'solver':['newton-cg', 'lbfgs', 'liblinear','saga']}

logreg_cv = LogisticRegression()

clf = GridSearchCV(logreg_cv ,param_grid = parameters, scoring='accuracy', cv=10)
clf.fit(x_train, y_train)

