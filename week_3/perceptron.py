import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')
X = np.vstack((np.array(data['X1']), np.array(data['X2']))).T
y = np.array(data['y'])
steps = 0
mistakes = 1
w = np.array([1.0, -1.0])
n = y.shape[0]

while mistakes > 0:
    mistakes = 0
    for i in range(n):
        steps += 1
        """
        Fill in matplotlib code here
        """
        if np.inner(w,X[i])*y[i] < 0:
            mistakes += 1
            w += y[i]*X[i]