class Player():
    def __init__(self,hand):
        self.hand=hand
    def nextHand(self,turn,field,available):
        x,y=map(int,input().split())
        return x,y

import random
class AI():
    def __init__(self,hand):
        self.hand=hand
    def nextHand(self,turn,field,available):
        x,y=random.randint(0,len(field)-1),random.randint(0,len(field)-1)
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
    def nextHand(self,turn,field,available):
        self.x=-1
        self.y=-1
        while True:
            time.sleep(.1)
            if self.x==self.y==-1:continue
            if available[f"[{self.x},{self.y}]"]:return self.x,self.y