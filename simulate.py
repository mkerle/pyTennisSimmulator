from Player import Player
from Set import Set

import random
import matplotlib.pyplot as plt
import numpy as np

p1 = Player('Mitch', lambda : random.gauss(0, 1))
p2 = Player('Alisa', lambda : np.random.default_rng().normal(0, 1, None))

results = { }
for i in range(0, 1000):
    s = Set(p1, p2)
    s.playSet()

    p1Score = s.setScore[p1.name]['score']
    p2Score = s.setScore[p2.name]['score']

    sP1Key = '%d-%d-%s' % (p1Score, p2Score, p1.name)
    sP2Key = '%d-%d-%s' % (p2Score, p1Score, p2.name)

    if sP1Key not in results:
        results[sP1Key] = 0

    results[sP1Key] += 1

    if sP2Key not in results:
        results[sP2Key] = 0

    results[sP2Key] += 1

def getLabels(results, player):

    labels = []
    for k in results.keys():
        if (player.name in k):
            labels.append(k)

    return sorted(labels)

def getValues(results, labels):

    vals = []
    for k in labels:
        vals.append(results[k])

    return vals


plt.rcdefaults()
fig, ax = plt.subplots()
width = 0.15

x = np.arange(len(getLabels(results, p1)))
rects1 = ax.bar(x - width/2, getValues(results, getLabels(results, p1)), width, label='P1 Results') 
rects2 = ax.bar(x + width/2, getValues(results, getLabels(results, p2)), width, label='P2 Results') 

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(getLabels(results, p1))
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

