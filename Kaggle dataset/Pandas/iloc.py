# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 06:40:37 2022

@author: Acer
"""
import pandas as pd
df = pd.DataFrame({'A':[1,2,3],
                   'B':[4,5,6],
                   'C':[7,8,9],
                   'D':[1,3,5],
                   'E':[5,3,6],
                   'F':[7,4,3]})
# pd.DataFrame({'column name':[1,2,3],'B':[4,5,6]}
print (df)
print(df.iloc[:, :-1]) # [semua row, semua column sampai sebelum yg last]
print(df.iloc[:, 5]) 
print(df.iloc[:, 1:5])
print(df.iloc[:, 1:5]) # semua row, column #1 sampai sebelum column #5 = 1-4 
X = animal.iloc[:,1:6] # semua row, column #1 sampai sebelum column #6 = 1-5
y = animal.iloc[:,17] # semua row dekat column nombor 17
Python list slicing syntax : for a:b it will get a and everything upto but not including b.
 a: will get a and everything after it.
 :b will get everything before b but not b. 
 The list index of -1 refers to the last element. 
 :-1 adheres to this gets everything before the last element but not the last element. 




# Python slicing
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

# step 
a[start:stop:step] # start through not past stop, by step
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed