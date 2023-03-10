from CharByChar import char_by_char

def get_number_of_random_numbers():
    char_by_char("Enter the number of random numbers to generate.\n")
    number_of_random_numbers = int(input(": "))
    return number_of_random_numbers

if __name__ == "__main__":
    get_number_of_random_numbers()
    print("Done")