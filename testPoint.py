from Player import Player
from Point import Point
import random

p1 = Player('Mitch', lambda : random.gauss(0, 1))
p2 = Player('Alisa', lambda : random.gauss(0, 0.2))

point = Point(p1, p2)
point.playPoint()
print(point.getPointWinner().name)
