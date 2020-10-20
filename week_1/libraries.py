#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:05:19 2020

@author: kevinmenglin
"""

import pandas as pd
import numpy as np

#numpy basics
#first, demonstrate all the neat things on the upper right

a = np.array(['a',3,'b'])
b = np.array([(1.5,2,3), (4,5,6)])

b.shape

b[:,2]
b[1,:]

np.zeros((3,4))

np.ones((2,3))

#how to make a dataframe
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#reading in data
breast_cancer=pd.read_csv('breast-cancer-wisconsin-data.csv')
breast_cancer.dtypes

#view data
breast_cancer.head()
breast_cancer.head(6)
breast_cancer.tail()

breast_cancer.describe()

#selecting data

#select by whole rows or columns
breast_cancer.Outcome
breast_cancer[0:3]

#by position
breast_cancer.iloc[0:3,0:4]

#using row or column names
df.loc[:,['A','C']]

#using booleans
breast_cancer[breast_cancer.Outcome!='N']
breast_cancer[breast_cancer.Outcome.isin(['A','R'])]
