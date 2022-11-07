
import pandas as pd
import seaborn as sns
# Read data into Python
house = pd.read_csv("C:\\Users\Acer\Downloads\Kaggle dataset\house.csv")
#list out all headers
house.columns
# 1. Analyse dependant variable - House Price
#Exploratory Data Analysis
#describe for all columns
house.describe()
#describe for Sale Price only
house.SalePrice.describe()

#Third moment business decision
house.SalePrice.skew()

#Fourth moment business decision
house.SalePrice.kurt()

#Graphical Representation
import matplotlib.pyplot as plt # mostly used for visualization purposes 
import numpy as np

plt.hist(house.SalePrice) #histogram
sns.distplot(house.SalePrice) #histogram+line
plt.boxplot(house.SalePrice) #boxplot

#correlation matrix - heatmap
corrmat = house.corr()
f, ax = plt.subplots(figsize=(12, 12))
sns.heatmap(corrmat, vmax=.8, square=True);

#saleprice correlation matrix utk compare dgn SalePrice
k = 10 #number of variables for heatmap
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(house[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()

#scatterplot correlation matrix utk selected columns
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt', 'MasVnrArea']
sns.pairplot(house[cols], size = 2.5)
plt.show();
#plot correlation between 2 column
sns. regplot(x=house['YearBuilt'], y=house['MasVnrArea'])
sns. regplot(x=house[''], y=house['YearBuilt'])
#Handle missing data dlm semua variable
total = house.isnull().sum().sort_values(ascending=False)
percent = (house.isnull().sum()/house.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)
# semua boleh buang kecuali electric sbb semua relate dgn domain yg kita ada