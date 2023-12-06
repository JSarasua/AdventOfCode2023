from AoCUtilities import *

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    seeds = [int(x) for x in fileData[0].split(':')[1].strip().split(' ')]

    listOfMaps = []

    currentMap = []
    for fileLine in fileData:
        if fileLine.startswith('seeds: '):
            continue
        if fileLine.strip() == '':
            if currentMap != []:
                listOfMaps.append(currentMap)
                currentMap = []
        elif not fileLine[0].isnumeric():
            continue
        else:
            mapping = [int(x) for x in fileLine.strip().split(' ')]
            currentMap.append(mapping)

    if currentMap != []:
        listOfMaps.append(currentMap)

    for mapping in listOfMaps:
        seedIndex = 0
        for seedIndex in range(len(seeds)):
            seed = seeds[seedIndex]
            for map in mapping:
                startSource = map[1]
                endSource = startSource + map[2] #Dont need to subtract one since doing a range right after
                startDest = map[0]
                diff = startDest - startSource
                if seed in range(startSource, endSource):
                    seed += diff
                    seeds[seedIndex] = seed
                    break

    minSeed = min(seeds)
    return minSeed


def TranslateRanges(startingRanges : list, mappingRanges : list) -> list:


    newRanges = []

    startingIndex = 0
    while startingIndex < len(startingRanges):
        startingRange = startingRanges[startingIndex]

        startVal = startingRange[0]
        endStartVal = startingRange[1]

        didHandleCurrentRange = False

        for mappingRange in mappingRanges:
            mapRange = (mappingRange[0], mappingRange[1])
            mapDiff = mappingRange[2]
            if endStartVal < mapRange[0]: #Range is in front of map, skip
                continue
            if startVal > mapRange[1]: #Range is behind map, skip
                continue
            if startVal >= mapRange[0] and endStartVal <= mapRange[1]: #Fully enclosed, diff all and move on
                newRange = [startVal + mapDiff, endStartVal + mapDiff]
                newRanges.append(newRange)
                didHandleCurrentRange = True
                break

            if startVal < mapRange[0] and endStartVal <= mapRange[1]: #Front half is not in, diff back half, all cases handled
                newStartRange = [startVal, mapRange[0] - 1]
                startingRanges.append(newStartRange)

                newMappedRange = [mapRange[0] + mapDiff, endStartVal + mapDiff]
                newRanges.append(newMappedRange)
                didHandleCurrentRange = True
                break

            if startVal >= mapRange[0] and endStartVal > mapRange[1]: #Front half is in, back half is not, all cases handled
                newStartRange = [mapRange[1] + 1, endStartVal]
                startingRanges.append(newStartRange)

                newMappedRange = [startVal + mapDiff, mapRange[1] + mapDiff]
                newRanges.append(newMappedRange)
                didHandleCurrentRange = True
                break

            if startVal < mapRange[0] and endStartVal > mapRange[1]: #map is inside, add two new ranges, split off old range, all cases handled
                newStartRangeFront = [startVal, mapRange[0] - 1]
                newStartRangeBack = [mapRange[1] + 1, endStartVal]
                startingRanges.append(newStartRangeFront)
                startingRanges.append(newStartRangeBack)

                newMappedRange = [mapRange[0] + mapDiff, mapRange[1] + mapDiff]
                newRanges.append(newMappedRange)
                didHandleCurrentRange = True
                break
        if not didHandleCurrentRange:
            existingRange = [startVal, endStartVal]
            newRanges.append(existingRange)
        startingIndex += 1

    return newRanges

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    seedNums = [int(x) for x in fileData[0].split(':')[1].strip().split(' ')]

    seedRanges = []

    numIndex = 0
    while numIndex < len(seedNums):
        seedStart = seedNums[numIndex]
        seedCount = seedNums[numIndex + 1]
        seedEnd = seedStart + seedCount - 1
        seedRanges.append((seedStart,seedEnd))
        numIndex += 2

    listOfMaps = []

    currentMap = []
    for fileLine in fileData:
        if fileLine.startswith('seeds: '):
            continue
        if fileLine.strip() == '':
            if currentMap != []:
                listOfMaps.append(currentMap)
                currentMap = []
        elif not fileLine[0].isnumeric():
            continue
        else:
            mapping = [int(x) for x in fileLine.strip().split(' ')]
            startVal = mapping[1]
            endVal = startVal + mapping[2] - 1
            diff = mapping[0] - startVal
            mapping = [startVal, endVal, diff]
            currentMap.append(mapping)

    if currentMap != []:
        listOfMaps.append(currentMap)

    for mapping in listOfMaps:
        seedRanges = TranslateRanges(seedRanges, mapping)

    minSeed = min([x[0] for x in seedRanges])

    return minSeed

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day5.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))