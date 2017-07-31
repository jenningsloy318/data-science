#!/usr/bin/python

import pandas as pd 
import matplotlib.pyplot as plt

hours_tv_watched = [0, 0, 0, 1, 1.3, 1.4, 2, 2.1, 2.6, 3.2, 4.1, 4.4, 4.4, 5]
work_performance = [87, 89, 92, 90, 82, 80, 77, 80, 76, 85, 80, 75, 73, 72]
fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot2grid((2, 1), (0, 0), colspan=1)
ax2 = plt.subplot2grid((2, 1), (1, 0), colspan=1)

df = pd.DataFrame({'hours_tv_watched':hours_tv_watched, 'work_performance':work_performance})
print(df.corr())
df.plot(title="Scatter plot",x='hours_tv_watched', y='work_performance',ax=ax1, kind='scatter')
df.plot(title="line plot",x='hours_tv_watched', y='work_performance',ax=ax2, kind='line')
fig.tight_layout()
plt.show()