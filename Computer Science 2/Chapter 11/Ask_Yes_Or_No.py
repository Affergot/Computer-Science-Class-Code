from YesNoQuestion import yes_no_question
from CharByChar import char_by_char
import random

def ask_for_seed():
    if yes_no_question("Do you want to use a random seed?") == True:
        char_by_char("Enter a random seed\n")
        RandomSeed = input(": ")
        random.seed(RandomSeed)
    else:
        pass