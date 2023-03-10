from CharByChar import char_by_char

def get_range():
    char_by_char("Enter the max range of numbers to chose from.\n")
    max_num = int(input(": "))
    return max_num

if __name__ == "__main__":
    get_range()
    print("Done")
