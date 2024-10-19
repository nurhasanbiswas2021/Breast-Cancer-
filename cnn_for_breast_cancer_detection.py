# -*- coding: utf-8 -*-
"""CNN for Breast Cancer Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15ljXCAZEZeuGty_0oBdv29ZRbG3qy43_

# Import essential libraries
"""



import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

"""# Load breast cancer dataset & explore

We are loading breast cancer data using a scikit-learn load_brast_cancer class.

Click on the below button to download the breast cancer data in CSV file format.
"""

from sklearn.datasets import load_breast_cancer
cancer_dataset = load_breast_cancer()
type(cancer_dataset)

"""The scikit-learn store data in an object bunch like a dictionary."""

cancer_dataset.keys()

cancer_dataset['data']

"""These numeric values are extracted features of each cell."""

cancer_dataset['target']

"""The target stores the values of malignant or benign tumors."""

cancer_dataset['target_names']

"""The cancer_dataset[‘DESCR’] store the description of breast cancer dataset."""

print(cancer_dataset['DESCR'])

"""Features name of malignant & benign tumor."""

print(cancer_dataset['feature_names'])

"""When we call load_breast_cancer() class it downloads breast_cancer.csv file and you can see file location."""

print(cancer_dataset['filename'])

"""# Create DataFrame

Click on the below button to download breast cancer DataFrame in CSV file format.
"""

cancer_df = pd.DataFrame(np.c_[cancer_dataset['data'],cancer_dataset['target']],
             columns = np.append(cancer_dataset['feature_names'], ['target']))

"""Head of cancer DataFrame"""

cancer_df.head(6)

"""The tail of cancer DataFrame"""

cancer_df.tail(6)

"""Getting information of cancer DataFrame using ‘.info()‘ method."""

cancer_df.info()

"""We have a total of non-null 569 patients’ information with 31 features. All feature data types in the float. The size of the DataFrame is 137.9 KB.

Numerical distribution of data. We can know to mean, standard deviation, min, max, 25%,50% and 75% value of each feature.
"""

cancer_df.describe()

"""# Data Visualization
Pair plot of breast cancer data

Basically, the pair plot is used to show the numeric distribution in the scatter plot.
"""

sns.pairplot(cancer_df, hue = 'target')

"""Pair plot of sample feature of DataFrame"""

sns.pairplot(cancer_df, hue = 'target',
             vars = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness'] )

"""# Counterplot"""

sns.countplot(cancer_df['target'])

plt.figure(figsize = (20,8))
sns.countplot(cancer_df['mean radius'])

"""# Heatmap
Heatmap of breast cancer DataFrame

In the below heatmap we can see the variety of different feature’s value. The value of feature ‘mean area’ and ‘worst area’ are greater than other and ‘mean perimeter’, ‘area error’, and ‘worst perimeter’ value slightly less but greater than remaining features.
"""

plt.figure(figsize=(16,9))
sns.heatmap(cancer_df)

"""# Heatmap of a correlation matrix

To find a correlation between each feature and target we visualize heatmap using the correlation matrix.
"""

plt.figure(figsize=(20,20))
sns.heatmap(cancer_df.corr(), annot = True, cmap ='coolwarm', linewidths=2)

"""# Correlation barplot

Taking the correlation of each feature with the target and the visualize barplot.
"""

cancer_df2 = cancer_df.drop(['target'], axis = 1)
print("The shape of 'cancer_df2' is : ", cancer_df2.shape)

plt.figure(figsize = (16,5))
ax = sns.barplot(x=cancer_df2.corrwith(cancer_df.target).index, y=cancer_df2.corrwith(cancer_df.target))
ax.tick_params(labelrotation = 90)

"""# Data Preprocessing
Split DataFrame in train and test
"""

X = cancer_df.drop(['target'], axis = 1)
X.head(6)

y = cancer_df['target']
y.head(6)

"""We have clean data to build the Ml model. But which Machine learning algorithm is best for the data we have to find. The output is a categorical format so we will use supervised classification machine learning algorithms.

To build the best model, we have to train and test the dataset with multiple Machine Learning algorithms then we can find the best ML model. So let’s try.

First, we need to import the required packages.
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 5)

"""# Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

"""# Breast Cancer Detection Machine Learning Model Building"""

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

"""# Support Vector Classifier"""

from sklearn.svm import SVC
svc_classifier = SVC()
svc_classifier.fit(X_train, y_train)
y_pred_scv = svc_classifier.predict(X_test)
accuracy_score(y_test, y_pred_scv)

svc_classifier2 = SVC()
svc_classifier2.fit(X_train_sc, y_train)
y_pred_svc_sc = svc_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_svc_sc)

"""# Logistic Regression

"""

from sklearn.linear_model import LogisticRegression
lr_classifier = LogisticRegression(random_state=51, penalty='l2')
lr_classifier.fit(X_train, y_train)
y_pred_lr = lr_classifier.predict(X_test)
accuracy_score(y_test, y_pred_lr)

lr_classifier2 = LogisticRegression(random_state=51, penalty='l2')
lr_classifier2.fit(X_train_sc, y_train)
y_pred_lr_sc = lr_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_lr_sc)

"""# K – Nearest Neighbor Classifier"""

from sklearn.neighbors import KNeighborsClassifier
knn_classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
knn_classifier.fit(X_train, y_train)
y_pred_knn = knn_classifier.predict(X_test)
accuracy_score(y_test, y_pred_knn)

knn_classifier2 = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
knn_classifier2.fit(X_train_sc, y_train)
y_pred_knn_sc = knn_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_knn_sc)

"""# Naive Bayes Classifier"""

from sklearn.naive_bayes import GaussianNB
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
y_pred_nb = nb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_nb)

nb_classifier2 = GaussianNB()
nb_classifier2.fit(X_train_sc, y_train)
y_pred_nb_sc = nb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_nb_sc)

"""# Decision Tree Classifier"""

from sklearn.tree import DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 51)
dt_classifier.fit(X_train, y_train)
y_pred_dt = dt_classifier.predict(X_test)
accuracy_score(y_test, y_pred_dt)

dt_classifier2 = DecisionTreeClassifier(criterion = 'entropy', random_state = 51)
dt_classifier2.fit(X_train_sc, y_train)
y_pred_dt_sc = dt_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_dt_sc)

"""# Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier.fit(X_train, y_train)
y_pred_rf = rf_classifier.predict(X_test)
accuracy_score(y_test, y_pred_rf)

rf_classifier2 = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier2.fit(X_train_sc, y_train)
y_pred_rf_sc = rf_classifier.predict(X_test_sc)
accuracy_score(y_test, y_pred_rf_sc)

"""# Adaboost Classifier"""

from sklearn.ensemble import AdaBoostClassifier
adb_classifier = AdaBoostClassifier(DecisionTreeClassifier(criterion = 'entropy', random_state = 200),
                                    n_estimators=2000,
                                    learning_rate=0.1,
                                    algorithm='SAMME.R',
                                    random_state=1,)
adb_classifier.fit(X_train, y_train)
y_pred_adb = adb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_adb)

adb_classifier2 = AdaBoostClassifier(DecisionTreeClassifier(criterion = 'entropy', random_state = 200),
                                    n_estimators=2000,
                                    learning_rate=0.1,
                                    algorithm='SAMME.R',
                                    random_state=1,)
adb_classifier2.fit(X_train_sc, y_train)
y_pred_adb_sc = adb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_adb_sc)

"""# XGBoost Classifier"""

from xgboost import XGBClassifier
xgb_classifier = XGBClassifier()
xgb_classifier.fit(X_train, y_train)
y_pred_xgb = xgb_classifier.predict(X_test)
accuracy_score(y_test, y_pred_xgb)

xgb_classifier2 = XGBClassifier()
xgb_classifier2.fit(X_train_sc, y_train)
y_pred_xgb_sc = xgb_classifier2.predict(X_test_sc)
accuracy_score(y_test, y_pred_xgb_sc)

"""# XGBoost Parameter Tuning Randomized Search"""

params={
 "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ]
}

from sklearn.model_selection import RandomizedSearchCV
random_search = RandomizedSearchCV(xgb_classifier, param_distributions=params, scoring= 'roc_auc', n_jobs= -1, verbose= 3)
random_search.fit(X_train, y_train)

random_search.best_params_

random_search.best_estimator_

xgb_classifier_pt = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bynode=1, colsample_bytree=0.4, gamma=0.2,
       learning_rate=0.1, max_delta_step=0, max_depth=15,
       min_child_weight=1, missing=np.nan, n_estimators=100, n_jobs=1,
       nthread=None, objective='binary:logistic', random_state=0,
       reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
       silent=None, subsample=1, verbosity=1)

xgb_classifier_pt.fit(X_train, y_train)
y_pred_xgb_pt = xgb_classifier_pt.predict(X_test)

accuracy_score(y_test, y_pred_xgb_pt)

"""# Confusion Matrix"""

cm = confusion_matrix(y_test, y_pred_xgb_pt)
plt.title('Heatmap of Confusion Matrix', fontsize = 15)
sns.heatmap(cm, annot = True)
plt.show()

"""# Classification Report of Model"""

print(classification_report(y_test, y_pred_xgb_pt))

"""# Cross-validation of the ML model"""

from sklearn.model_selection import cross_val_score
cross_validation = cross_val_score(estimator = xgb_model_pt2, X = X_train_sc, y = y_train, cv = 10)
print("Cross validation of XGBoost model = ",cross_validation)
print("Cross validation of XGBoost model (in mean) = ",cross_validation.mean())
from sklearn.model_selection import cross_val_score
cross_validation = cross_val_score(estimator = xgb_classifier_pt, X = X_train_sc,y = y_train, cv = 10)
print("Cross validation accuracy of XGBoost model = ", cross_validation)
print("\nCross validation mean accuracy of XGBoost model = ", cross_validation.mean())

"""# Save the Machine Learning model"""

## Pickle
import pickle

# save model
pickle.dump(xgb_classifier_pt, open('breast_cancer_detector.pickle', 'wb'))

# load model
breast_cancer_detector_model = pickle.load(open('breast_cancer_detector.pickle', 'rb'))

# predict the output
y_pred = breast_cancer_detector_model.predict(X_test)

# confusion matrix
print('Confusion matrix of XGBoost model: \n',confusion_matrix(y_test, y_pred),'\n')

# show the accuracy
print('Accuracy of XGBoost model = ',accuracy_score(y_test, y_pred))