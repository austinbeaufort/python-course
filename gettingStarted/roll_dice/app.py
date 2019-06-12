import random


class Dice:
    def __init__(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

    def roll_dice(self):
        return (self.dice1, self.dice2)


dice = Dice()

print(dice.roll_dice())


        