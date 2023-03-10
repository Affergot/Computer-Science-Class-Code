from CharByChar import char_by_char
import time
import json


def print_results():
    with open(("Computer Science 2\Chapter 11\List_Of_Unique_Nums.json"), 'r') as f:
        random_nums = json.load(f)
    # Unpack the list into the variables.
    number_of_retries = random_nums.pop()
    char_by_char("The number of retries was: ")
    char_by_char(str(number_of_retries))
    time.sleep(1)
    char_by_char("\nThe list of unique numbers is: ")
    char_by_char(str(random_nums))



if __name__ == "__main__":
    print_results()