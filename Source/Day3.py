from AoCUtilities import *

def IsSymbol(char : str) -> bool:
    if char.isnumeric():
        return False
    if char == '.':
        return False
    if char == '\n':
        return False
    return True

def GetFirstNumFromStr(fileLine : str, startIndex):
    numStartIndex = -1
    number = -1
    numEndIndex = len(fileLine) - 1

    for currentIndex in range(startIndex, len(fileLine)):
        char = fileLine[currentIndex]
        if char.isnumeric():
            if numStartIndex == -1:
                numStartIndex = currentIndex
        elif numStartIndex != -1:
            numEndIndex = currentIndex-1

        if numEndIndex != len(fileLine) - 1:
            break

    if numStartIndex == -1:
        return (numStartIndex, numEndIndex, number)

    number = int(fileLine[numStartIndex:numEndIndex+1])

    return (numStartIndex, numEndIndex, number)

def IsTouchingSymbol(colStart : int, colEnd : int, rowIndex : int, fileData : list) -> bool:

    startColIndex = max(colStart - 1, 0)
    endColIndex = min(colEnd + 2, len(fileData[0]))
    startRowIndex = max(rowIndex - 1, 0)
    endRowIndex = min(rowIndex + 2, len(fileData))

    for colIndex in range(startColIndex, endColIndex):
        for rowIndex in range(startRowIndex, endRowIndex):
            if IsSymbol(fileData[rowIndex][colIndex]):
                return True
    return False

def GetNumberContainingIndex( rowIndex : int, colIndex: int, fileData : list) -> tuple:

    fileLine = fileData[rowIndex]

    char = fileLine[colIndex]
    if not char.isnumeric():
        return -1, -1, -1

    startIndex = colIndex
    endIndex = colIndex

    while IsValidIndex(fileLine, startIndex-1) and fileLine[startIndex-1].isnumeric():
        startIndex -= 1


    while IsValidIndex(fileLine, endIndex+1) and fileLine[endIndex+1].isnumeric():
        endIndex += 1

    number = int(fileLine[startIndex:endIndex+1])

    'startIndex, endIndex, number'
    return startIndex, endIndex, number

def IsIndexAGear(rowIndex : int, colIndex : int, fileData : list):
    gearRatio = 0
    firstNum = -1
    secondNum = -1

    startColIndex = max(colIndex - 1, 0)
    endColIndex = min(colIndex + 2, len(fileData[0]))
    startRowIndex = max(rowIndex - 1, 0)
    endRowIndex = min(rowIndex + 2, len(fileData))

    rowIndex = startRowIndex
    while rowIndex < endRowIndex:
        colIndex = startColIndex
        while colIndex < endColIndex:
            char = fileData[rowIndex][colIndex]
            indexData = GetNumberContainingIndex(rowIndex, colIndex, fileData)
            startNumColIndex = indexData[0]
            endNumColIndex = indexData[1]
            number = indexData[2]
            if indexData[2] != -1:
                if firstNum == -1:
                    firstNum = number
                elif secondNum == -1:
                    secondNum = number
                else:
                    return False, 0
                colIndex = endNumColIndex
            colIndex += 1
        rowIndex += 1

    if firstNum != -1 and secondNum != -1:
        return True, firstNum*secondNum
    else:
        return False, 0

def GetGearSumInLine(rowIndex : int, fileData : list):
    gearSum = 0
    fileLine = fileData[rowIndex]
    rowLength = len(fileLine)
    for colIndex in range(0, rowLength):
        char = fileLine[colIndex]
        if char == '*':
            gearData = IsIndexAGear(rowIndex, colIndex, fileData)
            if gearData[0]:
                gearSum += gearData[1]
    return gearSum

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

        currentSum = 0
        lineIndex = 0
        while lineIndex < len(fileData):
            fileLine = fileData[lineIndex].strip()

            colIndex = 0
            while colIndex < len(fileData[0]):
                firstNumData = GetFirstNumFromStr(fileLine, colIndex)
                startIndex = firstNumData[0]
                endIndex = firstNumData[1]
                number = firstNumData[2]
                if startIndex == -1:
                    colIndex += 1
                    continue
                else:
                    if IsTouchingSymbol(startIndex, endIndex, lineIndex, fileData):
                        currentSum += number
                    colIndex = endIndex + 1
            lineIndex += 1
    return currentSum

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    gearSum = 0
    rowIndex = 0
    for rowIndex in range(0, len(fileData)):
        gearSum += GetGearSumInLine(rowIndex, fileData)
    return gearSum

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day3.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))