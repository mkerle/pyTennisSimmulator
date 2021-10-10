from Player import Player
from Point import Point
from Game import Game
from Set import Set
import random

p1 = Player('Soon Woo Kwon', lambda : random.gauss(0.629, 0.37), lambda : random.gauss(0.368, 0.32))
p2 = Player('Novak Djokovic', lambda : random.gauss(0.673, 0.337), lambda : random.gauss(0.422, 0.29))

set = Set(p1, p2)
set.playSet()

print(set.toString())