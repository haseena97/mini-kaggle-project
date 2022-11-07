# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 13:28:47 2022

@author: Acer
"""
# compare lambda dgn equation biasa
a = (lambda x : x*x*x)(10)
print (a)

x = 10
a = x*x*x
print (a)

# Example 2: dataframe
import pandas as pd
df=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['Jeremy','Frank','Janet','Ryan','Mary'],
    'age':[20,25,15,10,30],
    'income':[4000,7000,200,0,10000]
})
print(df)
# Error: We recorded ages with a difference of 3 years.
# To remove this error from the dataframe, we have to add 3 years to every person’s age
# Use apply() calls the lambda function 
# applies it to every row or column of the dataframe
# returns a modified copy of the dataframe
df['age']=df.apply(lambda x: x['age']+3,axis=1) #axis=1 apply dekat each row of 'Age'
print(df) #kalau axis=0 then apply kat each column
list(filter(lambda x: x>18,df['age'])) # bagi list yg filterkan age>18
df['income']=list(map(lambda x: int(x+x*0.2),df['income']))
# kalau x buat int kat dpn jadi error
# df['income']=df.apply(lambda x: [x['income']+[x['income']*0.2]],axis=1) 
print(df)
# nak categorize people into adult/child --create new column
df['category']=df['age'].apply(lambda x: 'Adult' if x>=18 else 'Child')
print(df)
df['status']=df['income'].apply(lambda x: 'Poor' if x<=10000 else 'Rich')
print(df)
