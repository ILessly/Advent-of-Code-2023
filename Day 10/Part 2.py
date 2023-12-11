#Advent of Code Day 10 Part 2

input = open(r"Day 10\input.txt", "r")
inputlist = input.readlines()

map = []
for y in inputlist:
    y = y.strip()
    row = []
    for x in y:
        row.append(x)
    map.append(row)

def PrintMap():
    for row in map:
        line=""
        for col in row:
            line += col
            # if col in "SUDO":
            #     line += col
            # else:
            #     line += "."
        print(line)

def FindArea():
    area = 0
    for row in map:
        in_loop = False
        on_line = False
        corners = 0
        for col in row:
            if in_loop:
                if col == "D":
                    in_loop = False
                if col not in "UD":
                    area += 1
            if not in_loop:
                if col == "U":
                    in_loop = True
            #print(col, in_loop)
    print(area)
                 

def FindStart():
    for row in map:
        for col in row:
            if col == "S":
                print("Start found!", map.index(row), row.index(col))
                return map.index(row), row.index(col)

def FirstStep(y, x):
    if y>0 and map[y-1][x] in "7|F": #Check above
        return "up"
    
    if x<len(row) and map[y][x+1] in "7-J":
        return "right"
    
    if y<len(inputlist) and map[y+1][x] in "J|L":
        return "left"

    if x>0 and map[y][x-1] in "F-L":
        return "down"

def Move(dir_to, y, x):
    moves = {"up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]}
    
    up = {"7": "left", "|": "up", "F": "right"}
    right = {"7": "down", "-": "right", "J": "up"}
    down = {"J": "left", "|": "down", "L": "right"}
    left = {"F": "down", "-": "left", "L": "up"}
    
    go = {"up": up, "right": right, "down": down, "left": left}
    
    char = map[y][x]
    nextchar = map[y+moves[dir_to][0]][x+moves[dir_to][1]]
    y = y+moves[dir_to][0]
    x = x+moves[dir_to][1]

    #print("On", char, "Moving", dir_to, "to", nextchar)
    
    # dir_to = map[y][x]
    
    # if dir_to is "up":
    #     dir_to = "U"
    # elif dir_to is "down":
    #     dir_to = "D"
    
    # map[y][x] = dir_to
    
    if nextchar in "UD":
        print("Back to start!")
        return "done", x, y, nextchar

    return go[dir_to][nextchar], x, y, nextchar
    
steps = 0
y, x = FindStart()
dir_to = FirstStep(y,x)
#print("Starting on S, moving", dir_to)
map[y][x] = "J"
char = "J"
dirletter = "U"
#dir_to, x, x, char = Move(dir_to, y, x)

while char not in "UD":
    steps += 1
    dir_to, x, y, char = Move(dir_to, y, x)
    if dir_to is "up":
        dirletter = "U"
    if dir_to is "down":
        dirletter = "D"
    map[y][x] = dirletter

    
print("Completed in", steps, "steps")
furthestpoint = int(steps/2)
print("Furthest point:", furthestpoint, "steps")

PrintMap()
FindArea()


