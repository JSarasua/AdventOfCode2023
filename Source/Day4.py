from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    totalSum = 0
    for fileLine in fileData:
        winningNumCount = 0
        fileLine = fileLine.split(': ')[1].strip()
        results = fileLine.split(' | ')
        winningNumers = results[0].strip().split(' ')
        myNumbers = results[1].strip().split(' ')
        for myNum in myNumbers:
            if myNum in winningNumers and myNum.isnumeric():
                winningNumCount += 1

        if winningNumCount == 0:
            continue
        else:
            power = pow(2, winningNumCount - 1)
            totalSum += power

    return totalSum

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    copyDict = dict.fromkeys(range(len(fileData)),1)
    cardCount = 0
    for index in range(len(fileData)):

        cardCount += copyDict[index]
        fileLine = fileData[index]

        winningNumCount = 0
        fileLine = fileLine.split(': ')[1].strip()
        results = fileLine.split(' | ')
        winningNumers = results[0].strip().split(' ')
        myNumbers = results[1].strip().split(' ')
        for myNum in myNumbers:
            if myNum in winningNumers and myNum.isnumeric():
                winningNumCount += 1

        if winningNumCount == 0:
            continue
        else:
            for copyIndex in range(index + 1, index + winningNumCount + 1):
                copyDict[copyIndex] += copyDict[index]

    return cardCount

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day4.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))