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