from collections import Counter

def execute(charInc, lineInc):
    f = open("inputfile.3.txt", "r")
    charIdx, lineIdx = 0, 0
    treeCount = 0
    lines = f.readlines()
    while lineIdx < len(lines):
        l = lines[lineIdx].strip()
        if l[charIdx] == '#':
            treeCount += 1
        
        lineIdx += lineInc
        charIdx = (charIdx + charInc) % len(l)

    return treeCount

def execute1():
    return execute(3,1)

def execute2():
    return execute(1,1) * execute(3,1) * execute(5,1) * execute(7,1) * execute(1,2)

if __name__ == "__main__":
    print(execute2())
