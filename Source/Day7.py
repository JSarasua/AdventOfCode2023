import functools

from AoCUtilities import *
from collections import Counter


cardTypesPartA = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9': 7, '8': 6, '7': 5, '6':4, '5':3, '4':2, '3':1, '2':0}
cardTypesPartB = {'A':12, 'K':11, 'Q':10, 'J':-1, 'T':8, '9': 7, '8': 6, '7': 5, '6':4, '5':3, '4':2, '3':1, '2':0}


class CardHand:

    def __init__(self, hand : list, bid : int, isPartA : bool):
        self.hand = hand
        self.bid = bid
        self.isPartA = isPartA
        self.handType = self.CalcHandTypePartA()
        if not isPartA:
            self.handType = self.CalcHandTypePartB()


    def CalcHandTypePartA(self):
        handAsCoundedList= Counter(self.hand).most_common(5)
        dictHand = dict(handAsCoundedList)
        if 'J' in dictHand:
            jCount = dictHand['J']

        for cardIndex in range(len(handAsCoundedList)):
            card = handAsCoundedList[cardIndex][0]
            count = handAsCoundedList[cardIndex][1]
            if count == 5:
                return 6
            elif count == 4:
                return 5
            elif count == 3:
                nextCount = handAsCoundedList[cardIndex+1][1]
                if nextCount == 2:
                    return 4
                else:
                    return 3
            elif count == 2:
                nextCount = handAsCoundedList[cardIndex + 1][1]
                if nextCount == 2:
                    return 2
                else:
                    return 1
            else:
                return 0
        return 0

    def CalcHandTypePartB(self):
        handAsCoundedList= Counter(self.hand).most_common(5)
        dictHand = dict(handAsCoundedList)
        jCount = 0
        if 'J' in dictHand:
            jCount = dictHand['J']

        for cardIndex in range(len(handAsCoundedList)):
            card = handAsCoundedList[cardIndex][0]
            count = handAsCoundedList[cardIndex][1]
            if count == 5:
                return 6
            elif count == 4:
                if jCount == 4:
                    return 6
                if jCount == 1:
                    return 6
                else:
                    return 5
            elif count == 3:
                nextCount = handAsCoundedList[cardIndex + 1][1]
                if jCount == 2:
                    return 6
                elif jCount == 1:
                    return 5
                elif jCount == 3:
                    if nextCount == 2:
                        return 6
                    else:
                        return 5
                if nextCount == 2:
                    return 4
                else:
                    return 3
            elif count == 1:
                if jCount == 1:
                    return 1
                else:
                    return 0
            elif count == 2:
                if card == 'J':
                    nextCount = handAsCoundedList[cardIndex + 1][1]
                    if nextCount == 2: # 4s
                        return 5
                    else:
                        return 3 # 3s 1 unique + 2 Js
                else:
                    if jCount == 2:
                        return 5
                    nextCount = handAsCoundedList[cardIndex + 1][1]
                    if nextCount == 2:
                        if jCount == 1:
                            return 4 # 2, 2, 1 where 1 is J
                        return 2 # 2 pairs
                    elif jCount == 1:
                        return 3 #3s 2 of a kind + 1 J
                    else:
                        return 1
            else:
                return 0
        return 0

def CmpHands(handA : CardHand, handB : CardHand):
    if (handA.handType > handB.handType):
        return 1
    elif handA.handType < handB.handType:
        return -1
    else:
        cardIndex = 0
        for cardIndex in range(len(handA.hand)):
            myCard = cardTypesPartA[handA.hand[cardIndex]]
            theirCard = cardTypesPartA[handB.hand[cardIndex]]
            if not handA.isPartA:
                myCard = cardTypesPartB[handA.hand[cardIndex]]
                theirCard = cardTypesPartB[handB.hand[cardIndex]]
            if myCard > theirCard:
                return 1
            elif myCard < theirCard:
                return -1
            else:
                continue
        return 0  # They must be identical

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    hands = []
    for fileLine in fileData:
        lineData = fileLine.strip().split(' ')
        hand = [x for x in lineData[0]]
        bid = int(lineData[1])
        hands.append(CardHand(hand, bid, True))

    sortedHand = sorted(hands, key=functools.cmp_to_key(CmpHands))
    sumOfScores = 0
    for handIndex in range(len(sortedHand)):
        bid = sortedHand[handIndex].bid
        sumOfScores += bid*(handIndex+1)

    return sumOfScores

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    hands = []
    for fileLine in fileData:
        lineData = fileLine.strip().split(' ')
        hand = [x for x in lineData[0]]
        bid = int(lineData[1])
        hands.append(CardHand(hand, bid, False))

    sortedHand = sorted(hands, key=functools.cmp_to_key(CmpHands))
    sumOfScores = 0
    for handIndex in range(len(sortedHand)):
        bid = sortedHand[handIndex].bid
        sumOfScores += bid*(handIndex+1)

    return sumOfScores

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day7.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))