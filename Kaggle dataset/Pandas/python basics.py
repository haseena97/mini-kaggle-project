# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 07:57:05 2022

@author: Acer
"""

x = 'Hello world'
x[4]
x[-4]

tuple1=("A","B","C" )# what is the result of the following operation tuple1[-1]?
tuple1[-1]

tupleA=((11,12),[21,22])
tupleA[1]
tupleA[0][1]
tupleA[1][1]
'1,2,3,4'
'1,2,3,4'.split(',')

V={'A','B'}
V.add('C')

x="Go"

if(x=="Go"):

    print('Go')

else:

    print('Go ')

print('Mike')

for n in range(3):   

    print(n)
    
for n in range(3):

    print(n+1)


x = 1
y =2
class Points(object):            #x=1 y=2

    def __init__(self,x,y):

        self.x=x

        self.y=y

def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points(1,2)

p1.print_point()

sum(6,4,9),
sum([1,2,3])
len(["hello",91, 92, 93])
def maximum(x, y): 
    if x > y: return x
    elif x == y: return 'The numbers are equal' 
    else:
        return y 
    print(maximum(5, 13))
y = 2 
z = lambda x: x * y print z(7)
import re
w = re.compile('[A-Za-z]+') 
w.findall('we have training today')
Object.iloc[:,1:20]
print("python EASY".capitalize())
print (9/2)
