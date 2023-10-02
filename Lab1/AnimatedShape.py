from graphics import *
def shape(x,y,win):
    name = Text(Point(x, y+95), "Jupiter")
    body = Circle(Point(x, y), 80)
    band = Rectangle(Point(x-79, y), Point(x+79, y+20))
    c_on_band = Oval(Point(x-50, y+22), Point(x,y-10))
    c1 = Circle(Point(x+20, y-25), 18)
    c2 = Circle(Point(x + 20, y - 25), 14)
    c3 = Circle(Point(x + 20, y - 25), 10)
    c4 = Circle(Point(x + 20, y - 25), 8)
    c5 = Circle(Point(x + 20, y - 25), 4)

    name.setFill("white")
    name.setSize(14)
    name.setFace("helvetica")
    name.setStyle("normal")
    body.setFill("red")
    body.setOutline("orange")
    band.setFill("dark red")
    band.setOutline("orange")
    c_on_band.setFill("dark red")
    c_on_band.setOutline("dark red")
    c1.setFill("orange")
    c1.setOutline("dark red")
    c2.setFill("dark red")
    c1.setOutline("orange")
    c3.setOutline("red")
    c3.setFill("orange")
    c4.setFill("orange")
    c5.setOutline("dark red")
    c5.setFill("dark red")
    name.draw(win)
    body.draw(win)
    band.draw(win)
    c_on_band.draw(win)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)
    c5.draw(win)

win=GraphWin('Drawing',1000,700, autoflush=False)
win.setBackground('black')

frame = 0
in_play=True
while in_play:
    mouse_position = win.getMousePosition()
    #print(mouse_position)
    win.clear_win()
    shape(mouse_position.x, mouse_position.y, win)
    win.update()



win.getMouse()
win.close()
