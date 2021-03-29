import os
import sys
import time
import threading
from Game import Game
from Player import Player,AI
class Osero():
    def __init__(self,players=[AI(hand=0),AI(hand=1)]):
        self.players=players
        self.game=Game()
        self.turn=0
    def run(self):
        availables=[{},{}]
        for i in range(self.game.H):
            for j in range(self.game.W):
                availables[0].update(self.game.isPutOK(j,i,0))
                availables[1].update(self.game.isPutOK(j,i,1))
        if sum(availables[0].values())==sum(availables[1].values())==0:
            self.game.result()
            self.game.gameEndFlag=1
            exit()
        #self.game.show()
        while True:
            if sum(availables[self.turn].values())==0:break
            x,y=self.players[self.turn].nextHand(self.turn,self.game.Field,availables[self.turn])
            if availables[self.turn][f"[{x},{y}]"]:
                self.game.update(x,y,self.turn)
                break
            else:
                #print("don't put that.",file=sys.stderr)
                continue
        #time.sleep(1)
        self.turn=(self.turn+1)%2

if __name__=="__main__":
    osero=Osero()
    osero.run()