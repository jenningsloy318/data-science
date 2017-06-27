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
plt.plot(num_trials,avgs)
plt.title=("Dice trials")
plt.xlabel("Number of trials")
plt.ylabel("Average")
plt.grid(True)
plt.show()