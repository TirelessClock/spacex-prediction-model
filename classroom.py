import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("dataset.csv")
y = data["Class"].to_numpy()
x = pd.read_csv("dataset2.csv")

x = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x,y)

print(y_test.shape)