class Player():
    def __init__(self,hand):
        self.hand=hand
    def nextHand(self,osero):
        x,y=map(int,input().split())
        return x,y

import re
import random
class AI():
    def __init__(self,hand):
        self.hand=hand
    def nextHand(self,osero):
        s=random.sample(osero.availables[osero.turn].keys(),1)
        x,y=map(int,str(re.sub(r"(\[|\])","",s[0])).split(","))
        return x,y

import time
class GUIPlayer():
    def __init__(self,hand):
        self.hand=hand
        self.x=-1
        self.y=-1
    def setXY(self,x,y):
        self.x=x
        self.y=y
    def nextHand(self,osero):
        self.x=-1
        self.y=-1
        while True:
            time.sleep(.1)
            if self.x==self.y==-1:continue
            if osero.availables[osero.turn][f"[{self.x},{self.y}]"]:return self.x,self.y

import copy
from Game import Game
class AI_monte():
    def __init__(self,hand):
        self.hand=hand
    def nextHand(self,osero):
        pass