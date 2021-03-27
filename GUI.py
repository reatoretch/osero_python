import wx
import threading
from Main import Osero
from Player import AI,GUIPlayer
class GUI(wx.Frame):
    def __init__(self, parent=None, id=-1, title=None):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(300, 200))
        self.panel.SetBackgroundColour('WHITE')
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Fit()
        self.thread=threading.Thread()
        self.osero=Osero(players=[AI(hand=0),GUIPlayer(hand=1)])
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Bind(wx.EVT_LEFT_DOWN,self.OnClick)
        self.timer.Start(1000) 
    
    def OnTimer(self, event):
        if self.thread.is_alive()==False:
            self.thread=threading.Thread(target=self.osero.run)
            self.thread.start()
        self.Refresh()

    def OnClick(self, event):
        pos = event.GetPosition()
        if isinstance(self.osero.players[self.osero.turn],GUIPlayer):
            x=(pos[0]-50)//20
            y=(pos[1]-20)//20
            self.osero.players[self.osero.turn].setXY(x,y)
 
    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel)
        dc.SetPen(wx.Pen('green'))
        dc.SetBrush(wx.Brush("green"))
        dc.DrawRectangle(50,20,160,160)
        dc.SetPen(wx.Pen('black'))
        for i in range(self.osero.game.H):
            for j in range(self.osero.game.W):
                if self.osero.game.Field[i][j]==0:
                    dc.SetBrush(wx.Brush("black"))
                    dc.DrawCircle(50+20*j+10,20+20*i+10,10)
                elif self.osero.game.Field[i][j]==1:
                    dc.SetBrush(wx.Brush("white"))
                    dc.DrawCircle(50+20*j+10,20+20*i+10,10)
        for i in range(9):
            y = 20 + 20*i
            dc.DrawLine(50, y, 210, y)
        for i in range(9):
            x = 50 + 20*i
            dc.DrawLine(x, 20, x, 180)
 
if __name__ == '__main__':
    app = wx.PySimpleApp()
    w = GUI(title='wxgr-line')
    w.Center()
    w.Show()
    app.MainLoop()