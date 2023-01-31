def YesOrNoQuestion(userprompt):
    print(userprompt)
    answer = input("Enter [y/n]\n")
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        print("Sorry, you didn't input a valid answer. Try again")
        YesOrNoQuestion(userprompt)