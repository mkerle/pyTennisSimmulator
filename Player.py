
class Player(object):

    def __init__(self, _name, _randFunc):

        self.name = _name
        self.randFunc = _randFunc

    def getRandValue(self):

        return self.randFunc()

