#!/usr/bin/python
import random
from matplotlib import pyplot as plt

def random_variables_of_dice_roll():
    return random.randint(1, 7)


num_trials = range(100,10000,10)
avgs=[]
for num_trial  in num_trials:
    trials=[]
    for trial in range(num_trial):
        trials.append(random_variables_of_dice_roll())
    avgs.append(sum(trials)/float(num_trial))



fig,ax=plt.subplots()
ax.plot(num_trials,avgs)
ax.set_title("pic title")
ax.set_xlabel("xx")
ax.set_ylabel("yy")
fig.suptitle("supper title")
plt.show()