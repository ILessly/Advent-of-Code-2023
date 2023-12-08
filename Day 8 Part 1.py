#Advent of Code Day 8 Part 1

input = open(r"2023\Day 8\input.txt", "r")
inputlist = input.readlines()

steps = inputlist.pop(0).strip()
inputlist.pop(0)
map = {}

for line in inputlist:
    line = line.strip().split("=")
    map[line[0].strip()] = line[1].strip()[1:9].split(", ")

step = "AAA"
finish = False
count = 0

while not finish:
    for x in steps:
        #print(step)
        left_or_right = map[step]
        #print("Left or Right?", left_or_right)
        if x == "L":
            step = map[step][0]
            #print("Left:", step)
            count += 1
        elif x == "R":
            step = map[step][1]
            #print("Right:", step)
            count += 1
    if step == "ZZZ":
        finish = True  
print("Done!", count)


