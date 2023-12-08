#Advent of Code Day 2 Part 1

input = open(r"filelocationonmycomputer", "r")
inputlist = input.readlines()
#print(inputlist)

total = 0

for i in inputlist:        #Isolate each game
    i = i.strip()
    i = i.split(":")
    ID = i[0]               #Split the game ID from results
    i = i[1]
    ID = int(ID[5:])
    gameset = i.split(";")
    for group in gameset:           #Isolate each grab
        group = group.split(",")
        for set in group:           #Isolate each color
            set = set.strip()
            set = set.split(" ")
            if (set[1] == "red" and int(set[0]) > 12) or (set[1] == "green" and int(set[0]) > 13) or (set[1] == "blue" and int(set[0]) > 14):
                ID = 0
    total = total + ID
    
print(total)     
            
