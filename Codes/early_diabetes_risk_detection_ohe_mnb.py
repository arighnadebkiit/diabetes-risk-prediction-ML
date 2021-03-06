# -*- coding: utf-8 -*-
"""Early_Diabetes_Risk_Detection_Ohe_MNB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HGyYmtyyIt93mPXEWLBJS_mlv0UeqplP

# Data Pre-processing

# Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""# Importing the dataset"""

dataset = pd.read_csv('diabetes_data_upload.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

"""# Encoding categorical data
# Encoding independent variables
"""

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore', drop='if_binary')
X = np.array(ohe.fit_transform(X))
print(X)

"""# Encoding dependent variables"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

"""# Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35, random_state = 1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

"""# Training the Multimonial Naive Bayes model on the Training set"""

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

"""# Predicting the Test set results"""

y_pred = classifier.predict(X_test)

"""# Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""# Estimating precision, recall and F1 score"""

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
fscore = f1_score(y_test, y_pred, average='binary')
print('Precision: %.2f' % precision)
print('Recall: %.2f' % recall)
print('F1 score: %.2f' % fscore)

"""# Estimating ROC curve and ROC area"""

from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
roc_scr = roc_auc_score(y_test, y_pred)
print(roc_scr)
fpr, tpr, _ = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)

"""# Plot of a ROC curve"""

plt.figure()
lw = 2
plt.plot(
    fpr,
    tpr,
    color="darkorange",
    lw=lw,
    label="ROC curve (area = %0.2f)" % roc_auc,
)
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver operating characteristic example")
plt.legend(loc="lower right")
plt.show()

"""# Computing the accuracy with k-fold cross validation"""

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))