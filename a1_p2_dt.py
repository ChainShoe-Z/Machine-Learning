# -*- coding: utf-8 -*-
"""a1_p2_dt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y-IEAQS9319prT3gXfy5w765foCLCtc1
"""

#use the breast cancer as dataset, 0 is no cancer, 1 is having cancer
from sklearn import tree
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn.datasets as datasets
import numpy as np
import pandas as pd

can = load_breast_cancer()
#can.feature_names
import pandas as pd
#pd.concat([pd.DataFrame(can.data),pd.DataFrame(can.target)],axis=1)
#can.target

x_train,x_test,y_train,y_test = train_test_split(can.data,can.target,test_size=0.2)

clf = tree.DecisionTreeClassifier(
                  random_state=20
                  ,splitter ="random"

)
clf = clf.fit(x_train,y_train)
score = clf.score(x_test,y_test)
score

#x_train.shape

#used to find the best max_depth
import matplotlib.pyplot as plt
from matplotlib.pyplot import*
test=[]
for i in range(10):
  clf = tree.DecisionTreeClassifier(max_depth=i+1
                    ,random_state=20
                    ,splitter ="random"
                    ,criterion="entropy"
                                    )
  clf = clf.fit(x_train,y_train)
  score = clf.score(x_test, y_test)
  test.append(score)
plt.plot(range(1,11),test,color="red",label="max_depth")
plt.legend()
plt.show()

#find the best max_features
import matplotlib.pyplot as plt
from matplotlib.pyplot import*
test=[]
for i in range(24,30):
  clf = tree.DecisionTreeClassifier(max_depth=5
                    ,random_state=20
                    ,splitter ="random"
                    ,criterion="entropy"
                    ,max_features=i+1
                                    )
  clf = clf.fit(x_train,y_train)
  score = clf.score(x_test, y_test)
  test.append(score)
plt.plot(range(25,31),test,color="red",label="max_features")
plt.legend()
plt.show()

clf = tree.DecisionTreeClassifier(
                  random_state=20
                  ,splitter ="random"
                  ,criterion="entropy"
                  ,max_depth=5
                  ,max_features=26

)
clf = clf.fit(x_train,y_train)
score = clf.score(x_test,y_test)
score

import graphviz
from sklearn import tree

thisdata = tree.export_graphviz(clf
                  ,out_file=None
                  ,filled=True
                  ,feature_names=can.feature_names)
graph = graphviz.Source(thisdata)
graph