from AoCUtilities import *

def SolveWord(word : str):
    currentValue = 0
    for char in word:
        if char == '\n':
            continue
        currentValue += ord(char)
        currentValue *= 17
        currentValue = currentValue % 256
    return currentValue


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sum = 0
    for fileLine in fileData:
        chunks = fileLine.strip().split(',')
        for chunk in chunks:
            sum += SolveWord(chunk)

    return sum

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    hashMap = [[] for x in range(256)]
    sum = 0
    for fileLine in fileData:
        chunks = fileLine.strip().split(',')
        for chunk in chunks:
            if '=' in chunk:
                word,fl = chunk.split('=')
                hash = SolveWord(word)
                doesExist = False
                for lensIndex in range(len(hashMap[hash])):
                    lensHash = hashMap[hash][lensIndex][0]
                    if lensHash == word:
                        hashMap[hash][lensIndex] = (word,fl)
                        doesExist = True
                        break
                if not doesExist:
                    hashMap[hash].append((word,fl))
            if '-' in chunk:
                word = chunk.split('-')[0]
                hash = SolveWord(word)
                for lens in hashMap[hash]:
                    if lens[0].startswith(word):
                        hashMap[hash].remove(lens)

    for hashIndex in range(len(hashMap)):
        slots = len(hashMap[hashIndex])
        if slots == 0:
            continue
        boxNum = 1 + hashIndex
        for slotIndex in range(slots):
            slot = 1 + slotIndex
            focalLength = hashMap[hashIndex][slotIndex][1]
            sum += boxNum * slot * int(focalLength)

    return sum

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day15.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))