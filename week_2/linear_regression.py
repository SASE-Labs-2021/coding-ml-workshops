#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 09:16:31 2020

@author: kevinmenglin
"""
#import these, if you don't have them, email mengl003@umn.edu and I'll help you install them
import statsmodels.api as sm #for making linear models
import pandas as pd #so we can use pandas data frames to represent our csv data
from sklearn.model_selection import train_test_split  #for splitting our data into train-test sets
from sklearn import metrics #for calculating some model evaluation metrics
import matplotlib.pyplot as plt #for making plots


##QUICK NOTE: FEW PEOPLE MEMORIZE EVERY FUNCTION IN EVERY LIBRARY, EACH OF THESE LIBRARIES
##HAS ONLINE DOCUMENTATION THAT YOU CAN REFERENCE AND YOU CAN FIND EXAMPLES OF HOW TO USE THEM.
##ALSO, GOOGLE IS YOUR FRIEND. IF YOU DON'T KNOW HOW TO DO SOMETHING, JUST GOOGLE IT.
##THERE'S NO SHAME, MANY SOFTWARE ENGINEERS SAY THEY WOULD BE OUT OF A JOB IF THEY DIDN'T HAVE
##GOOGLE SO KEEP THAT IN MIND.

##ALSO, MAKE SURE YOUR WORK FOLDER (SEE TOP RIGHT TOOL BAR) IS SET TO THE FOLDER THAT CONTAINS
##THE NHANES DATA

#read and view the data as a pandas data frame object
data=pd.read_csv('NHANES.csv')
data.head()

#get rid of this unnecessary column
data=data.drop('Unnamed: 0',1)
data.head()

#view the dimensions of a pandas data frame
data.shape

#some summary statistics
data.describe()

#split the data to prepare for machine learning
y=data.LBDHDL
X=data.drop("LBDHDL",1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
#note, train_test_split returns a list
#when a function returns a list, you can assign each list element to multiple outputs
#it always outputs the data in the order that I show here, so name your variables accordingly

X_test.head()

#we make a linear regression model using only the BMI variable
basicModel=sm.OLS(endog=y_train,exog=sm.add_constant(X_train.BMXBMI))
resultBasic = basicModel.fit()

#get some information about our model
print(resultBasic.summary())

#give our model the test data, and let it predict
predictionsBasic=resultBasic.predict(sm.add_constant(X_test.BMXBMI))

#note, we introduce a new way to print lines here
print("Training R2:",resultBasic.rsquared) #get the training R-squared value
print("Test R2:",metrics.r2_score(y_test, predictionsBasic)) #test R-squared value
print("Training Mean Squared Error:", resultBasic.mse_resid) #training mean squared error
print("Test Mean Squared Error:",metrics.mean_squared_error(y_test, predictionsBasic)) #test mean squared error

#generate a residual plot
fig, ax = plt.subplots() #initialize the plot
#get the predicted values on my training data
trainPredictions=resultBasic.predict(sm.add_constant(X_train.BMXBMI))
#calculate the residual from my training data
residuals=y_train-trainPredictions
#plot
ax.plot(trainPredictions,residuals,'o')

##BECAUSE THE PLOTTING IS WEIRD, HIGHLIGHT AND RUN THESE LINES TOGETHER
fig, ax = plt.subplots()
ax.plot(trainPredictions,residuals,'o')

#try the modeling again but now using BMI and age
model=sm.OLS(endog=y_train,exog=sm.add_constant(X_train.iloc[:,[0,3]]))
#for a pandas data frame or numpy array, you can use 2 dimensional list indexing
#[row index, column index]

result = model.fit()
print(result.summary())

#evaluate this new model
predictions=result.predict(sm.add_constant(X_test.iloc[:,[0,3]]))
#notice, I give the same variables as I trained on

print("Training R2:",result.rsquared)
print("Test R2:",metrics.r2_score(y_test, predictions))
print("Training Mean Squared Error:", result.mse_resid)
print("Test Mean Squared Error:",metrics.mean_squared_error(y_test, predictions))

#make dummy variables
sex=pd.get_dummies(data.RIAGENDR,prefix='sex') #prefix is optional but helpful
sex.head()

#get rid of the male variable
sex=sex.iloc[:,0]
sex.head()

#drop the gender variable in the original data, add our new sex_female variable
data=data.drop('RIAGENDR',1)
data=data.join(sex)
data.head()

#make dummy variables for ethnicity and smoking and join them together
ETH=pd.get_dummies(data.RIDRETH1,prefix='ethnicity')
SMQ=pd.get_dummies(data.SMQ040,prefix='smoking')
add=ETH.join(SMQ)
add.head()

#drop a variable for each one of my original variables, use these as baselines
add=add.drop('ethnicity_Non-Hispanic White',1)
add=add.drop('smoking_Not at all',1)
add.head()

#make new data using these
dataNew=data.drop(['RIDRETH1','SMQ040'],1) #assign the data without the original smoke and
#ethnicity variable to 'dataNew'
dataNew=dataNew.join(add)
dataNew.head()

#re-run modeling
y=dataNew.LBDHDL
X=dataNew.drop("LBDHDL",1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
dataNew
model=sm.OLS(endog=y_train,exog=sm.add_constant(X_train))
result = model.fit()
print(result.summary())

#generate evaluation metrics
predictions=result.predict(sm.add_constant(X_test))
print("Training R2:",result.rsquared)
print("Test R2:",metrics.r2_score(y_test, predictions))
print("Training Mean Squared Error:", result.mse_resid)
print("Test Mean Squared Error:",metrics.mean_squared_error(y_test, predictions))

#residual plot
fig, ax = plt.subplots()
trainPredict=result.predict(sm.add_constant(X_train))
residuals=y_train-trainPredict
ax.plot(trainPredict,residuals,'o')

##BECAUSE THE PLOTTING IS WEIRD, HIGHLIGHT AND RUN THESE LINES TOGETHER
fig, ax = plt.subplots()
ax.plot(trainPredict,residuals,'o')

#here's a 'fun' exercise: I did a lot of code copy-pasting here. Could you shorten this script
#by making your own functions?

##example for making a dummy variable then updating the data set
def autoDummyUpdate(inputData, variableName):
    dummy=pd.get_dummies(inputData.loc[:,variableName])
    print(dummy)
    remove=input("Enter the name of the column you want to remove ")
    dummy=dummy.drop(remove,1)
    newData=inputData.drop(variableName,1)
    newData=newData.join(dummy)
    return(newData)
    