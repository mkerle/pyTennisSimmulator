from Player import Player
from Game import Game

class Set(object):

    def __init__(self, player1, player2):

        self.p1 = player1
        self.p2 = player2

        self.games = []

        self.setScore = { self.p1.name : { 'score' : 0, 'object' : self.p1 }, self.p2.name : { 'score' : 0, 'object' : self.p2 } }

    def playSet(self):

        while (not self.isSetComplete()):
            game = Game(self.p1, self.p2)
            game.playGame()

            self.updateSetScore(game.getGameWinner()['object'], game.getGameLooser()['object'])

            self.games.append(game)

    def updateSetScore(self, winner, looser):

        self.setScore[winner.name]['score'] += 1

    def isSetComplete(self):

        isComplete = False
        for player in self.setScore:
            if (self.setScore[player]['score'] == 6):
                isComplete = True

        return isComplete

    def getSetWinner(self):

        winner = None
        for player in self.setScore:
            if (self.setScore[player]['score'] == 6):
                winner = self.setScore[player]

        return winner

    def getSetLooser(self):

        looser = None
        if (self.isSetComplete()):
            for player in self.setScore:
                if (self.setScore[player]['score'] != 6):
                    looser = self.setScore[player]

        return looser

    def toString(self):

        outputStr = 'Games:\n'
        for g in self.games:
            outputStr += g.toString() + '\n'

        outputStr += 'Set Winner: %s (%d), Set Looser: %s (%d)' % (self.getSetWinner()['object'].name, self.getSetWinner()['score'], self.getSetLooser()['object'].name, self.getSetLooser()['score'])

        return outputStr