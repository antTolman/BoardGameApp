


class PlayerMove:
    def __init__(self, start, end, player):
        self.start = start
        self.end = end
        self.player = player

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getPlayer(self):
        return self.player