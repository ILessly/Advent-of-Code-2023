#Advent of Code Day 6 Part 1

input = open(r"Day 6/input.txt", "r")
inputlist = input.readlines()

times = inputlist[0].strip().split()[1:]
distances = inputlist[1].strip().split()[1:]
hold = 0
run = 0
total = 1
for time in times:
  wins = 0
  run = int(time)
  for hold in range(int(time)):
    result = hold * run
    run += -1
    #print("Hold for", hold, "runs for", run, "travels", result)
    if result > int(distances[times.index(time)]):
      wins +=1
  print("Can win:", wins, "times")
  total = total * wins

print("total", total)
