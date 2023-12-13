from AoCUtilities import *

def SolveMirror(dataBox : list):
    numRows = len(dataBox)
    numCols = len(dataBox[0])

    #It is a mirror if after the given index it is a mirror across teh value
    possibleXMirrorLocations = [True] * numCols
    possibleYMirrorLocations = [True] * numRows

    possibleXMirrorLocations[0] = False
    possibleYMirrorLocations[0] = False

    for rowIndex in range(numRows):
        for colIndex in range(numCols):
            currentVal = dataBox[rowIndex][colIndex]

            mirrorSpotX = colIndex + 1
            testColIndex = colIndex + 1
            while testColIndex < numCols:
                testVal = dataBox[rowIndex][testColIndex]
                if currentVal != testVal:
                    possibleXMirrorLocations[mirrorSpotX] = False
                testColIndex += 2
                mirrorSpotX += 1

            mirrorSpotY = rowIndex + 1
            testRowIndex = rowIndex + 1
            while testRowIndex < numRows:
                testVal = dataBox[testRowIndex][colIndex]
                if currentVal != testVal:
                    possibleYMirrorLocations[mirrorSpotY] = False
                testRowIndex += 2
                mirrorSpotY += 1

    if True in possibleXMirrorLocations:
        mirrorXIndex = possibleXMirrorLocations.index(True)
        value = mirrorXIndex
        return value
    if True in possibleYMirrorLocations:
        mirrorYIndex = possibleYMirrorLocations.index(True)
        value = mirrorYIndex
        value *= 100
        return value

    return 0

def SolveMirrorPart2(dataBox : list):
    numRows = len(dataBox)
    numCols = len(dataBox[0])

    #It is a mirror if after the given index it is a mirror across teh value
    possibleXMirrorLocations = [0] * numCols
    possibleYMirrorLocations = [0] * numRows

    for rowIndex in range(numRows):
        for colIndex in range(numCols):
            currentVal = dataBox[rowIndex][colIndex]

            mirrorSpotX = colIndex + 1
            testColIndex = colIndex + 1
            while testColIndex < numCols:
                testVal = dataBox[rowIndex][testColIndex]
                if currentVal != testVal:
                    possibleXMirrorLocations[mirrorSpotX] += 1
                testColIndex += 2
                mirrorSpotX += 1

            mirrorSpotY = rowIndex + 1
            testRowIndex = rowIndex + 1
            while testRowIndex < numRows:
                testVal = dataBox[testRowIndex][colIndex]
                if currentVal != testVal:
                    possibleYMirrorLocations[mirrorSpotY] += 1
                testRowIndex += 2
                mirrorSpotY += 1

    if 1 in possibleXMirrorLocations:
        mirrorXIndex = possibleXMirrorLocations.index(1)
        value = mirrorXIndex
        return value
    if 1 in possibleYMirrorLocations:
        mirrorYIndex = possibleYMirrorLocations.index(1)
        value = mirrorYIndex
        value *= 100
        return value

    return 0

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sums = 0
    dataBox = []
    for fileLine in fileData:
        if fileLine != '\n':
            dataBox.append(fileLine.strip())
        else:
            sums += SolveMirror(dataBox)
            dataBox = []

    sums += SolveMirror(dataBox)

    return sums

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sums = 0
    dataBox = []
    for fileLine in fileData:
        if fileLine != '\n':
            dataBox.append(fileLine.strip())
        else:
            sums += SolveMirrorPart2(dataBox)
            dataBox = []

    sums += SolveMirrorPart2(dataBox)

    return sums

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day13.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))