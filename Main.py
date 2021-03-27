import os
import sys
import time
from Game import Game
from Player import Player,AI
def main():
    game=Game()
    players=[AI(hand=0),AI(hand=1)]
    turn=0
    while not game.isEnd():
        availables=[{},{}]
        for i in range(game.H):
            for j in range(game.W):
                availables[0].update(game.isPutOK(j,i,0))
                availables[1].update(game.isPutOK(j,i,1))
        if sum(availables[0].values())==sum(availables[1].values())==0:
            game.result()
            exit()
        game.show()
        while True:
            if sum(availables[turn].values())==0:break
            x,y=players[turn].nextHand(turn,game.Field,availables[turn])
            if availables[turn][f"[{x},{y}]"]:
                game.update(x,y,turn)
                break
            else:
                #print("don't put that.",file=sys.stderr)
                continue
        #time.sleep(1)
        turn=(turn+1)%2

if __name__=="__main__":
    main()