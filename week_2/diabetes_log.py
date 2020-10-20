#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# matplotlib inline

diabetes = pd.read_csv('desktop//diabetes.csv')

print(diabetes.columns)


# In[ ]:


diabetes.head()
print("dimension of diabetes data: {}".format(diabetes.shape))


# In[ ]:


print(diabetes.groupby('Outcome').size())


# In[ ]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'],
                                                    diabetes['Outcome'], stratify=diabetes['Outcome'], 
                                                    random_state=66)


# In[ ]:


from sklearn.linear_model import LinearRegression
logreg = LogisticRegression().fit(X_train, y_train)
print("Training set score: {:.3f}".format(logreg.score(X_train, y_train)))
print("Test set score: {:.3f}".format(logreg.score(X_test, y_test)))


# In[ ]:


logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
print("Training set accuracy: {:.3f}".format(logreg100.score(X_train, y_train)))
print("Test set accuracy: {:.3f}".format(logreg100.score(X_test, y_test)))


# In[ ]:


from sklearn import metrics 
confusionMatrix=metrics.confusion_matrix(y_test,predictions)
confusionMatrix


# In[ ]:


print('True Positive Rate:', confusionMatrix[1,1]/sum(confusionMatrix[1,:]))
print('False Discovery Rate:',confusionMatrix[0,1]/sum(confusionMatrix[:,1]))

