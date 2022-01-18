# -*- coding: utf-8 -*-
"""Decisiontree(18/01/22).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18stnsiVEXJ8RXH7Vis1FPXARp77Rh49i
"""

import pandas as pd 
import numpy as np
from sklearn.datasets import load_iris

data=load_iris()

data.data.shape

print('classes to predict:',data.target_names)
print('features:',data.feature_names)

x=data.data
y=data.target
display(x.shape,y.shape)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=50,test_size=0.25)

#default criterion gini
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print('accuracy on train data using gini:',accuracy_score(y_train,classifier.predict(x_train)))
print('accuracy on test data using gini:',accuracy_score(y_test,y_pred))

#entropy
classifier_entropy=DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(x_train,y_train)
y_pred_entropy=classifier_entropy.predict(x_test)
print('accuracy on train data using entropy:',accuracy_score(y_train,classifier_entropy.predict(x_train)))
print('accuracy on test data using entopy:',accuracy_score(y_test,y_pred_entropy))

#entropy with min_samples_split
classifier_entropy1=DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
classifier_entropy1.fit(x_train,y_train)
y_pred_entropy1=classifier_entropy1.predict(x_test)
print('accuracy on train data using entropy:',accuracy_score(y_true=y_train,y_pred=classifier_entropy1.predict(x_train)))
print('accuracy on test data using entopy:',accuracy_score(y_true=y_test,y_pred=y_pred_entropy1))

#visualize
from sklearn.tree import export_graphviz #for visualization
from six import StringIO  #keep drawings
from IPython.display import Image #IPython interactive shell
import pydotplus #interface to export lang
dot_data=StringIO()
export_graphviz(classifier,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=data.feature_names,class_names=data.target_names)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

from sklearn.tree import export_graphviz #for visualization
from six import StringIO  #keep drawings
from IPython.display import Image #IPython interactive shell
import pydotplus #interface to export lang
dot_data=StringIO()
export_graphviz(classifier_entropy,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=data.feature_names,class_names=data.target_names)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

from sklearn.tree import export_graphviz #for visualization
from six import StringIO  #keep drawings
from IPython.display import Image #IPython interactive shell
import pydotplus #interface to export lang
dot_data=StringIO()
export_graphviz(classifier_entropy1,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=data.feature_names,class_names=data.target_names)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())