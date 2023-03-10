from CharByChar import char_by_char

def yes_no_question(userprompt):
    char_by_char(userprompt)
    char_by_char("\nEnter [y/n]\n")
    answer = input(": ")
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        char_by_char("Sorry, you didn't input a valid answer. Try again")
        yes_no_question(userprompt)


if __name__ == "__main__":
    if yes_no_question("Do you want to continue?") == True:
        char_by_char("You said Yes")
    else:
        char_by_char("You said No")
