from Point import Point
from Player import Player

class Game(object):

    def __init__(self, player1, player2):

        self.p1 = player1
        self.p2 = player2

        self.points = []

        self.gameScore = { self.p1.name : { 'score' : 0, 'object' : self.p1 }, self.p2.name : { 'score' : 0, 'object' : self.p2 } }

    def playGame(self):

        while (not self.isGameComplete()):
            point = Point(self.p1, self.p2)
            point.playPoint()

            self.updateGameScore(point.getPointWinner(), point.getPointLooser())

            self.points.append(point)


    def updateGameScore(self, winner, looser):

        currentWinnerScore = self.gameScore[winner.name]['score']
        currentLooserScore = self.gameScore[looser.name]['score']

        if (currentWinnerScore == 41):
            self.gameScore[winner.name]['score'] = 42
        elif (currentWinnerScore == 40 and currentLooserScore == 41):
            self.gameScore[winner.name]['score'] = 40
            self.gameScore[looser.name]['score'] = 40
        elif (currentWinnerScore == 40 and currentLooserScore == 40):
            self.gameScore[winner.name]['score'] = 41
        elif (currentWinnerScore == 40 and currentLooserScore < 40):
            self.gameScore[winner.name]['score'] = 42
        elif (currentWinnerScore == 30):
            self.gameScore[winner.name]['score'] = 40
        elif (currentWinnerScore == 15):
            self.gameScore[winner.name]['score'] = 30
        elif (currentWinnerScore == 0):
            self.gameScore[winner.name]['score'] = 15

    def isGameComplete(self):

        isComplete = False
        for player in self.gameScore:
            if (self.gameScore[player]['score'] == 42):
                isComplete = True

        return isComplete

    def getGameWinner(self):

        winner = None
        for player in self.gameScore:
            if (self.gameScore[player]['score'] == 42):
                winner = self.gameScore[player]

        return winner

    def getGameLooser(self):

        looser = None
        if (self.isGameComplete()):
            for player in self.gameScore:
                if (self.gameScore[player]['score'] != 42):
                    looser = self.gameScore[player]

        return looser

    def toString(self):

        outputStr = 'Points:\n'
        for p in self.points:
            outputStr += p.toString() + '\n'

        outputStr += 'Game Winner: %s (%d), Game Looser: %s (%d)' % (self.getGameWinner()['object'].name, self.getGameWinner()['score'], self.getGameLooser()['object'].name, self.getGameLooser()['score'])

        return outputStr
        

