#!/usr/bin/python
from matplotlib import pyplot as plt
import numpy as np

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531, 742, 621]
friend_mean=np.mean(friends)
friend_median=np.median(friends)
friend_sd=np.std(friends)
print("Mean number of friends is %f" %friend_mean)
print("Median number of friends is %f" %friend_median)
print("The gap between maximun and least is %f"%(np.max(friends)-np.min(friends)))
print("The standard deviation is %f"%friend_sd)


fig,(ax1,ax2)=plt.subplots(1,2, sharey=False)
y_pos = range(len(friends))

z_scores = []
for friend in friends:
    z = (friend - friend_mean)/friend_sd
    z_scores.append(z)


ax1.bar(y_pos, friends)
ax1.bar(y_pos, friends)
ax1.plot((0, 25), (789, 789), 'b-')
ax1.plot((0, 25), (789+425, 789+425), 'g-')
ax1.plot((0, 25), (789-425, 789-425), 'r-')
ax1.set_xlabel("Person ID")
ax1.set_ylabel("Friends")
ax1.set_title("Frieds of FB")

ax2.bar(y_pos,z_scores)
ax2.set_title("Relative value")
ax2.set_xlabel("Person ID")
ax2.set_ylabel("Measure of variation")
ax2.plot((0, 25), (1, 1), 'g-')
ax2.plot((0, 25), (0, 0), 'b-')
ax2.plot((0, 25), (-1, -1), 'r-')
fig.suptitle("Analysis of Friends")

plt.show()