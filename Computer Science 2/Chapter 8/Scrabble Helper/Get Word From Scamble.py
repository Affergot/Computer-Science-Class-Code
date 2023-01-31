'''
Given a mess of letters, find all possible combinations and put them into a list
Then check the list to see if any of those words are in the english language
Put any real words into a new list
Turn real list into a dictionary with Scrabble point values linked to the appropriate word
'''
import json
import itertools
from PyDictionary import PyDictionary as EnglishDictionary
import time

#Try to use the json file dictionary to see if the compile time is faster
#KnownWords = json.load(open("Computer Science 2\Chapter 8\Scrabble Helper\dictionary.json"))

def AllTileCombinations(UsersCurrentTiles):
    ListOfPossibleWords = []
    for length in range(len(UsersCurrentTiles)+1):
        for combination in itertools.permutations(UsersCurrentTiles, length):
            if combination not in ListOfPossibleWords:
                ListOfPossibleWords += ["".join(combination)]
    return ListOfPossibleWords

def WordsThatExist(RandomWordslist):
    RealWordsList = []
    for word in RandomWordslist:
        if EnglishDictionary.meaning(word,True) is None:
            pass
        elif len(word) < 2:
            pass
        else:
            if word not in RealWordsList:
                RealWordsList.append(word)            
    return RealWordsList





if __name__ == "__main__":
    print("Please enter all of your tiles with a space inbetween. Ex:[a b d e k z r]")
    UsersCurrentTiles = input().lower().split()
    start = time.time()
    PossibleWords = AllTileCombinations(UsersCurrentTiles)
    print(PossibleWords)
    RealWords = WordsThatExist(PossibleWords)
    print(RealWords)
    end = time.time()
    print(end - start)
