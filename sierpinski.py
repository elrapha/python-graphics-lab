from graphics import *
# create a window with width = 700 and height = 500
win = GraphWin('Program Name', 700, 500)
##tri = Polygon(Point(0,500),Point(350,0), Point(700,500))
##tri.setFill('yellow')
##tri.draw(win)
def midpoint(point1,point2):
    x=abs((point2.x+point1.x)/2)
    y=abs((point2.y+point1.y)/2)
    return Point(x,y)

def sierpinski(p1,p2,p3,win,colors,n):
    sierpinski.count+=1
    print
    print
    print
    print
    if n==1:
        
        tri = Polygon(p1,p2,p3)
        tri.setFill(colors[(sierpinski.count-n)%len(colors)])
        tri.draw(win)
        
    else:
        p4=midpoint(p1,p2)
        p5=midpoint(p2,p3)
        p6=midpoint(p1,p3)

        demo=sierpinski.count%6
        if demo==0:
            sierpinski(p1,p4,p6,win,colors,n-1)
            sierpinski(p4,p2,p5,win,colors,n-1)
            sierpinski(p6,p5,p3,win,colors,n-1)

        if demo==1:
            sierpinski(p1,p4,p6,win,colors,n-1)
            sierpinski(p6,p5,p3,win,colors,n-1)
            sierpinski(p4,p2,p5,win,colors,n-1)

        if demo==2:
            sierpinski(p4,p2,p5,win,colors,n-1)
            sierpinski(p1,p4,p6,win,colors,n-1)
            sierpinski(p6,p5,p3,win,colors,n-1)
        if demo==3:
            sierpinski(p4,p2,p5,win,colors,n-1)
            sierpinski(p6,p5,p3,win,colors,n-1)
            sierpinski(p1,p4,p6,win,colors,n-1)
        if demo==4:
            sierpinski(p6,p5,p3,win,colors,n-1)
            sierpinski(p1,p4,p6,win,colors,n-1)
            sierpinski(p4,p2,p5,win,colors,n-1)
        if demo==5:
            sierpinski(p6,p5,p3,win,colors,n-1)
            sierpinski(p4,p2,p5,win,colors,n-1)
            sierpinski(p1,p4,p6,win,colors,n-1)
            
        

sierpinski.count=-1
colors=['red','gold','blue','green','SteelBlue','pink','PaleTurquoise','SeaGreen','navy','khaki','DodgerBlue','skyBlue']
rounds=[5,6,7]
while  True:
    sierpinski(Point(350,0),Point(0,500),Point(700,500),
           win,colors,rounds[0])
    colors.append(colors[0])
    rounds.append(rounds[0])
    colors.remove(colors[0])
    rounds.remove(rounds[0])
win.mainloop()   
