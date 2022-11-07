# load numpy
import numpy as np
# load pandas
import pandas as pd

create a numpy array with 10 integers.
 We will use NumpPy’s random module to generate random numbers in between 25 and 200. 
 We will also use random seed to reproduce the random numbers.

# set a random seed to reproduce
np.random.seed(123)
# create 10 random integers  
x = np.random.randint(low=25, high=200, size=10)
x = np.sort(x)
print(x) #[ 42  82  91 108 121 123 131 134 148 151]
# digitize examples
we use 50 as threshold to bin our data into two categories. 
One with values less than 50 are in the 0 category.
the ones above 50 are in the 1 category.

np.digitize(x,bins=[50])

# less than 50 = 0, 50-100 = 1, 100 above = 2
np.digitize(x,[50,100])

# less than 25 = 0, 25-50 = 1, 50-100 = 2, more than 100 = 3
np.digitize(x,[25,50,100])

# Discretize or Bin with Pandas cut() function
df = pd.DataFrame({"height":x})
df.head()
   height
0      42
1      82
2      91
3     108
4     121
# need to specify both lower and upper end of the bins for categorizing.
0-25 = 0, 25-50 = 1, 50-100 = 2, 100-200 = 3
df['binned']=pd.cut(x=df['height'], bins=[0,25,50,100,200])
df.head()
   height      binned
0      42    (25, 50]
1      82   (50, 100]
2      91   (50, 100]
3     108  (100, 200]
4     121  (100, 200]
            
df['height_bin']=pd.cut(x = df['height'],
                        bins = [0,25,50,100,200], 
                        labels = [0, 1, 2,3]) # utk label encode terus
df            
   height      binned height_bin
0      42    (25, 50]          1
1      82   (50, 100]          2
2      91   (50, 100]          2
3     108  (100, 200]          3
4     121  (100, 200]          3
5     123  (100, 200]          3
6     131  (100, 200]          3
7     134  (100, 200]          3
8     148  (100, 200]          3
9     151  (100, 200]          3
            
# we can use more descriptive categories like this as well
df['height_bin']=pd.cut(x=df['height'], bins=[0,25,50,100,200], 
                        labels=["very short", " short", "medium","tall"])
print(df.head())
   height      binned height_bin
0      42    (25, 50]      short
1      82   (50, 100]     medium
2      91   (50, 100]     medium
3     108  (100, 200]       tall
4     121  (100, 200]       tall