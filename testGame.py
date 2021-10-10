from Player import Player
from Point import Point
from Game import Game
import random

p1 = Player('Mitch', lambda : random.gauss(0, 1))
p2 = Player('Alisa', lambda : random.gauss(0, 0.2))

game = Game(p1, p2)
game.playGame()

print(game.toString())

