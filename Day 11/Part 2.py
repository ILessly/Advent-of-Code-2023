#Advent of Code Day 11 Part 2

import math

input = open(r"Day 11\input.txt", "r")
inputlist = input.readlines()

#print(inputlist)

rawmap = []
for y in inputlist:
    y = y.strip()
    row = []
    for col in y:
        row.append(col)
    rawmap.append(row)

def PrintMap(map):
    i = 0
    for row in map:
        line = "Row " + str(i) + ":    "[0:0-len(str(i))]
        for col in row:
            line += col
        print(line)
        i += 1

def AddRows(map):
    emptyrows = []
    for row in range(len(map)):
        if "#" not in rawmap[row]:
            emptyrows.append(row) 
    #print("Empty rows:", emptyrows)
    blankrow = []
    for i in range(len(map[0])):
        blankrow.append("0")
    # for i in emptyrows:
    #     index = emptyrows.index(i)
    #     map.insert(i+1+index, blankrow)
    return map, emptyrows

def AddCols(map):
    emptycols = []
    for y in range(len(map[0])):
        column = []
        for x in range(len(map)):
            column.append(map[x][y])
        if "#" not in column:
            emptycols.append(y)
    #print("Empty columns:", emptycols)
    # for y in range(len(map)):
    #     for x in emptycols:
    #         index = emptycols.index(x)
    #         map[y].insert(x+1+index, "0")
    return map, emptycols

def ExpandMap(map):
    print("Adding columns...")
    map, emptycols = AddCols(map)
    print("Done!")
    print("Adding rows...")
    map, emptyrows = AddRows(map)
    print("Done!")
    
    return map, emptyrows, emptycols
 
def GetGalaxies(map):
    galaxies = []
    galnum = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "#":
                #print("Found galaxy!", row, col)
                galaxies.append([row, col])
    return galaxies

def FindDistance(g1, g2):
    #print(g1)
    #print(g2)
    dist = abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
    #print("Distance:", dist)
    return dist
    

print("Expanding map...")
map, emptyrows, emptycols = ExpandMap(rawmap)

print("Retrieving galaxies...")
galaxies = GetGalaxies(map)
print("Done!")

total = 0
expansion_factor = 1000000

while galaxies:
    #print("Rows:", emptyrows)
    #print("Cols:", emptycols)
    g1 = galaxies[0]
    galaxies.pop(0)
    for g2 in galaxies:
        crossed_rows = 0
        crossed_cols = 0
        #print("Getting distance from:", g1, "to", g2)

        if g1[0] < g2[0]:
            r1 = g1[0]
            r2 = g2[0]
        else:
            r1 = g2[0]
            r2 = g1[0]
        for row in emptyrows:
            if r1 < row < r2:
                #print("Crosses row:", row)
                crossed_rows += 1
        #print("Check columns...")
        if g1[1] < g2[1]:
            c1 = g1[1]
            c2 = g2[1]
        else:
            c1 = g2[1]
            c2 = g1[1]
        for col in emptycols:
            if c1 < col < c2:
                crossed_cols += 1
        
        dist = FindDistance(g1, g2)
        
        #print("Crossed rows:", crossed_rows)
        #print("Crossed cols:", crossed_cols)
        extra_crossings = (crossed_rows + crossed_cols)*(expansion_factor-1)
        dist += extra_crossings
        #print("Distance is:", dist)
        total += dist

print(total)
          
