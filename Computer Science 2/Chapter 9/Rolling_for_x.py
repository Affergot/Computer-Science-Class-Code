'''
Complete function roll_specific_number() that has three parameters: a GVDie object, an integer representing a desired face number of a die,
 and an integer representing the goal amount of times to roll the desired face number. The function roll_specific_number() then rolls the die
   until the desired face number is rolled the goal amount of times and returns the number of rolls required.

Note: For testing purposes, a GVDie object is created in the main() function using a pseudo-random number generator with a fixed seed value.
 The program uses a seed value of 15 during development, but when submitted, a different seed value will be used for each test case.
'''
import random
from TypedOut import *

class GVDie:
    def __init__(self):
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1, 6)

    def set_seed(self, seed):
        self.rand.seed(seed)
    
    def roll_specific_number(self, selected_face, taget_amount):
        rolls = 0
        while True:
            self.roll()
            rolls += 1
            if self.my_value == selected_face:
                taget_amount -= 1
            if taget_amount == 0:
                return rolls


if __name__ == "__main__":

    die = GVDie()
    die.set_seed(int(input("Enter a seed value\n:")))
    charByChar("See how many times it takes to roll a specific number on a die.\n")
    charByChar("Enter the desired face value\n")
    selected_face = int(input(":"))
    charByChar("Enter the goal amount of times to roll the desired face value\n")
    taget_amount = int(input(":"))
    rolls = die.roll_specific_number(selected_face, taget_amount)
    charByChar(f"It took {rolls} rolls to roll {taget_amount} {selected_face}'s.")
