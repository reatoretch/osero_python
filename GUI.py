import wx
from Main import Osero
class GUI(wx.Frame):
    def __init__(self, parent=None, id=-1, title=None):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(300, 200))
        self.panel.SetBackgroundColour('WHITE')
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Fit()
        self.osero=Osero()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(1000) 
    
    def OnTimer(self, event):
        self.osero.run()
        self.Refresh()
 
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