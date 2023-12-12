#Advent of Code Day 12 Part 1

input = open(r"Day 12\example2.txt", "r")
inputlist = input.readlines()

def GetSprings(row):
    print("Getting springs in row", row)
    springs = row[0]
    tempsprings = ""
    sizes = row[1].split(",")

    for x in sizes:
        print("Checking for spring of size", x + "...")
        score = 0
        for i in range(len(springs)):
            if springs[i] in "?#":
                score += 1
                print("Possible spring at", i, "? Score:", score)
            else:
                score = 0
            if score == int(x):
                print("Spring found of size:", score)
                springs = "#"*score + springs[score:]
                print("In progress spring:", springs)
                i += score
                score = 0
                break
    #print(springs)            
            
    
    
            
    



total = 0

for line in inputlist:
    row = line.strip().split(" ")
    GetSprings(row)
    

print("Done! Total is:", total)