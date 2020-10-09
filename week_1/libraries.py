#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:05:19 2020

@author: kevinmenglin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#numpy basics
#first, demonstrate all the neat things on the upper right

a = np.array(['a',3,'b'])
b = np.array([(1.5,2,3), (4,5,6)])

b.ndim

b.shape

b.size

b.dtype

a.dtype

b[:,2]
b[1,:]

np.zeros((3,4))

np.ones((2,3,4))

#np.empty((2,3))


#how to make a series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
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
breast_cancer.index
df.index
breast_cancer.columns

df.to_numpy()
breast_cancer.to_numpy()

breast_cancer.describe()

breast_cancer.T

df.sort_index(axis=1,ascending=False)
df.sort_index(axis=0,ascending=True)

df.sort_values(by='B',ascending=False)
#selecting data

#select by whole rows or columns
breast_cancer.Outcome
breast_cancer[0:3]
df[df.index[0]:df.index[2]]

#by position
breast_cancer.iloc[0,:]
breast_cancer.iloc[:,0:5]
breast_cancer.iloc[0:3,0:4]

#using row or column names
df.loc[df.index[0]:df.index[2],['A','C']]
df.loc[df.index[[0,3]],df.columns[[0,3]]]

#using booleans
breast_cancer[breast_cancer.Outcome!='N']
breast_cancer[breast_cancer=='R']
breast_cancer.Outcome.isin(['A','R'])
breast_cancer[breast_cancer.Outcome.isin(['A','R'])]
#plotting

