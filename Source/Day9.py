from AoCUtilities import *

def SolveLineA(dataLine : list):

    allDiffs = []
    currentDataLine = dataLine
    allDiffs.append(currentDataLine)

    currentSet = set(currentDataLine)
    while len(currentSet) > 1 or 0 not in currentSet:
        newDiffLine = []
        currentIndex = 0
        while currentIndex < len(currentDataLine) - 1:
            currentVal = currentDataLine[currentIndex]
            nextVal = currentDataLine[currentIndex + 1]
            diff = nextVal - currentVal
            newDiffLine.append(diff)

            currentIndex += 1
        currentDataLine = newDiffLine
        currentSet = set(currentDataLine)
        allDiffs.append(currentDataLine)

    nextVal = 0
    currentDiffIndex = len(allDiffs) - 2
    while currentDiffIndex >= 0:
        prevRow = allDiffs[currentDiffIndex]
        prevVal = prevRow[-1]
        nextVal += prevVal
        currentDiffIndex -= 1
    return nextVal

def SolveLineB(dataLine : list):

    allDiffs = []
    currentDataLine = dataLine
    allDiffs.append(currentDataLine)

    currentSet = set(currentDataLine)
    while len(currentSet) > 1 or 0 not in currentSet:
        newDiffLine = []
        currentIndex = 0
        while currentIndex < len(currentDataLine) - 1:
            currentVal = currentDataLine[currentIndex]
            nextVal = currentDataLine[currentIndex + 1]
            diff = nextVal - currentVal
            newDiffLine.append(diff)

            currentIndex += 1
        currentDataLine = newDiffLine
        currentSet = set(currentDataLine)
        allDiffs.append(currentDataLine)

    nextVal = 0
    currentDiffIndex = len(allDiffs) - 2
    while currentDiffIndex >= 0:
        prevRow = allDiffs[currentDiffIndex]
        prevVal = prevRow[0]
        nextVal = prevVal - nextVal
        currentDiffIndex -= 1
    return nextVal


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sums = 0
    for fileLine in fileData:
        dataLine = [int(x) for x in fileLine.strip().split(' ')]
        sums += SolveLineA(dataLine)
    return sums

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sums = 0
    for fileLine in fileData:
        dataLine = [int(x) for x in fileLine.strip().split(' ')]
        sums += SolveLineB(dataLine)
    return sums

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day9.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))