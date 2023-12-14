from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    cols = len(fileData[0].strip())
    rows = len(fileData)
    verticalArray = []
    for col in range(cols):
        column = []
        for row in range(rows):
            column.append(fileData[row][col])
        verticalArray.append(column)


    currentMinIndex = 0

    for y in range(len(verticalArray)):
        currentMinIndex = 0
        for x in range(len(verticalArray[0])):
            currentVal = verticalArray[y][x]
            if currentVal == '#':
                currentMinIndex = x + 1
                continue
            elif currentVal == 'O':
                if x != currentMinIndex:
                    verticalArray[y][x] = '.'
                    verticalArray[y][currentMinIndex] = 'O'
                currentMinIndex = currentMinIndex + 1


    sumScores = 0
    for y in range(len(verticalArray)):
        for x in range(len(verticalArray[0])):
            currentVal = verticalArray[y][x]
            if currentVal == 'O':
                sumScores += rows - x

    return sumScores

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    return 0

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day14.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))