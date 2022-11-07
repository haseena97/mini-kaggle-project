# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:41:17 2022

@author: Acer
"""

import pandas as pd
house = pd.read_csv("C:\\Users\\Acer\\Downloads\\Kaggle dataset\\boston\\boston.csv")
# add header to pandas dataframe
df = pd.read_csv("path/to/file.txt", sep='\t')
headers =  ['CRIM',"ZN", "INDUS", "CHAS", "NOX", 'RM', 'AGE', 'DIS','RAD', 'TAX', 'PTRATIO','B','LSTAT', 'MEDV']

# Multilinear Regression

house.describe()
house.head
# check missing values
house.isnull().sum()
# EDA
# Scatter plot between the variables along with histograms
import seaborn as sns
import matplotlib.pyplot as plt
# tgk distribution utk dependant variable
sns.distplot(house.MEDV)

sns.boxplot(house.MEDV)                             
# Correlation matrix 
sns.pairplot(house.iloc[:,:]) 
house.corr()
# variable byk sgt so better tgk heatmap yg ada correlation matrix
correlation_matrix = house.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True)

#scatterplot correlation matrix utk selected columns
sns.set()
cols = ['MEDV', 'INDUS', 'NOX', 'RM', 'TAX', 'PTRATIO', 'LSTAT']
sns.pairplot(house[cols], size = 2.5)
plt.show();
# preparing model considering all the variables 
import statsmodels.formula.api as smf # for regression model
         
ml1 = smf.ols('MEDV ~ INDUS+NOX+RM+TAX+PTRATIO+LSTAT', data=house).fit() # simple regression model

# Summary
ml1.summary()

# calculating VIF's values of independent variables
rsq_hp = smf.ols('INDUS ~ NOX+RM+TAX+PTRATIO+LSTAT', data=house).fit().rsquared  
vif_hp = 1/(1-rsq_hp) 

rsq_wt = smf.ols('NOX ~ INDUS+RM+TAX+PTRATIO+LSTAT', data=house).fit().rsquared  
vif_wt = 1/(1-rsq_wt)

rsq_vol = smf.ols('RM ~ INDUS+NOX+TAX+PTRATIO+LSTAT', data=house).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 

rsq_sp = smf.ols('TAX ~ INDUS+NOX+RM+PTRATIO+LSTAT', data=house).fit().rsquared  
vif_sp = 1/(1-rsq_sp) 

rsq_PO = smf.ols('PTRATIO ~ INDUS+NOX+RM+TAX+LSTAT', data=house).fit().rsquared  
vif_PO = 1/(1-rsq_PO) 

rsq_LT = smf.ols('LSTAT ~ INDUS+NOX+RM+TAX+PTRATIO', data=house).fit().rsquared  
vif_LT = 1/(1-rsq_LT) 
# Storing vif values in a data frame
d1 = {'Variables':['INDUS','NOX','RM','TAX','PTRATIO','LSTAT'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp,vif_PO,vif_LT]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
#kalau nak write dalam excel file (nak header=true,kalau x nak header=None,kalau x nak index=False)sep=separator
Vif_frame.to_csv('C:\\Users\\Acer\\Downloads\\Cars\\test2.csv',header=True,index=False,sep=',',mode='w')
#kalau nak write dalam txt file (nak header=true,kalau x nak header=None,kalau x nak index=False),\t bagi sengkang
Vif_frame.to_csv('C:\\Users\\Acer\\Downloads\\Cars\\test2.txt',header=True,index=False,sep='\t',mode='w')

# scatter plot
import numpy as np
plt.scatter(x=(house['INDUS']),y=house['MEDV'],color='blue')
plt.scatter(x=(house['RM']),y=house['MEDV'],color='red')
plt.scatter(x=np.log(house['TAX']),y=house['MEDV'],color='yellow')
plt.scatter(x=(house['PTRATIO']),y=house['MEDV'],color='blue')
plt.scatter(x=(house['LSTAT']),y=house['MEDV'],color='black')
plt.legend(loc='upper left')
plt.show()

# final model (letak log dekat TAX & polynomial LSTAT)
final_ml= smf.ols('MEDV ~ INDUS+RM+np.log(TAX)+PTRATIO+LSTAT+I(LSTAT*LSTAT)', data = house).fit()
final_ml.summary()


### Splitting the data into train and test data 
from sklearn.model_selection import train_test_split
house_train, house_test  = train_test_split(house, test_size = 0.3) # 30% test data

# preparing the model on train data 
model_train = smf.ols("MEDV ~ INDUS+RM+np.log(TAX)+PTRATIO+LSTAT+I(LSTAT*LSTAT)", data = house_train).fit()

# prediction on test data set 
test_pred = model_train.predict(house_test)

# test residual values 
test_resid  = test_pred - house_test.MEDV

# RMSE value for test data 
test_rmse = np.sqrt(np.mean(test_resid*test_resid)) 
test_rmse


# train_data prediction
train_pred = model_train.predict(house_train)

# train residual values 
train_resid  = train_pred - house_train.MEDV

# RMSE value for train data 
train_rmse = np.sqrt(np.mean(train_resid * train_resid))
train_rmse
