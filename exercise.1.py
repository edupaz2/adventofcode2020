

def execute1():
    f = open("inputfile.1.txt", "r")
    lines = f.readlines()
    for i, l in enumerate(lines):
        for ll in lines[i:]:
            if int(l) + int(ll) == 2020:
                return int(l) * int(ll)
    return -1

def execute2():
    f = open("inputfile.1.txt", "r")
    lines = f.readlines()
    for i, l in enumerate(lines):
        intl = int(l)
        for ii, ll in enumerate(lines[i:]):
            intll = int(ll)
            for lll in lines[ii:]:
                if intl + intll + int(lll) == 2020:
                    return intl * intll * int(lll)
    return -1

if __name__ == "__main__":
    print(execute2())
