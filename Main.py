import os
import sys
import time
import copy
import threading
from Game import Game
from Player import Player, AI


class Osero():
    def __init__(self, players=[AI(hand=0), AI(hand=1)]):
        self.players = players
        self.game = Game()
        self.cnt = []
        self.turn = 0

    def run(self):
        self.availables = [{}, {}]
        for i in range(self.game.H):
            for j in range(self.game.W):
                self.availables[self.game.BLACK].update(
                    self.game.isPutOK(j, i, self.game.BLACK))
                self.availables[self.game.WHITE].update(
                    self.game.isPutOK(j, i, self.game.WHITE))
        if sum(self.availables[self.game.BLACK].values()) == sum(self.availables[self.game.WHITE].values()) == 0:
            self.cnt = self.game.result()
            self.game.gameEndFlag = 1
            if self.game.consoleFlag:
                print(
                    f"Black:{self.cnt[self.game.BLACK]}\nWhite:{self.cnt[self.game.WHITE]}")
            return self.game.gameEndFlag
        # self.game.show()
        while True:
            if sum(self.availables[self.turn].values()) == 0:
                break
            x, y = self.players[self.turn].nextHand(copy.deepcopy(self))
            if self.availables[self.turn][(x, y)]:
                self.game.update(x, y, self.turn)
                break
            else:
                #print("don't put that.",file=sys.stderr)
                continue
        # time.sleep(1)
        self.turn = (self.turn+1) % 2


if __name__ == "__main__":
    osero = Osero()
    osero.run()
