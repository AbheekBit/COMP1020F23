from graphics import *
from Dice import *


class Horse:
    def __init__(self, name, x_pos, y_pos, image, max_speed):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.dice = Dice(max_speed)

    def move(self, update):
        self.x_pos += self.dice.roll()

    def drawimage(self, win):
        self.image.draw_at_pos(win, self.x_pos, self.y_pos)

    def crossed_finish(self):
        return self.x_pos > 800


def main():
    win: GraphWin = GraphWin('Horse Race', 1000, 500, autoflush=False)
    win.setBackground('yellow')

    crab = Horse("Crab", 10, 40, Image(Point(100, 100), "Knight.gif"), 10)
    plant = Horse("Plant", 10, 110, Image(Point(100, 100), "Wizard.gif"), 10)

    finish_line = Line(Point(800, 1), Point(800, 500))

    finish_line.draw(win)
    crab.drawimage(win)
    plant.drawimage(win)

    race_finished = False

    mouse_clicked = False
    if win.getMouse():
        mouse_clicked = True

    while not race_finished and mouse_clicked:
        crab.move(update(5))
        plant.move(update(5))
        win.clear_win()
        finish_line.draw(win)
        crab.drawimage(win)
        plant.drawimage(win)

        win.update()

        if crab.crossed_finish():
            print("Crab has won the race!")
            race_finished = True
        if plant.crossed_finish():
            print("Plant has won the race!")
            race_finished = True
        if crab.crossed_finish() and plant.crossed_finish():
            print("The race is a tie")
            race_finished = True


if __name__ == "__main__":
    main()
