__author__ = 'm.kiselev@gmail.com'
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('titanic.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Pclass', 'Fare', 'Age', 'Sex'])
ndata = np.isnan(data)

print(ndata)

#clf = DecisionTreeClassifier()
#clf.fit()

