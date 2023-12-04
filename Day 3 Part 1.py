#Advent of Code Day 3 part 1
input = open(r"C:\Users\chimp\Desktop\Advent of Code\2023\Day 3\Day_3_Input.txt", "r")

inputlist = input.readlines()
max = len(inputlist) - 1
rowmax = len(inputlist) - 1
colmax = len(inputlist[0]) - 2
print(colmax, "x", rowmax, "matrix")


matrix = []

for i in inputlist:
    i = i.strip()
    row = []
    for x in i:
        row.append(x)
    matrix.append(row)
    if len(i) < (colmax + 2): row.append(".")

def CheckForSymbol(row, col):
    
    if (row > 0) and (col > 0) and (matrix[row-1][col-1] not in ".1234567890"):
        return True
    elif (row > 0) and (matrix[row-1][col] not in ".1234567890"):
        return True 
    elif (row > 0) and (col < colmax) and (matrix[row-1][col+1] not in ".1234567890"):
        return True
    elif (col > 0) and (matrix[row][col-1] not in ".1234567890"):
        return True
    elif (col < colmax) and (matrix[row][col+1] not in ".1234567890"):
        return True
    elif (row < rowmax) and (col > 0) and (matrix[row+1][col-1] not in ".1234567890"):
        return True
    elif (row < rowmax) and (matrix[row+1][col] not in ".1234567890"):
        return True
    elif (row < rowmax) and (col < colmax) and (matrix[row+1][col+1] not in ".1234567890"):
        return True
    else:
        return False
goodtotal = 0
total = 0
for x in matrix:
    validnumber = False
    value = ""
    for y in x:
        row = matrix.index(x)
        col = x.index(y)
        if y.isdigit():
            if CheckForSymbol(row, col) is True:
                validnumber = True
            value = value + y
            matrix[row][col] = "."
        elif y != "0123456789" and value != "":
            if validnumber:
                total = total + int(value)
            validnumber = False
            value = "" 
print("Total is", total)

        