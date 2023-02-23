import time
def charByChar(string):
    for letter in string:
        print(letter, end='', flush=True)
        time.sleep(0.03)

if __name__ == "__main__":

    string = input("Enter a string: ")
    charByChar(string)