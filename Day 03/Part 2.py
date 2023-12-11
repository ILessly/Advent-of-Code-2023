#Advent of Code Day 3 part 2
input = open(r"filepathonmycomputer", "r")

inputlist = input.readlines()
max = len(inputlist) - 1
rowmax = len(inputlist) - 1
colmax = len(inputlist[0]) - 2
print(colmax, "x", rowmax, "matrix")


matrix = []
goodnumbers = []
badnumbers = []

for i in inputlist:
    i = i.strip()
    row = []
    for x in i:
        row.append(x)
    matrix.append(row)
    if len(i) < (colmax + 2): row.append(".")

def CheckIsGear(row, col):
    ratio = 0
    adjacentnums = []
    if CheckDigit(row-1, col-1) or CheckDigit(row-1, col+1) or CheckDigit(row-1, col):        #Check the above row
        if CheckDigit(row-1, col):                                #Only one number above in this case
            adjacentnums.append(GetNumber(row-1, col))
        else:
            if CheckDigit(row-1, col-1): 
                adjacentnums.append(GetNumber(row-1, col-1))
            if CheckDigit(row-1, col+1):
                adjacentnums.append(GetNumber(row-1, col+1))
    if CheckDigit(row+1, col-1) or CheckDigit(row+1, col+1) or CheckDigit(row+1, col):        #Check the below row
        if CheckDigit(row+1, col):                                #Only one number below in this case
            adjacentnums.append(GetNumber(row+1, col))
        else:
            if CheckDigit(row+1, col-1): 
                adjacentnums.append(GetNumber(row+1, col-1))
            if CheckDigit(row+1, col+1):
                adjacentnums.append(GetNumber(row+1, col+1))
    if CheckDigit(row, col-1):
        adjacentnums.append(GetNumber(row, col-1))
    if CheckDigit(row, col+1):   
        adjacentnums.append(GetNumber(row, col+1))
    print("No other digits")
    if len(adjacentnums) == 2:
        print("Gear found! at", row, col)
        print("Adjacent numbers:", adjacentnums)
        ratio = int(adjacentnums[0]) * int(adjacentnums[1])
        print("Ratio is", ratio)
        return ratio
    else:
        print("Not a gear!")
        return 0
    
def CheckDigit(row, col):
    if row == -1 or row > rowmax or col == -1 or col > colmax:
        return False
    else:
        return matrix[row][col].isdigit()

def GetNumber(row, col):
    number = matrix[row][col]
    print("Starting with digit", matrix[row][col])
    leftbound = col-1
    rightbound = col+1
    while InBounds(row, leftbound) and matrix[row][leftbound].isdigit():
       number = matrix[row][leftbound] + number
       print("Digit", matrix[row][leftbound], "found")
       leftbound += -1
    while InBounds(row, rightbound) and matrix[row][rightbound].isdigit():
       number = number + matrix[row][rightbound]
       print("Digit", matrix[row][rightbound], "found")
       rightbound += 1
    number = int(number)
    return number
    
def InBounds(row, col):
    if row in range(rowmax+1) and col in range(colmax+1):
        return True
    else:
        return False  

total = 0
for x in matrix:
    value = ""
    for y in x:
        row = matrix.index(x)
        col = x.index(y)
        if y == "*":
            print("Possible gear at", row, col)
            total = total + CheckIsGear(row, col)
            matrix[row][col] = "."

print("Total is", total)

        
