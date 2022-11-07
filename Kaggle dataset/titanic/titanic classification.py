# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:51:40 2022

@author: Acer
"""
import numpy as np
import pandas as pd
training = pd.read_csv("C:\\Users\\Acer\\Downloads\\Kaggle dataset\\titanic\\train.csv")
test = pd.read_csv("C:\\Users\\Acer\\Downloads\\Kaggle dataset\\titanic\\test.csv")
# we will be exclusively working with the Training set.
# We will be validating based on data from the training set as well.
# For our final submissions, we will make predictions based on the test set.
training['train_test'] = 1
test['train_test'] = 0
test['Survived'] = np.NaN # test data xde column survive so letak Nan
all_data = pd.concat([training,test]) # concat = merge dlm satu dataframe
all_data.columns # nak selaraskan train dgn test
# Understand nature of the data .info() .describe()
training.describe()
training.info()


# Value counts 
# Missing data 
training.isnull().sum()
#quick look at our data types & null counts 
training.info()
#quick way to separate numeric columns -- tgk yg mana yg valid
training.describe().columns
# look at numeric and categorical values separately 
df_num = training[['Age','SibSp','Parch','Fare']]
df_cat = training[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]
# How is the distribution for numerical values
import seaborn as sns
import matplotlib.pyplot as plt
# Histograms and boxplots
#distributions for all numeric variables (df_num) --histogram
for i in df_num.columns:
    plt.hist(df_num[i])
    plt.title(i)
    plt.show()
#distributions for all numeric variables (df_num) --boxplot
for i in df_num.columns:
    plt.boxplot(df_num[i])
    plt.title(i)
    plt.show()
 
# Correlation between the metrics 
print(df_num.corr())
sns.heatmap(df_num.corr())
# compare survival rate across Age, SibSp, Parch, and Fare (numerical variables)
pd.pivot_table(training, index = 'Survived', values = ['Age','SibSp','Parch','Fare'])
# Distribution for categorical variable
# Bar plot
for i in df_cat.columns:
    sns.barplot(df_cat[i].value_counts().index,df_cat[i].value_counts()).set_title(i)
    plt.show()
    
# Comparing survival and each of these categorical variables (mcm Excel)
# index = row, values = brpa org yg kita kira pakai column yg xde missing values
print(pd.pivot_table(training, index = 'Survived', columns = 'Pclass' , values = 'Ticket', aggfunc ='count'))
print()
print(pd.pivot_table(training, index = 'Survived', columns = 'Sex', values = 'Ticket' ,aggfunc ='count'))
print()
print(pd.pivot_table(training, index = 'Survived', columns = 'Embarked', values = 'Ticket' ,aggfunc ='count'))
# Explore interesting themes 
    # Wealthy survive? 
    # By location 
    # Age scatterplot with ticket price 
    # Young and wealthy Variable? 
    # Total spent? 
# Feature engineering 
df_cat.Cabin
# x=0 kalau missing value, pecahkan setiap cabin sbb nak kira siapa sewa >1 cabin
training['cabin_multiple'] = training.Cabin.apply(lambda x: 0 if pd.isna(x) else len(x.split(' ')))

print(training['cabin_multiple'])
# summarize ikut survived/not survived
training['cabin_multiple'].value_counts()
pd.pivot_table(training, index = 'Survived', columns = 'cabin_multiple', values = 'Ticket' ,aggfunc ='count')
#creates categories based on the cabin letter (n stands for null)
#in this case we will treat null values like it's own category
training['cabin_adv'] = training.Cabin.apply(lambda x: str(x)[0]) #strip the letter from letter number combo
print(training['cabin_adv']) # kluar huruf je
#comparing surivial rate by cabin
print(training.cabin_adv.value_counts())
pd.pivot_table(training,index='Survived',columns='cabin_adv', values = 'Name', aggfunc='count')
#understand ticket values better 
#numeric vs non numeric ticket
training['numeric_ticket'] = training.Ticket.apply(lambda x: 1 if x.isnumeric() else 0) # ada yg semua nombor
training['ticket_letters'] = training.Ticket.apply(lambda x: ''.join(x.split(' ')[:-1]).replace('.','').replace('/','').lower() if len(x.split(' ')[:-1]) >0 else 0)
training['numeric_ticket'].value_counts()
#lets us view all rows in dataframe through scrolling. This is for convenience 
pd.set_option("max_rows", None)
training['ticket_letters'].value_counts()
#difference in numeric vs non-numeric tickets in survival rate 
pd.pivot_table(training,index='Survived',columns='numeric_ticket', values = 'Ticket', aggfunc='count')
#survival rate across different ticket types 
pd.pivot_table(training,index='Survived',columns='ticket_letters', values = 'Ticket', aggfunc='count')
# feature engineering on person's title
training.Name.head(50) # Split cth: Masselmani, Mrs. Fatima
training['name_title'] = training.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
#mr., ms., master. etc
print(training['name_title'])
training['name_title'].value_counts()
pd.pivot_table(training,index='Survived',columns='name_title', values = 'Ticket', aggfunc='count')

#create all categorical variables that we did above apply for both training and test sets = alldata
all_data['cabin_multiple'] = all_data.Cabin.apply(lambda x: 0 if pd.isna(x) else len(x.split(' ')))
all_data['cabin_adv'] = all_data.Cabin.apply(lambda x: str(x)[0])
all_data['numeric_ticket'] = all_data.Ticket.apply(lambda x: 1 if x.isnumeric() else 0)
all_data['ticket_letters'] = all_data.Ticket.apply(lambda x: ''.join(x.split(' ')[:-1]).replace('.','').replace('/','').lower() if len(x.split(' ')[:-1]) >0 else 0)
all_data['name_title'] = all_data.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
# Impute data with mean for fare and age (Should also experiment with median)
#impute nulls for continuous data 
#all_data.Age = all_data.Age.fillna(training.Age.mean())
all_data.Age = all_data.Age.fillna(training.Age.median())
#all_data.Fare = all_data.Fare.fillna(training.Fare.mean())
all_data.Fare = all_data.Fare.fillna(training.Fare.median())

#drop null 'embarked' rows. Only 2 instances of this in training and 0 in test 
all_data.dropna(subset=['Embarked'],inplace = True)
#tried log norm of sibsp (not used)
all_data['norm_sibsp'] = np.log(all_data.SibSp+1)
all_data['norm_sibsp'].hist()

# log norm of fare (used)
all_data['norm_fare'] = np.log(all_data.Fare+1)
all_data['norm_fare'].hist()
# To compare normalized dgn yang belum
all_data['Fare'].hist()

# converted fare to category for pd.get_dummies()
all_data.Pclass = all_data.Pclass.astype(str)

#created dummy variables from categories (also can use OneHotEncoder)
all_dummies = pd.get_dummies(all_data[['Pclass','Sex','Age','SibSp','Parch','norm_fare','Embarked','cabin_adv','cabin_multiple','numeric_ticket','name_title','train_test']])

#Split to train test again
X_train = all_dummies[all_dummies.train_test == 1].drop(['train_test'], axis =1)
X_test = all_dummies[all_dummies.train_test == 0].drop(['train_test'], axis =1)


y_train = all_data[all_data.train_test==1].Survived
y_train.shape
  
# Scaling?
# Scale features data 
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
all_dummies_scaled = all_dummies.copy()
all_dummies_scaled[['Age','SibSp','Parch','norm_fare']]= scale.fit_transform(all_dummies_scaled[['Age','SibSp','Parch','norm_fare']])
all_dummies_scaled

X_train_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 1].drop(['train_test'], axis =1)
X_test_scaled = all_dummies_scaled[all_dummies_scaled.train_test == 0].drop(['train_test'], axis =1)

y_train = all_data[all_data.train_test==1].Survived
# Model Baseline 
# Model comparison with CV 
best_rf.fit(X_train_scaled, y_train)
y_hat_rf = best_rf.predict(X_test_scaled).astype(int)
final_data = {'PassengerId': test.PassengerId, 'Survived': y_hat_rf}
submission.to_csv('submission_rf.csv', index =False)
submission = pd.DataFrame(data=final_data)