import re

def validate1(passport):
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

def checkDigit(item, digits, min, max):
    return item.isdigit() and len(item) == digits and int(item) >= min and int(item) <= max

def validate2(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    if validate1(passport):
        validBYR = checkDigit(passport["byr"], 4, 1920, 2020)
        validIYR = checkDigit(passport["iyr"], 4, 2010, 2020)
        validEYR = checkDigit(passport["eyr"], 4, 2020, 2030)
        hgtUnit = passport["hgt"][-2:]
        hgtDigits = int(passport["hgt"][:-2]) if passport["hgt"][:-2].isdigit() else 0
        validHGT = (hgtUnit == "cm" and hgtDigits >= 150 and hgtDigits <= 193) or (hgtUnit == "in" and hgtDigits >= 59 and hgtDigits <= 76)
        validHCL = re.fullmatch('^#[a-f0-9]{6}$', passport["hcl"]) != None
        validECL = passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        validPID = passport["pid"].isdigit() and len(passport["pid"]) == 9
        print('Validation validBYR: {0}, validIYR: {1}, validEYR: {2}, validHGT: {3} , validHCL: {4}, validECL: {5}, validPID: {6}'.format(validBYR, validIYR, validEYR, validHGT, validHCL, validECL, validPID))
        return validBYR and validIYR and validEYR and validHGT and validHCL and validECL and validPID
    return False

def execute(validate):
    f = open("inputfile.4.txt", "r")
    count = 0
    passport = {}
    for l in f.readlines():
        print("Line: " + l.strip())
        if len(l.strip()) == 0:
            # Check passport
            valid = validate(passport)
            print('Checking passport {0}{1}{2}'.format(passport.keys(), passport.values(), "--> VALID" if valid else "--> INVALID"))
            if valid:
                count += 1
            passport = {}
        else:
            items = l.strip().split(' ')
            for i in items:
                ii = i.split(':')
                passport[ii[0]] = ii[1]

    # Check the last passport
    valid = validate(passport)
    print('Checking passport {0}{1}{2}'.format(passport.keys(), passport.values(), "--> VALID" if valid else "--> INVALID"))
    if valid:
        count += 1
    return count

if __name__ == "__main__":
    print(execute(validate2))
