#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:01:42 2020

@author: kevinmenglin
"""

import pandas as pd
import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


#read in the data

data=pd.read_csv('diabetes.csv')
data.columns


y=data.Outcome
X=data.drop('Outcome',1)

#show how to read a function documentation
labelencoder_X_1 = LabelEncoder()
y = labelencoder_X_1.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)



sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from keras.models import Sequential
from keras.layers import Dense, Dropout


classifier = Sequential()
classifier.add(Dense(output_dim=5, activation='sigmoid', input_dim=8))

classifier.add(Dense(output_dim=3, activation='sigmoid'))

classifier.add(Dense(output_dim=1,activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

classifier.fit(X_train, y_train, batch_size=10, nb_epoch=20)

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

_, accuracy = classifier.evaluate(X_test,y_test)
print(accuracy)

