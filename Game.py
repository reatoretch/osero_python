import os
import sys
X=[1,1,0,-1,-1,-1,0,1]
Y=[0,-1,-1,-1,0,1,1,1]
class Game():
    def __init__(self,N=8,consoleFlag=1):
        if N%2:print("No!!",file=sys.stderr);exit()
        self.H=N
        self.W=N
        self.BLACK=0
        self.WHITE=1
        self.gameEndFlag=0
        self.consoleFlag=consoleFlag
        self.winner=""
        self.Field=[[-1]*self.W for i in range(self.H)]
        self.Field[self.H//2][self.W//2]=1
        self.Field[self.H//2-1][self.W//2-1]=1
        self.Field[self.H//2][self.W//2-1]=0
        self.Field[self.H//2-1][self.W//2]=0 

    def isEnd(self):
        return self.gameEndFlag

    def show(self):
        os.system("cls")
        for i in range(self.H):
            for j in range(self.W):
                if self.Field[i][j]==self.BLACK:
                    print(end="x")
                elif self.Field[i][j]==self.WHITE:
                    print(end="o")
                else:
                    print(end=".")
            print()
    
    def isPutOK(self,x,y,hand):
        d={}
        if self.Field[y][x]==-1:
            for nx,ny in zip(X,Y):
                tx,ty=x,y
                cnt=0
                if (x,y) in d:break
                while 0<=tx+nx<self.W and 0<=ty+ny<self.H:
                    if self.Field[ty+ny][tx+nx]!=-1 and self.Field[ty+ny][tx+nx]!=hand:
                        cnt+=1
                    elif self.Field[ty+ny][tx+nx]==hand and cnt>0:
                        d[(x,y)]=True
                        break
                    else:
                        break
                    ty+=ny;tx+=nx
        return d

    def update(self,x,y,hand):
        self.Field[y][x]=hand
        for nx,ny in zip(X,Y):
            tx,ty=x,y
            cnt=0
            while 0<=tx+nx<self.W and 0<=ty+ny<self.H:
                if self.Field[ty+ny][tx+nx]!=-1 and self.Field[ty+ny][tx+nx]!=hand:
                    cnt+=1
                elif self.Field[ty+ny][tx+nx]==hand and cnt>0:
                    for i in range(1,cnt+1):
                        self.Field[y+i*ny][x+i*nx]=hand
                    break
                else:
                    break
                ty+=ny;tx+=nx

    def result(self):
        cnt=[0,0]
        for i in range(self.H):
            for j in range(self.W):
                if self.Field[i][j]==self.WHITE:
                    cnt[self.WHITE]+=1
                elif self.Field[i][j]==self.BLACK:
                    cnt[self.BLACK]+=1
        if self.consoleFlag:
            if cnt[self.BLACK]>cnt[self.WHITE]:
                print("Black!!")
            elif cnt[self.BLACK]==cnt[self.WHITE]:
                print("Draw Game")
            else:
                print("White!!")
        return cnt