#Advent of Code Day 4 Part 1

input = open(r"filepath", "r")
inputlist = input.readlines()

def CheckForWinner(w, g):
    points = 0
    numwins = 0
    for x in g:
        if x in w:

            numwins += 1
    if numwins !=0: points = pow(2, numwins-1)
    return points

total = 0

for card in inputlist:
    card = card.strip()
    card = card.split("|")
    winningnums = card[0].split(":")[1].strip().split()
    givennums = card[1].strip().split()
    total = total + CheckForWinner(winningnums, givennums)
print(total)

    



