from AoCUtilities import *

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
def isWordNumber(word):
    if word in numbers:
        return True
    return False

def getNumberStartingWith(word : str):
    number = -1
    for index in range(0, len(numbers)):
        numberWord = numbers[index]
        if word.startswith(numberWord):
            number = index
    return number


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumTotal = 0

    for fileLine in fileData:
        charString = ""
        lastDigit = ""
        for char in fileLine:
            if char.isnumeric():
                if charString == "":
                    charString += char

                lastDigit = char

        charString += lastDigit
        if(charString.isnumeric()):
            sumTotal += int(charString)

    return sumTotal

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumTotal = 0

    for fileLine in fileData:
        charString = ""
        lastDigit = ""
        for charIndex in range(0, len(fileLine)):
            char = fileLine[charIndex]

            if char.isnumeric():
                lastDigit = char
                if charString == "":
                    charString += lastDigit

            else:
                fileLineSubStr = fileLine[charIndex:len(fileLine)]
                number = getNumberStartingWith(fileLineSubStr)
                if number != -1:
                    lastDigit = str(number)
                    if charString == "":
                        charString += lastDigit




        charString += lastDigit
        sumTotal += int(charString)

    return sumTotal

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day1.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))