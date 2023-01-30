class PlayerScoreCard:
    def __init__(self):
        self.aces = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixs = 0
        self.bonus = 0
        self.threeofakind = 0
        self.fourofakind = 0
        self.fullhouse = 0
        self.smallstraight = 0
        self.largestraight = 0
        self.yahtzee = 0
        self.chance = 0
        self.bonusyahtzee = 0
        self.firstyahtzee = True

listOfScoringOptions = [
    "All 1's",
    "All 2's",
    "All 3's",
    "All 4's",
    "All 5's",
    "All 6's",
    "3 of a kind",
    "4 of a kind",
    "Full House",
    "Small Straight",
    "Large Straight",
    "Yahtzee",
    "Chance"
]
def ChooseScoringOption():
    print("What would you like to score your roll as?")
    for options in listOfScoringOptions:
        print(options)
    whatToScoreAs = input()
    if whatToScoreAs in listOfScoringOptions:
        pass
    else:
        print()

upperSectionScoreCard = {
    "All 1's": "Total of all 1's rolled",
    "All 2's": "Total of all 2's rolled",
    "All 3's": "Total of all 3's rolled",
    "All 4's": "Total of all 4's rolled",
    "All 5's": "Total of all 5's rolled",
    "All 6's": "Total of all 6's rolled",
    "BONUS": "If upper section is 63 or more, score a bonus 35"
}

lowerSectionScoreCard = {
    "3 of a kind": "Total of all 5 Dice",
    "4 of a kind": "Total of all 5 Dice",
    "Full House": 25,
    "Small Straight": 30,
    "Large Straight": 40,
    "Yahtzee": 50,
    "Chance": "Total of all 5 Dice",
    "Yahtzee BONUS": 100
}

def ScoreThreeOfAKind(diceList):
    numberOfEachFace = {}
    for results in diceList:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if not 3 in numberOfEachFace.values() and not 4 in numberOfEachFace.values() and not 5 in numberOfEachFace.values():
        print("You do not have a valid three of a kind")
        PlayerScoreCard.threeofakind = 0
    elif 3 in numberOfEachFace.values() or 4 in numberOfEachFace.values() or 5 in numberOfEachFace.values():
        PlayerScoreCard.threeofakind = sum(diceList)
    print(PlayerScoreCard.threeofakind)

def ScoreFourOfAKind(diceList):
    numberOfEachFace = {}
    for results in diceList:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if not 4 in numberOfEachFace.values() and not 5 in numberOfEachFace.values():
        print("You do not have a vaild four of a kind")
    elif 4 in numberOfEachFace.values() or 5 in numberOfEachFace.values():
        PlayerScoreCard.fourofakind = sum(diceList)
    print(PlayerScoreCard.fourofakind)

def ScoreFullHouse(diceList):
    numberOfEachFace = {}
    for results in diceList:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if 3 in numberOfEachFace.values() and 2 in numberOfEachFace.values():
        PlayerScoreCard.fullhouse = 25
    else:
        print("You do not have a valid full house")
    print(PlayerScoreCard.fullhouse)

def ScoreSmallStraight(diceList):
    PlayerScoreCard.smallstraight = 30

def ScoreLargeStraight(diceList):
    PlayerScoreCard.largestraight = 40

def ScoreYahtzee(diceList):
    numberOfEachFace = {}
    for results in diceList:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if 5 in numberOfEachFace.values():
        PlayerScoreCard.yahtzee = 50
        __ScoreBonusYahtzee()
    else:
        print("You do not have a valid Yahtzee")
    print(PlayerScoreCard.yahtzee)


def __ScoreBonusYahtzee():
    PlayerScoreCard.bonusyahtzee += 100


if __name__=="__main__":

    Player = PlayerScoreCard
    diceList = [2,2,2,2,6]
    ScoreFourOfAKind(diceList)
    Player2 = PlayerScoreCard
    print(Player2.fourofakind)