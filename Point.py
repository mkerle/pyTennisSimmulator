from Player import Player

class Point(object):

    def __init__(self, player1, player2):

        self.p1 = player1
        self.p2 = player2

    def playPoint(self):

        self.p1RandVal = self.p1.getServiceRandValue()
        self.p2RandVal = self.p2.getReturnRandValue()

    def getPointWinner(self):

        if (self.p1RandVal > self.p2RandVal):
            return self.p1

        return self.p2

    def getPointLooser(self):

        if (self.p1RandVal <= self.p2RandVal):
            return self.p1

        return self.p2

    def toString(self):

        return 'Winner %s, Looser %s' % (self.getPointWinner().name, self.getPointLooser().name)
