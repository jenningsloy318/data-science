#!/usr/bin/python
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531, 742, 621]
happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2, .8, 1, .6, .2, .7, .5, .3, .1, 0, .3, 1]
friend_mean=np.mean(friends)
friend_median=np.median(friends)
friend_sd=np.std(friends)
print("Mean number of friends is %f" %friend_mean)
print("Median number of friends is %f" %friend_median)
print("The gap between maximun and least is %f"%(np.max(friends)-np.min(friends)))
print("The standard deviation is %f"%friend_sd)


df = pd.DataFrame({'friends':friends, 'happiness':happiness})
df_scaled = pd.DataFrame(preprocessing.scale(df), columns = ['friends_scaled', 'happiness_scaled'])
print(df.corr())

within_1_std=df_scaled[(df_scaled['friends_scaled'] <= 1) & (df_scaled['friends_scaled'] >= -1)].shape[0]
percentage_within_1_std=within_1_std/float(df_scaled.shape[0])
print(percentage_within_1_std)

within_2_std=df_scaled[(df_scaled['friends_scaled'] <= 2) & (df_scaled['friends_scaled'] >= -2)].shape[0]
percentage_within_2_std=within_2_std/float(df_scaled.shape[0])
print(percentage_within_2_std)

within_3_std=df_scaled[(df_scaled['friends_scaled'] <= 3) & (df_scaled['friends_scaled'] >= -3)].shape[0]
percentage_within_3_std=within_3_std/float(df_scaled.shape[0])
print(percentage_within_3_std)

#fig,((ax1,ax2),(ax3,_))=plt.subplots(2,2, sharey=False)
y_pos = range(len(friends))

z_scores = []
for friend in friends:
    z = (friend - friend_mean)/friend_sd
    z_scores.append(z)

fig = plt.figure(figsize=(8, 6))

ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=1)
ax1.bar(y_pos, friends)
ax1.plot((0, 25), (789, 789), 'b-')
ax1.plot((0, 25), (789+425, 789+425), 'g-')
ax1.plot((0, 25), (789-425, 789-425), 'r-')
ax1.set_xlabel("Person ID")
ax1.set_ylabel("Friends")
ax1.set_title("Frieds of FB")

ax2 = plt.subplot2grid((2, 2), (0, 1), colspan=1)
ax2.bar(y_pos,z_scores)
ax2.set_title("Relative value")
ax2.set_xlabel("Person ID")
ax2.set_ylabel("Measure of variation")
ax2.plot((0, 25), (1, 1), 'g-')
ax2.plot((0, 25), (0, 0), 'b-')
ax2.plot((0, 25), (-1, -1), 'r-')

ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
df_scaled.plot(kind='scatter', x = 'friends_scaled', y = 'happiness_scaled',ax=ax3)
ax3.set_xlabel("friends_scaled")
ax3.set_ylabel("happiness_scaled")
ax3.set_title("Friends_happiness")


fig.suptitle("Analysis of Friends")

fig.tight_layout()

plt.show()