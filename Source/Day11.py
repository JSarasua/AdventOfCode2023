from AoCUtilities import *
import re

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()



    rowWeights = [2] * len(fileData)
    colWeights = [2] * len(fileData[0])

    galaxyLocations = []

    rowIndex = 0
    while rowIndex < len(fileData):
        fileLine = fileData[rowIndex]
        galaxyIndices = [m.start() for m in re.finditer('#', fileLine)]

        for colIndex in galaxyIndices:
            rowWeights[rowIndex] = 1
            colWeights[colIndex] = 1
            galaxyLocations.append((colIndex,rowIndex))

        rowIndex += 1

    galaxyPairs = []

    tempGalaxyLocations = galaxyLocations
    galaxyIndex = 0
    while galaxyIndex < len(tempGalaxyLocations) - 1:
        currentGalaxy = tempGalaxyLocations[galaxyIndex]
        for nextGalaxyIndex in range(galaxyIndex + 1, len(tempGalaxyLocations)):
            nextGalaxy = tempGalaxyLocations[nextGalaxyIndex]
            galaxyPair = currentGalaxy,nextGalaxy
            galaxyPairs.append(galaxyPair)

        tempGalaxyLocations.pop(0)

    sumDists = 0
    for galaxyPair in galaxyPairs:
        galaxy1 = galaxyPair[0]
        galaxy2 = galaxyPair[1]

        minX = min(galaxy1[0],galaxy2[0])
        maxX = max(galaxy1[0],galaxy2[0])
        minY = min(galaxy1[1],galaxy2[1])
        maxY = max(galaxy1[1],galaxy2[1])

        rowDist = sum(rowWeights[minY:maxY])
        colDist = sum(colWeights[minX:maxX])
        totalDist = rowDist + colDist
        sumDists += totalDist

    return sumDists

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()



    rowWeights = [1000000] * len(fileData)
    colWeights = [1000000] * len(fileData[0])

    galaxyLocations = []

    rowIndex = 0
    while rowIndex < len(fileData):
        fileLine = fileData[rowIndex]
        galaxyIndices = [m.start() for m in re.finditer('#', fileLine)]

        for colIndex in galaxyIndices:
            rowWeights[rowIndex] = 1
            colWeights[colIndex] = 1
            galaxyLocations.append((colIndex,rowIndex))

        rowIndex += 1

    galaxyPairs = []

    tempGalaxyLocations = galaxyLocations
    galaxyIndex = 0
    while galaxyIndex < len(tempGalaxyLocations) - 1:
        currentGalaxy = tempGalaxyLocations[galaxyIndex]
        for nextGalaxyIndex in range(galaxyIndex + 1, len(tempGalaxyLocations)):
            nextGalaxy = tempGalaxyLocations[nextGalaxyIndex]
            galaxyPair = currentGalaxy,nextGalaxy
            galaxyPairs.append(galaxyPair)

        tempGalaxyLocations.pop(0)

    sumDists = 0
    for galaxyPair in galaxyPairs:
        galaxy1 = galaxyPair[0]
        galaxy2 = galaxyPair[1]

        minX = min(galaxy1[0],galaxy2[0])
        maxX = max(galaxy1[0],galaxy2[0])
        minY = min(galaxy1[1],galaxy2[1])
        maxY = max(galaxy1[1],galaxy2[1])

        rowDist = sum(rowWeights[minY:maxY])
        colDist = sum(colWeights[minX:maxX])
        totalDist = rowDist + colDist
        sumDists += totalDist

    return sumDists

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day11.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))