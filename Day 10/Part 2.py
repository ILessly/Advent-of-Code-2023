#Advent of Code Day 10 Part 2

input = open(r"Day 10\example2.txt", "r")
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
            if col in "SVHC":
                line += col
            else:
                line += "."
        print(line)

def FindArea():
    area = 0
    for row in map:
        in_loop = False
        on_line = False
        corners = 0
        for col in row:
            if row.count("V") == 0:
                continue
            if col is "C" and corners != 2:
                corners += 1
            elif col is "C" and corners == 2:
                corners = 0
            if not in_loop:
               if col == "V" or corners == 2:
                   in_loop = True 
            elif in_loop:
                if col == "V" or corners == 2:
                    in_loop = False
                if col == ".":
                    area += 1
                    #print(map.index(row), row.index(col), col)
            print(col, in_loop)
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

def Move(dir, y, x):
    # map[y][x] = "O"
    moves = {"up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]}
    
    up = {"7": "left", "|": "up", "F": "right"}
    right = {"7": "down", "-": "right", "J": "up"}
    down = {"J": "left", "|": "down", "L": "right"}
    left = {"F": "down", "-": "left", "L": "up"}
    
    go = {"up": up, "right": right, "down": down, "left": left}
    
    char = map[y+moves[dir][0]][x+moves[dir][1]]
    y = y+moves[dir][0]
    x = x+moves[dir][1]
    if char is "S":
        if dir in "up or down":
           map[y][x] = "C"
        else:
            map[y][x] = "H" 
        return "done", x, y, char
    #print("Moving", dir)
    #print("On", char, "can only go", go[dir][char])
    if map[y][x] == "-":
        map[y][x] = "H"
    elif map[y][x] == "|":
        map[y][x] = "V"
    else:
        map[y][x] = "C"
    
    return go[dir][char], x, y, char
    
steps = 0
y, x = FindStart()
dir = FirstStep(y,x)
char = "s"
while char not in "SVHC":
    #print(steps)
    steps += 1
    dir, x, y, char = Move(dir, y, x)
    
print("Completed in", steps, "steps")
furthestpoint = int(steps/2)
print("Furthest point:", furthestpoint, "steps")

PrintMap()
FindArea()


