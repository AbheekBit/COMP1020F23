from graphics import *

def eyes(x, y, win):
    face = Circle(Point(x,y+20),80)
    c1 = Circle(Point(x - 40, y), 30)
    c2 = Circle(Point(x + 40, y), 30)
    face.setFill("red")
    c1.setFill("blue")
    c2.setFill("green")
    face.draw(win)
    c1.draw(win)
    c2.draw(win)

win=GraphWin('Drawing',1000,700, autoflush=False)
win.setBackground('yellow')

frame = 0
for x in range(1, 1000, 1):
    print(x)
    win.clear_win()
    eyes(x, 0, win)
    win.update()

win.getMouse()
win.close()
