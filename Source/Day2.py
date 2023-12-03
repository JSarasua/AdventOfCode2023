from AoCUtilities import *

colorCount = {'red':12, 'green': 13, 'blue': 14}

'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    'read each line, if number record the next words color and add it to list to compare against dictionary'
    'evaluate and reset on each semicolon'
    totalSum = 0
    currentIndex = 1
    for fileLine in fileData:
        isGood = True
        fileLine = fileLine.split(':')[1]
        fileLine = fileLine.strip()
        colorSets = fileLine.split(';')
        for colorGroup in colorSets:
            currentSetAmount = {'red': 0, 'green': 0, 'blue': 0}
            colorCounts = colorGroup.split(',')
            for colors in colorCounts:
                colors = colors.strip()
                numberedColors = colors.split(' ')
                indColorCount = int(numberedColors[0])
                currentSetAmount[numberedColors[1]] += indColorCount
            if currentSetAmount['red'] > colorCount['red'] or currentSetAmount['green'] > colorCount['green'] or currentSetAmount['blue'] > colorCount['blue']:
                isGood = False
        if isGood:
                totalSum += currentIndex
        currentIndex += 1



    return totalSum

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    totalSumPower = 0
    for fileLine in fileData:
        isGood = True
        fileLine = fileLine.split(':')[1]
        fileLine = fileLine.strip()
        colorSets = fileLine.split(';')
        colorPowers = {'red': 0, 'green': 0, 'blue': 0}
        for colorGroup in colorSets:
            colorCounts = colorGroup.split(',')
            for colors in colorCounts:
                colors = colors.strip()
                numberedColors = colors.split(' ')
                indColorCount = int(numberedColors[0])
                if colorPowers[numberedColors[1]] < indColorCount:
                    colorPowers[numberedColors[1]] = indColorCount

        totalSumPower += colorPowers['red']*colorPowers['green']*colorPowers['blue']

    return totalSumPower

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day2.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))