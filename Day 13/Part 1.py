#Advent of Code Day 13 Part 1

input = open(r"Day 13/input.txt", "r")
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
  print("Checking rows...") if printrows == True else None
  for row in range(len(rows)-1):
    row1 = row
    row2 = row+1
    x1 = rows[row1]
    x2 = rows[row2]
    while x1 == x2:
      print("Match found! Row:", row1, "and", row2) if printrows == True else None
      row1 += -1 if row1 > 0 else row2 + 1000
      row2 += 1
      try:
        x1 = rows[row1]
        x2 = rows[row2]
        print("Checking row", row1, "and", row2, "...") if printrows == True else None
        
        
      except:
        print("Edge found. Mirror confirmed! Between", row, "and", row+1) if printrows == True else None
        return row+1

  print("No row mirror found.") if printrows == True else None
  return 0


def CheckCols(cols):
  print("Checking columns...") if printcols == True else None
  for col in range(len(cols)-1):
    col1 = col
    col2 = col+1
    x1 = cols[col1]
    x2 = cols[col2]
    while x1 == x2:
      print("Match found! Column:", col1, "and", col2) if printcols == True else None
      col1 += -1 if col1 > 0 else col2 + 1000
      col2 += 1
      try:
        x1 = cols[col1]
        x2 = cols[col2]
        print("Checking column", col1, "and", col2, "...") if printcols == True else None
        
      except:
        print("Edge found. Mirror confirmed! Between", col, "and", col+1) if printcols == True else None
        return col+1

  print("No column mirror found.") if printcols == True else None
  return 0
  
  
printrows = False
printcols = False
total = 0
for block in blocks.keys():
  print("=================", block, "================================")
  colvalue = CheckCols(blocks.get(block)[1]) 
  rowvalue = CheckRows(blocks.get(block)[0])
  if colvalue == 0 and rowvalue == 0:
    print("Anomaly found, no mirror:", block)
  if colvalue != 0 and rowvalue != 0:
    print("Anomaly fouund, two mirrors:", block)
  total += (100*rowvalue) + colvalue
  print("Done!")
  
print("All done! Total:", total)






    
