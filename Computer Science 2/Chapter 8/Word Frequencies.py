listOfWords = ["hello", "hello", "pee", "poo", "pee"]
numberOfUniqueWords = {}
def BuildDictionary(list):
    for words in list:
            numberOfUniqueWords[words] = numberOfUniqueWords.get(words, 0) + 1
BuildDictionary(listOfWords)
#print(numberOfUniqueWords.get("hello", 0))