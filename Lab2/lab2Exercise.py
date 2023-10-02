import random


class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def roll(self):
        return random.randint(1, self.number_of_sides)

def main():

    my_dice = Dice(6)
    my_side_die = Dice(6)
    #print(my_dice.number_of_sides)
    #my_dice.roll()
    doubles = 0
    for count in range(1000):
        roll_1=my_dice.roll()
        side_roll=my_side_die.roll()
        print(roll_1)
        print(side_roll)
        if roll_1==side_roll:
            print("DOUBLEEE")
            doubles += 1

    print(doubles)


if __name__=="__main__":
    main()