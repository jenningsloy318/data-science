#!/usr/bin/python
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
results = []
for n in range(1,10000):
    nums=np.random.randint(low=1,high=10, size=n)# choose n numbers between 1 and 10
    mean = nums.mean()                              # find the average of these numbers
    results.append(mean)                            # add the average to a running list
#print("How large is the list results?: it is %d.\n"%len(results))
df = pd.DataFrame({ 'means' : results})
#print(df.head())
df.plot(title="Law of Large Numbers")
plt.xlabel("Number of throws in sample")
plt.ylabel("Average Of Sample")
plt.show()
