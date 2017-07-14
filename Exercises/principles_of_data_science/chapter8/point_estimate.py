import numpy as np 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

seed=np.random.seed(1234)
long_breaks=stats.poisson.rvs(loc=10, mu=60, size=3000)
short_breaks = stats.poisson.rvs(loc=10, mu=15, size=6000)
breaks = np.concatenate((long_breaks, short_breaks))
sample_breaks = np.random.choice(a = breaks, size=100)
employee_races = (["white"]*2000) + (["black"]*1000) + (["hispanic"]*1000) + (["asian"]*3000) +  (["other"]*3000)

print(breaks.mean() - sample_breaks.mean())

fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1)
ax1.set_title("Long Breaks")
ax2 = plt.subplot2grid((2, 2), (0, 1), colspan=1)
ax2.set_title("Short Breaks")
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
ax3.set_title("Overall Breaks")
pd.Series(long_breaks).hist(ax=ax1)
pd.Series(short_breaks).hist(ax=ax2)
pd.Series(breaks).hist(ax=ax3)


fig.suptitle("Point Estimate")
fig.tight_layout()
plt.show()