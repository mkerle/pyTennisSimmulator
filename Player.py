
class Player(object):

    def __init__(self, _name, _servRandFunc, _returnRandFunc):

        self.name = _name
        self.serveFunc = _servRandFunc
        self.returnFunc = _returnRandFunc

    def getServiceRandValue(self):

        return self.serveFunc()

    def getReturnRandValue(self):

        return self.returnFunc()

