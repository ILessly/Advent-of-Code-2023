#Advent of Code Day 8 Part 2
import math

input = open(r"Day 8/input.txt", "r")
inputlist = input.readlines()

steps = inputlist.pop(0).strip()
inputlist.pop(0)
map = {}

for line in inputlist:
    line = line.strip().split("=")
    map[line[0].strip()] = line[1].strip()[1:9].split(", ")

loc = []
for key in list(map.keys()):
  if key[2:3]=="A":
    loc.append(key)

endcount = []
total = 1
for step in loc:
  print("Doing", step, ":")
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
          if step[2:3] == "Z":
              finish = True
              break
  print("Done!", count)
  endcount.append(count)
print(endcount)

for i in range(len(endcount)-1):
  x1 = endcount[0]
  x2 = endcount[1]
  gcd = int(math.gcd(x1, x2))
  lcm = int((x1 * x2)/gcd)
  endcount.pop(0)
  endcount[0] = lcm

print("Total:", endcount)
