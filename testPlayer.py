from Player import Player
import random

p1 = Player('Mitch', lambda : random.gauss(0, 1))

print(p1.getRandValue())

