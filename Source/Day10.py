from AoCUtilities import *

left = (-1,0)
right = 1,0
up = 0,-1
down = 0,1
invalid = 0,0

def IsValidUpPipe(pipe : str):
    validPipes = ['|', '7', 'F']
    return pipe in validPipes

def IsValidDownPipe(pipe : str):
    validPipes = ['|', 'L', 'J']
    return pipe in validPipes

def IsValidLeftPipe(pipe : str):
    validPipes = ['-', 'L', 'F']
    return pipe in validPipes

def IsValidRightPipe(pipe : str):
    validPipes = ['-', '7', 'J']
    return pipe in validPipes

def MovDir(startPos : tuple, dir : tuple):
    return startPos[0] + dir[0], startPos[1] + dir[1]

def GetDir(pipe : str, inDir : tuple):
    if inDir == left:
        if pipe == '-':
            return left
        elif pipe == 'L':
            return up
        elif pipe == 'F':
            return down
    elif inDir == right:
        if pipe == '-':
            return right
        elif pipe == '7':
            return down
        elif pipe == 'J':
            return up
    elif inDir == up:
        if pipe == '7':
            return left
        elif pipe == 'F':
            return right
        elif pipe =='|':
            return up
    elif inDir == down:
        if pipe == '|':
            return down
        elif pipe == 'L':
            return right
        elif pipe == 'J':
            return left

    return invalid

def GetPipe(fileData : list, pos : tuple):
    row = fileData[pos[1]]
    pipe = row[pos[0]]
    return pipe

def GetDirFromData(fileData : list, pos : tuple, inDir : tuple):
    pipe = GetPipe( fileData, pos)
    return GetDir(pipe, inDir)

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sRow = -1
    sCol = -1

    while sRow == -1 and sCol == -1:
        for currentRowIndex in range(len(fileData)):
            fileLine = fileData[currentRowIndex]
            sCol = fileLine.find('S')
            if sCol != -1:
                sRow = currentRowIndex
                break

    startPoint = sCol, sRow
    startingDirs = []

    upSpot = MovDir(startPoint, up)
    downSpot = MovDir(startPoint, down)
    leftSpot = MovDir(startPoint, left)
    rightSpot = MovDir(startPoint, right)

    upPipe = fileData[upSpot[1]][upSpot[0]]
    downPipe = fileData[downSpot[1]][downSpot[0]]
    leftPipe = fileData[leftSpot[1]][leftSpot[0]]
    rightPipe = fileData[rightSpot[1]][rightSpot[0]]

    if IsValidUpPipe(upPipe):
        startingDirs.append(up)
    if IsValidDownPipe(downPipe):
        startingDirs.append(down)
    if IsValidLeftPipe(leftPipe):
        startingDirs.append(left)
    if IsValidRightPipe(rightPipe):
        startingDirs.append(right)

    currentDirs = startingDirs
    currentPoints = [startPoint, startPoint]
    moves = 0
    while currentPoints[0] != currentPoints[1] or currentPoints[0] == startPoint:
        firstPos = currentPoints[0]
        firstDirs = currentDirs[0]

        nextPosFirst = MovDir(firstPos, firstDirs)
        currentPipeFirst = GetPipe(fileData, nextPosFirst)
        nextDirsFirst = GetDirFromData(fileData, nextPosFirst, firstDirs)
        currentPoints[0] = nextPosFirst
        currentDirs[0] = nextDirsFirst

        secondPos = currentPoints[1]
        secondDirs = currentDirs[1]

        nextPosSecond = MovDir(secondPos, secondDirs)
        currentPipeSecond = GetPipe(fileData, nextPosSecond)
        nextDirsSecond = GetDirFromData(fileData, nextPosSecond, secondDirs)
        currentPoints[1] = nextPosSecond
        currentDirs[1] = nextDirsSecond
        moves += 1


    return moves

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    return 0

filePath = "C:\\dev\\AdventOfCode2023\\Input\\Day10.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))