# -*- coding: utf-8 -*-
"""a1_p2_rf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12q2CcyIULFSgfEPCa53yXiscrwG6uLbC
"""

# Commented out IPython magic to ensure Python compatibility.
#use the breast cancer as dataset, 0 is no cancer, 1 is having cancer
# %matplotlib inline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.datasets as datasets

can = load_breast_cancer()
can.target

rfc = RandomForestClassifier(n_estimators=100, random_state=20)

#plot score and the number of trees in the forest and get the best number
scorel = []
for i in range(0,200,10):
  rfc = RandomForestClassifier(n_estimators=i+1
                    ,n_jobs=-1
                    ,random_state=20
                  )
  score=cross_val_score(rfc,can.data,can.target,cv=10).mean()
  scorel.append(score)
print(max(scorel),(scorel.index(max(scorel))*10)+1)
plt.figure(figsize=[20,5])
plt.plot(range(1,201,10),scorel)
plt.show()

rfc = RandomForestClassifier(n_estimators=61
                 ,random_state=20
                 )
score_pre = cross_val_score(rfc,can.data,can.target,cv=10).mean()
score_pre