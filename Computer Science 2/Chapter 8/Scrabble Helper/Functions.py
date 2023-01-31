import json
from difflib import get_close_matches
from YesNoQuestion import YesOrNoQuestion
from PyDictionary import PyDictionary as dictionary

EnglishDictionary = json.load(open("Computer Science 2\Chapter 8\Scrabble Helper\dictionary.json"))

def CheckValidWord(word):
    word = word.lower()
    if word in EnglishDictionary:
        return EnglishDictionary[word], word
    elif len(get_close_matches(word, EnglishDictionary.keys())) > 0:
        answer = YesOrNoQuestion("Did you mean % s instead?" % get_close_matches(word, EnglishDictionary.keys())[0])
        if answer == True:
            word = get_close_matches(word, EnglishDictionary.keys())[0]
            return EnglishDictionary[get_close_matches(word, EnglishDictionary.keys())[0]], word
        elif answer == False:
            print("The word doesn't exist. Please double check your spelling")
        else:
            print("Sorry, didn't catch that")
    else:
        print("The word doesn't exist. Please double check your spelling")


def GetWordDefinition(word):
    if dictionary.meaning(word):
        definition = dictionary.meaning(word)
        return print(f"The definition for {word} is:\n{definition}")
    else:
        return print(f"There is no definition for the word {word}")


if __name__ == "__main__":
    userword = input("Enter the word you would like to see if is real:\n")
    legit, userword = CheckValidWord(userword)
    if legit == 1:
        print(f"Yes! {userword.capitalize()} is indeed a real word!")
        GetWordDefinition(userword)
    elif legit == "None":
        print("That word doesn't exist")