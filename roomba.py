import sys 

dirtPos = {}
allPos = []
dx = -1
dy = -1
source = (-1, -1)
dirs = ""
def do_roomba():
    f = open("test.txt")
    
    data = f.read().split("\n")
    data = data[ 1 : -1 ]

    if len(data) < 3:
        sys.exit(0)

    i = 0
    for d in data:
        #parse input here
        if i == (len(data) - 1):
            dirs = d
        elif i <= 1:
            key, value = d.split(' ')

            if i == 0:
                dx = int(key)
                dy = int(value)
            elif i == 1:
                source = (int(key), int(value))    
        else:
            dirtPos[d] = 1
        i = i + 1
    print i
    print dirtPos
    f.close()
    (finalPos, dirtCleaned) = CalcPos()
  
    print finalPos + "\n" + str(dirtCleaned)

def CalcPos():
    
    last = source
    print dirs
    for c in dirs:
        print c
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
        
        (xf, yf) = last

        allPos.append(str(xf) + " " + str(yf))

    (xPos, yPos) = last
    return (str(xPos) + " " + str(yPos), GetCleanSpots())

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
