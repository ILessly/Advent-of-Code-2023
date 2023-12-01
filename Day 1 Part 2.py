#Advent of Code Day 1 part 2

file = open(r"filepathonmyhomecomputerlol", "r")
inputlist = file.readlines()
i=0
t=0
total=0

digitltrs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digitnums = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']

for i in inputlist:
  i=i.strip()
  for t in digitltrs:
    if t in i:
      i = i.replace(t, digitnums[digitltrs.index(t)])
      
  number = i.translate({ord(a): None for a in 'abcdefghijklmnopqrstuvwxyz'})
  x1 = number[0:1]
  x2 = number[-1:]
  value = int(x1 +x2)
  total = total + value
  
print(total)
