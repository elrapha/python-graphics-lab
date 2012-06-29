from graphics import *
class DigitalClock(object):
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
        self.pos=Point(150,100)
        self.time=Text(self.pos,self.TimeAsStr())
    def draw(self,win):
        self.drawFace(win)
        self.drawText(win)
        self.update(win)
    def drawFace(self,win):
        rect=Rectangle(Point(50,70),Point(250,130))
        rect.setFill('white')
        rect.draw(win)
    def drawText(self,win):
        self.time.setStyle('bold')
        self.time.setSize(36)
        self.time.draw(win)
    def update(self,win):
        if self.second<59:
            self.second+=1
        elif self.minute<59:
            self.second=0
            self.minute+=1
        elif self.hour<23:
            self.second=0
            self.minute=0
            self.hour+=1
        else:
            self.second=0
            self.minute=0
            self.hour=0
        
        self.time.setText(self.TimeAsStr())
        win.after(1000,self.update,win)
            
    def TimeAsStr(self):
        if self.second<10:
            secStr='0'+str(self.second)
        else:   
            secStr=str(self.second)
            
        if self.minute<10:
            minStr='0'+str(self.minute)
        else:   
            minStr=str(self.minute)
            
        if self.hour<10:
            hrStr='0'+str(self.hour)
        else:   
            hrStr=str(self.hour)
        return hrStr+':'+minStr+':'+ secStr

win = GraphWin("Digital Clock", 300, 200)
clock = DigitalClock(23, 58, 50)
clock.draw(win)

win.mainloop()
