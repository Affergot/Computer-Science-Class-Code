def yes_no_question(userprompt):
    print(userprompt)
    answer = input("Enter [y/n]\n")
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        print("Sorry, you didn't input a valid answer. Try again")
        yes_no_question(userprompt)

if __name__ == "__main__":
    if yes_no_question("Do you want to continue?") == True:
        print("You said yes")
    else:
        print("You said no")
