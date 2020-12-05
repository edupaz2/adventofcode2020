
def getRow(sequence):
    start = 0
    total = 128
    for c in sequence:
        total /= 2
        if c == 'B':
            start = start + total
    return int(start)

def getSeat(sequence):
    start = 0
    total = 8
    for c in sequence:
        total /= 2
        if c == 'R':
            start = start + total
    return int(start)

def execute1():
    f = open("inputfile.5.txt", "r")
    maxCheck = 0
    for l in f.readlines():
        row = getRow(l[:7])
        seat = getSeat(l[7:])
        boardingPass = row*8+seat
        print("Line: {0}  -> {1} {2} {3}".format(l.strip(), row, seat, boardingPass))
        if boardingPass > maxCheck:
            maxCheck = boardingPass
    return maxCheck

def execute2():
    f = open("inputfile.5.txt", "r")
    allseats = [i for i in range(0, 127*8+7)]
    seats = []
    for l in f.readlines():
        row = getRow(l[:7])
        seat = getSeat(l[7:])
        boardingPass = row*8+seat
        seats.append(boardingPass)
        print("Line: {0}  -> {1} {2} {3}".format(l.strip(), row, seat, boardingPass))
    return [i for i in allseats if i not in seats]

if __name__ == "__main__":
    print(execute2())
