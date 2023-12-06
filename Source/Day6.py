from AoCUtilities import *

def GetDist(time : int, speed: int):
    return speed * time

def DoesGoFartherThanRecord(time : int, speed: int, recordDist : int):
    return GetDist(time, speed) > recordDist



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    timeData = fileData[0].split(':')[1].strip().split(' ')
    distData = fileData[1].split(':')[1].strip().split(' ')
    times = [int(x) for x in [x.strip() for x in timeData] if x ]
    dists = [int(x) for x in [x.strip() for x in distData] if x ]

    waysYouBeatRecord = 1

    index = 0
    for index in range(len(times)):
        maxTime = times[index]
        recordDist = dists[index]

        currentRaceMargins = 0
        for time in range(maxTime):
            remainingTime = maxTime - time
            speed = time
            if DoesGoFartherThanRecord(remainingTime, speed, recordDist):
                currentRaceMargins += 1
        waysYouBeatRecord *= currentRaceMargins

    return waysYouBeatRecord

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    maxTime = int(fileData[0].split(':')[1].strip().replace(' ', ''))
    recordDist = int(fileData[1].split(':')[1].strip().replace(' ', ''))

    waysYouBeatRecord = 1
    currentRaceMargins = 0
    for time in range(maxTime):
        remainingTime = maxTime - time
        speed = time
        if DoesGoFartherThanRecord(remainingTime, speed, recordDist):
            currentRaceMargins += 1
    waysYouBeatRecord *= currentRaceMargins

    return waysYouBeatRecord

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day6.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))