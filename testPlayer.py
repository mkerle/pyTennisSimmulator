from Player import Player
import random

p1 = Player('Mitch', lambda : random.gauss(0.629, 0.108), lambda : random.gauss(0.368, 0.094))

print(p1.getServiceRandValue())
print(p1.getReturnRandValue())

