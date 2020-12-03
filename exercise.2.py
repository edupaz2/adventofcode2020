from collections import Counter

def execute1():
    f = open("inputfile.2.txt", "r")
    count = 0
    for l in f.readlines():
        items = l.split(" ")
        limits = items[0].split("-")
        min, max = int(limits[0]), int(limits[1])
        letter = items[1][0]
        counter = Counter(items[2])
        times = counter[letter]
        if times >= min and times <= max:
            count += 1

    return count

def execute2():
    f = open("inputfile.2.txt", "r")
    count = 0
    for l in f.readlines():
        items = l.split(" ")
        limits = items[0].split("-")
        pos1, pos2 = int(limits[0]) - 1, int(limits[1]) - 1
        letter = items[1][0]
        password = items[2]
        pos1Match = password[pos1] == letter
        pos2Match = password[pos2] == letter
        if pos1Match != pos2Match:
            count += 1

    return count

if __name__ == "__main__":
    print(execute2())
