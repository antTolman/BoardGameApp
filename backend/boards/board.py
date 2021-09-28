import numpy as np

class GameBoard:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def initBoard(self):
        self.board = [[0] * self.width] * self.height

    def resetBoard(self):
        self.initBoard()

    def inBounds(self, point):
        if point[0] < 0 or point[0] >= self.height:
            return False
        if point[1] < 0 or point[1] >= self.width:
            return False
        return True

    def isValidMove(self, move):
        if not self.inBounds(move.getStart()):
            return False
        if not self.inBounds(move.getEnd()):
            return False
        return True

    def executeMove(self, move):
        pass

    def getBoardSize(self):
        return (self.height, self.width)

    def getPiece(self, location):
        pass

    def getBoard(self):
        return self.board
