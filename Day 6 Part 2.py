#Advent of Code Day 6 Part 2

input = open(r"Day 6/input.txt", "r")
inputlist = input.readlines()

time = int(inputlist[0].strip()[5:].replace(" ",""))
distance = int(inputlist[1].strip()[9:].replace(" ",""))
hold = 0
run = 0
total = 1
wins = 0
run = time
for hold in range(time):
  result = hold * run
  run += -1
  #print("Hold for", hold, "runs for", run, "travels", result)
  if result > distance:
    wins +=1
print("Can win:", wins, "times")
