from AoCUtilities import *
import math
from array import array

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    moveInstructions = [x for x in fileData[0].strip()]
    moveInstructions = list(map(lambda x: x.replace('L', '0'), moveInstructions))
    moveInstructions = list(map(lambda x: x.replace('R', '1'), moveInstructions))
    moveInstructions = [int(x) for x in moveInstructions]

    mapDict = {}

    startingIndex = 2
    while startingIndex < len(fileData):
        fileLine = fileData[startingIndex].strip().split('=')
        key = fileLine[0].strip()
        leftDir, rightDir = fileLine[1].replace('(','').replace(')', '').split(',')
        mapDict[key] = (leftDir.strip(), rightDir.strip())
        startingIndex += 1


    currentSteps = 0
    currentKey = 'AAA'

    while True:
        stepIndex = 0
        while stepIndex < len(moveInstructions):
            currentSteps += 1
            dir = moveInstructions[stepIndex]
            currentKey = mapDict[currentKey][dir]
            stepIndex += 1

            if currentKey == 'ZZZ':
                return currentSteps

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    moveInstructions = [x for x in fileData[0].strip()]
    moveInstructions = list(map(lambda x: x.replace('L', '0'), moveInstructions))
    moveInstructions = list(map(lambda x: x.replace('R', '1'), moveInstructions))
    moveInstructions = [int(x) for x in moveInstructions]

    mapDict = {}
    startingKeys = []



    startingIndex = 2
    while startingIndex < len(fileData):
        fileLine = fileData[startingIndex].strip().split('=')
        key = fileLine[0].strip()
        if key.endswith('A'):
            startingKeys.append(key)
        leftDir, rightDir = fileLine[1].replace('(','').replace(')', '').split(',')
        mapDict[key] = (leftDir.strip(), rightDir.strip())
        startingIndex += 1

    LCMs = [-1] * len(startingKeys)
    currentSteps = 0
    LCMsFound = 0

    while True:
        stepIndex = 0
        while stepIndex < len(moveInstructions):
            currentSteps += 1
            dir = moveInstructions[stepIndex]

            keysEndingInZ = 0
            for keyIndex in range(len(startingKeys)):
                currentKey = startingKeys[keyIndex]
                startingKeys[keyIndex] = mapDict[currentKey][dir]
                if startingKeys[keyIndex].endswith('Z'):
                    if LCMs[keyIndex] == -1:
                        LCMs[keyIndex] = currentSteps
                        LCMsFound += 1
                    keysEndingInZ += 1

            stepIndex += 1
        if LCMsFound == len(LCMs):
            return math.lcm(*LCMs)

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day8.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))