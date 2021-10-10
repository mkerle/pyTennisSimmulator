from Player import Player
from Point import Point
from Game import Game
from Set import Set
import random

p1 = Player('Mitch', lambda : random.gauss(0, 1))
p2 = Player('Alisa', lambda : random.gauss(0, 0.2))

set = Set(p1, p2)
set.playSet()

print(set.toString())