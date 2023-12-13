#Advent of Code Day 12 Part 1

input = open(r"Day 12\input.txt", "r")
inputlist = input.readlines()

#Damaged spring = #
#Working spring = .
#Unknown spring = ?

def CheckSprings(prev, curr, group, springs, damaged):
    #print("Checking", curr, "in", springs)
    
    next = springs[0] if springs else None
    
    if not damaged and not springs:
        return 1
    
    if not damaged and springs:
        if "#" not in springs:
            return 1
        else:
            return 0
    
    if not prev and not curr and damaged:
        return 0
    
    if curr ==  "?":
        broken = CheckSprings(prev, "#", group, springs, damaged)
        working = CheckSprings(prev, ".", group, springs, damaged)
        return broken + working
    
    if curr != prev and group:
        if group != damaged[0]:
            return 0
        damaged = damaged[1:]
        group = 0
    
    if curr == "#":
        group += 1
        if group > damaged[0]:
            return 0

    
    return CheckSprings(curr, next, group, springs[1:], damaged)
    

total = 0

for line in inputlist:
    row = line.strip().split(" ")
    springs = row[0]
    damaged = [int(i) for i in row[1].split(",")]
    print("Checking row", row)
    variations = CheckSprings(None, springs[0], 0, springs[1:], damaged)
    print(row, "has", variations, "variations.")
    total += variations

print("Done! Total is:", total)