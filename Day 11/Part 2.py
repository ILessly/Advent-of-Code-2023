#Advent of Code Day 11 Part 2

import math

input = open(r"Day 11\example.txt", "r")
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

def AddRows(map, extra):
    emptyrows = []
    for row in range(len(map)):
        if "#" not in rawmap[row]:
            emptyrows.append(row) 
    #print("Empty rows:", emptyrows)
    blankrow = []
    for i in range(len(map[0])):
        blankrow.append("0")
    for i in emptyrows:
        for r in range(extra):
            index = emptyrows.index(i)
            map.insert(i+1+index*extra, blankrow)
            print(r, "Adding", str(index+1) + "/" + str(len(emptyrows)), end="\r")
    return map

def AddCols(map, extra):
    emptycols = []
    for y in range(len(map[0])):
        column = []
        for x in range(len(map)):
            column.append(map[x][y])
        if "#" not in column:
            emptycols.append(y)
    #print("Empty columns:", emptycols)
    for y in range(len(map)):
        for x in emptycols:
            for r in range(extra):
                index = emptycols.index(x)
                map[y].insert(x+1+index*extra, "0")
                print(r, "Adding", str(index) + "/" + str(len(emptycols)), end="\r")

    return map

def ExpandMap(map):
    extra = 100
    print("Adding columns...")
    map = AddCols(map, extra)
    print("Done!")
    print("Adding rows...")
    map = AddRows(map, extra)
    print("Done!")
    
    return map
 
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
map = ExpandMap(rawmap)

print("Retrieving galaxies...")
galaxies = GetGalaxies(map)
print("Done!")

total = 0
while galaxies:
    g1 = galaxies[0]
    galaxies.pop(0)
    for g2 in galaxies:
        dist = FindDistance(g1, g2)
        total += dist

print(total)

          
