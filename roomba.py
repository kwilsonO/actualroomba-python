import sys 

dx = None
dy = None
source = None
dirs = None
dirtPos = None
allPos = None

def do_roomba():
    f = open("test.txt")
    
    data = f.readline()

    if len(data) < 3:
        sys.exit(0)

    i = 0
    for d in data:
        #parse input here

        if i == len(data) - 1:
            dirs = d

        if i <= 1:
            key, value = d.split(' ')

            if i == 0:
                dx = key
                dy = value
            if i == 1:
                source = (int(key), int(value))    

        dirtPos[d] = 1
        i = i + 1
    f.close()

    (finalPos, dirtCleaned) = CalcPos()
  
    print finalPos + "\n" + dirtCleaned

def CalcPos():

    last = source
    for c in dirs:
        if c == 'N':
            (xi, yi) = last
            last = (xi, yi + 1)
        if c == 'E':
            (xi, yi) = last
            last = (xi + 1, yi)
        if c == 'S':
            (xi, yi) = last
            last = (xi, yi - 1)
        if c == 'W':
            (xi, yi) = last
            last = (xi - 1, yi)

        if CheckPos(last) == 1:
            allPos.append(' '.join(last))

    return allPos.index(len(allPos) - 1), GetCleanSpots()

def GetCleanSpots():

    count = 0
    for p in allPos:
        if dirtPos[p] == 1:
            dirtPos[p] = 0
            count = count + 1

    return count

def CheckPos(point):

    (x, y) = point

    if (x >= 0 and x < dx) and (y >=0 and y < dy):
        return 1
    else:
        return 0


do_roomba()
