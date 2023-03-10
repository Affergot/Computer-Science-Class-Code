import time
def char_by_char(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.03)

if __name__ == "__main__":

    string = input("Enter a string: ")
    char_by_char(string)