def create_colors_dictionary():
    f = open("inputfile.7.txt", "r")
    colors = {}
    for l in f.readlines():
        l = l.strip()[:-1].split(' contain ')
        color = l[0][:-5]
        contents = []
        if l[1] != "no other bags":
            for i in l[1].split(', '):
                if int(i[0]) > 1:
                    contents.append(i[2:-5])
                else:
                    contents.append(i[2:-4])
        colors[color] = contents
    return colors

def explore_color(colors, color):
    if color in colors:
        contents = colors[color]
        count = 0
        for item in contents:
            if item == "shiny gold":
                count = 1
            else:
                count = max(count, explore_color(colors, item))
        return count
    return 0

def execute1():
    colors = create_colors_dictionary()
    count = 0
    for k in colors.keys():
        count += explore_color(colors, k)
    return count

def create_colors_dictionary2():
    f = open("inputfile.7.txt", "r")
    colors = {}
    for l in f.readlines():
        l = l.strip()[:-1].split(' contain ')
        color = l[0][:-5]
        contents = []
        if l[1] != "no other bags":
            for i in l[1].split(', '):
                n = int(i[0])
                if n > 1:
                    contents.append((n, i[2:-5]))
                else:
                    contents.append((n, i[2:-4]))
        else:
            contents.append((0, []))
        colors[color] = contents
    return colors

def print_level(level):
    return "-" * level

def explore_color2(colors, color, level):
    if color in colors:
        contents = colors[color]
        count = 0
        for c in contents:
            m = c[0]
            if m > 0:
                print("{0} Color {1} has {2} bags of color {3}".format(print_level(level), color, m, c[1]))
                count += m + (m * explore_color2(colors, c[1], level+1))
        return count
    return 0

def execute2():
    colors = create_colors_dictionary2()
    return explore_color2(colors, "shiny gold", 0)

if __name__ == "__main__":
    print(execute2())
