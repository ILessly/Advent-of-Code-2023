#Advent of Code Day 12 Part 1

input = open(r"Day 13/example.txt", "r")
inputlist = input.readlines()

inputblocks = []
blocks = {}
block = []

b = 1
for line in inputlist:
  block.append(line.strip()) if line.strip() != "" else None
  if line.strip() == "" or line == inputlist[-1]:
    inputblocks.append(block)
    block = []

for block in inputblocks:
  rows = []
  cols = []
  
  for row in block:
    rows.append(row)
    for x in range(len(row)):
      if len(cols) == len(row):
       cols[x] += str(row[x])
      else:
        cols.append(row[x])
  blocks.update({"Block"+ str(b) : [rows, cols]}) #Dict of all blocks. Block'X' has [rows][columns].
  b += 1

def PrintBlock(block):
  if block not in blocks.keys():
    print("Block", block, "does not exist.")
    return None
  for x in range(2):
    for i in blocks.get(block)[x]:
      print(i)
    print("\n")

def CheckRows(rows):
  print("Checking rows...")
  for row in range(len(rows)-1):
    x1 = rows[row]
    x2 = rows[row+1]
    while x1 == x2:
      print("Match found! Row:", row, "and", row+1)
      try:
        x1 = rows[rows.index(x1)-1]
        x2 = rows[rows.index(x2)+1]
        print("Checking row", rows.index(x1)-1, "and", rows.index(x2)+1, "...")

      except:
        print("Edge reached.")
        break

        
  

def CheckCols(cols):
  print("Checking columns...")

for block in blocks.keys():
  print(block)
  CheckRows(blocks.get(block)[0])
  CheckCols(blocks.get(block)[1])
  print("Done!")






    
