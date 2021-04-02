import copy
import time
import random
from Game import Game


class Player():
    def __init__(self, hand):
        self.hand = hand

    def nextHand(self, osero):
        x, y = map(int, input().split())
        return x, y


class AI():
    def __init__(self, hand):
        self.hand = hand

    def nextHand(self, osero):
        x, y = random.sample(osero.availables[osero.turn].keys(), 1)[0]
        return x, y


class GUIPlayer():
    def __init__(self, hand):
        self.hand = hand
        self.x = -1
        self.y = -1

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def nextHand(self, osero):
        self.x = -1
        self.y = -1
        while True:
            time.sleep(.1)
            if self.x == self.y == -1:
                continue
            if osero.availables[osero.turn][(self.x, self.y)]:
                return self.x, self.y


class AI_monte():
    def __init__(self, hand):
        self.hand = hand

    def nextHand(self, osero):
        nowGame = copy.deepcopy(osero)
        nowGame.game.consoleFlag = 0
        monte_hand = []
        avail = osero.availables[self.hand].keys()
        for x, y in random.sample(avail, min(len(avail), 5)):
            # for x,y in avail:
            winCnt = 0
            for _ in range(30):
                nowGame.turn = osero.turn
                nowGame.game.Field = copy.deepcopy(osero.game.Field)
                nowGame.game.update(x, y, self.hand)
                nowGame.turn = (nowGame.turn+1) % 2
                nowGame.players = [
                    AI(hand=osero.game.BLACK), AI(hand=osero.game.WHITE)]
                while True:
                    if nowGame.run():
                        # nowGame.game.show()
                        winCnt += nowGame.cnt[self.hand] > nowGame.cnt[(
                            self.hand+1) % 2]
                        break
            monte_hand += [[winCnt, x, y]]
            # print(monte_hand)
        _, x, y = sorted(monte_hand, reverse=True)[0]
        return x, y
