#Advent of Code Day 4 Part 2

input = open(r"filepath", "r")
inputlist = input.readlines()

def CheckForWinner(w, g):
    numwins = 0
    for x in g:
        if x in w:
            numwins += 1   
    return numwins

total = 0
nummatches = []

for card in inputlist:
    card = card.strip()
    card = card.split("|")
    winningnums = card[0].split(":")[1].strip().split()
    givennums = card[1].strip().split()
    nummatches.append(CheckForWinner(winningnums, givennums))

totalcards = 0
uncheckedcards = []
for i in range(len(inputlist)):
    uncheckedcards.append((i, nummatches[i]))    

while len(uncheckedcards) >= 0:
    #print(uncheckedcards)
    (index, wins) = uncheckedcards.pop(0)
    for i in range(index+1, index+wins+1):
        if i >= len(nummatches):
            continue
        uncheckedcards.append((i, nummatches[i]))
    totalcards += 1
    if len(uncheckedcards) == 0: break

print(totalcards)
    



