def execute1():
    f = open("inputfile.6.txt", "r")
    count = 0
    answers = set()
    for l in f.readlines():
        #print("Line: " + l.strip())
        l = l.strip()
        if len(l) == 0:
            # Count answers
            print("Adding {0} {1} to count: {2}".format(answers, len(answers), count))
            count += len(answers)
            answers = set()
        else:
            for c in l:
                answers.add(c)

    # Count the last set
    count += len(answers)
    return count

def execute2():
    f = open("inputfile.6.txt", "r")
    count = 0
    answers = None
    for l in f.readlines():
        l = l.strip()
        if len(l) == 0:
            # Count answers
            count += len(answers)
            print("Adding: {0} to count: {1}, answers: {2}".format(len(answers), count, answers))
            answers = None
        else:
            if answers == None:
                answers = [c for c in l]
            else:
                answers = [c for c in l if c in answers]

    # Count the last set
    count += len(answers)
    print("Adding: {0} to count: {1}, answers: {2}".format(len(answers), count, answers))
    return count


if __name__ == "__main__":
    print(execute2())
