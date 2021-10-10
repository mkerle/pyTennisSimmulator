from Player import Player
from Set import Set

import random
import matplotlib.pyplot as plt
import numpy as np

p1 = Player('Soon Woo Kwon', lambda : random.gauss(0.629, 1), lambda : random.gauss(0.368, 1))
p2 = Player('Novak Djokovic', lambda : random.gauss(0.673, 0.5), lambda : random.gauss(0.422, 0.5))

results = { p1.name : { }, p2.name : { } }
for i in range(0, 10000):
    s = Set(p1, p2)
    s.playSet()

    p1Score = s.setScore[p1.name]['score']
    p2Score = s.setScore[p2.name]['score']

    sKey = '%d-%d' % (p1Score, p2Score)
    if (p2Score > p1Score):
        sKey = '%d-%d' % (p2Score, p1Score)
    
    if sKey not in results[s.getSetWinner()['object'].name]:
        results[s.getSetWinner()['object'].name][sKey] = 0

    results[s.getSetWinner()['object'].name][sKey] += 1


def getLabels(results):

    labels = []
    for p in results:
        for k in results[p]:
            if (k not in labels):
                labels.append(k)

    return sorted(labels)

def getValues(results, labels, player):

    vals = []
    for k in labels:
        if (k in results[player.name]):
            vals.append(results[player.name][k])
        else:
            vals.append(0)

    return vals


plt.rcdefaults()
fig, ax = plt.subplots()
width = 0.15

x = np.arange(len(getLabels(results)))
rects1 = ax.bar(x - width/2, getValues(results, getLabels(results), p1), width, label='%s Results' % (p1.name)) 
rects2 = ax.bar(x + width/2, getValues(results, getLabels(results), p2), width, label='%s Results' % (p2.name)) 

ax.set_ylabel('Wins')
ax.set_title('Set Wins')
ax.set_xticks(x)
ax.set_xticklabels(getLabels(results))
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

