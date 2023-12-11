#Advent of Code Day 1 part 1

file = open(r"filepathonmyhomecomputerlol", "r")
inputlist = file.readlines()
i=0
total=0

for i in inputlist:
  i=i.strip()
  number = i.translate({ord(a): None for a in 'abcdefghijklmnopqrstuvwxyz'})
  x1 = number[0:1]
  x2 = number[-1:]
  value = int(x1 +x2)
  total = total + value
  
print(total)
