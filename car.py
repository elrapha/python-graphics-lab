from graphics import *
from wheel import *
"""
win = GraphWin("Rectangle", 300, 300)
rect = Rectangle( Point( 10,10), Point(200, 100 ) )
rect.setFill( "blue" )
rect.draw( win )
rect.setOutline('red')
rect.setWidth(5)
win.mainloop()
"""
win = GraphWin('Car', 700, 300)
class Car(object):
    def __init__(self,center1,rad1,center2,rad2,height):
        self.wheel1=Wheel(center1,rad1*0.3,0.7*rad1)
        self.wheel2=Wheel(center2,rad2*0.3,0.7*rad2)
        self.cartop=Rectangle(Point(50,50-height),Point(100,50-height/2))
        self.carbody=Rectangle\
                      (Point(50-2*rad1,50-height/2),\
                       Point(100+2*rad1,50))
    def draw(self,win):
        self.cartop.draw(win)
        self.carbody.draw(win)
        self.wheel1.draw(win)
        self.wheel2.draw(win)
        
    def set_color(self,tyre_col,rim_col,bodycol):
        self.wheel1.set_color(rim_col,tyre_col)
        self.wheel2.set_color(rim_col,tyre_col)
        self.cartop.setFill(bodycol)
        self.carbody.setFill(bodycol)

    def animate(self,win,dx,dy,n):
        if n>0:
            self.move(dx,dy)
            win.after(50,self.animate,win,dx,dy,n-1)

    def move(self,dx,dy):
        self.wheel1.move(dx,dy)
        self.wheel2.move(dx,dy)
        self.carbody.move(dx,dy)
        self.cartop.move(dx,dy)



car1= Car(Point(50,50),15,Point(100,50),15,40)
car1.draw(win)
car1.set_color('black','grey','pink')
car1.animate(win,1,0,500)

win.mainloop()
