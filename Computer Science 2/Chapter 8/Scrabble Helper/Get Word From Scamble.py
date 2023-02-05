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


KnownWords = json.load(open("Computer Science 2\Chapter 8\Scrabble Helper\dictionary.json"))

def AllTileCombinations(UsersCurrentTiles):
    ListOfTilePermutations = []
    for length in range(len(UsersCurrentTiles)+1):
        for combination in itertools.permutations(UsersCurrentTiles, length):
            if combination not in ListOfTilePermutations:
                ListOfTilePermutations += ["".join(combination)]
    return ListOfTilePermutations

def FiltrationOfMassWords(list):
    ReasonableWordList = []
    for gibberish in list:   
        if len(gibberish) < 3:
            gibberish = None
        if gibberish in KnownWords:
            if gibberish not in ReasonableWordList:
                ReasonableWordList.append(gibberish)
    return ReasonableWordList


def WordsWithDefinition(RandomWordslist):
    RealWordsList = []
    for word in RandomWordslist:
        if EnglishDictionary.meaning(word,True) is None:
            word = None
        else:
            if word not in RealWordsList:
                RealWordsList.append(word)            
    return RealWordsList





if __name__ == "__main__":
    print("Please enter all of your tiles with a space inbetween. Ex:[a b d e k z r]")
    UsersCurrentTiles = input().lower().split()
    AllPermutations = AllTileCombinations(UsersCurrentTiles)
    print(AllPermutations)
    FilteredPermutations = FiltrationOfMassWords(AllPermutations)
    #print(FilteredPermutations)
    WordsInDictionary = WordsWithDefinition(FilteredPermutations)
    print(WordsInDictionary)
