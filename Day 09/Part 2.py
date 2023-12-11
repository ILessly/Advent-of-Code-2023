#Advent of Code Day 9 Part 2

input = open(r"Day 9\input.txt", "r")
inputlist = input.readlines()

sequence = []
for x in inputlist:
    sequence.append(x.strip().split())

def FindDifferences(nums, firstnums):
    #print("Recieved", nums)
    difflist = []
    for y in range(len(nums)-1):
        #print("First number:", nums[y])
        #print("Second number:", nums[y+1])
        diff = int(nums[y+1]) - int(nums[y])
        #print("Difference:", diff)
        difflist.append(diff)
    print("Differences:", difflist)
    #print("Final diff in list:", difflist[-1])
    firstnums.insert(0, difflist[0])

    return difflist, firstnums
    

total = 0
for x in sequence:
    nonzero = True
    #print("Starting sequence:", x)
    firstnums = [int(x[0])]
    diffs, firstnums = FindDifferences(x, firstnums)
    #print(diffs)
    while nonzero:
        #print("Non zero diffs! Finding next tier.")
        diffs, firstnums = FindDifferences(diffs, firstnums)
        #print(diffs, finalnums)
        zeros = diffs.count(0)
        if zeros == len(diffs):
            nonzero = False
            
    print("Done!", diffs)
    print("First of each seq:", firstnums)
    next = 0
    for i in range(len(firstnums)):
        #print("Subtracting", next, "from", firstnums[i])
        next = firstnums[i] - next
        #print(next)
   
    print("Next num is", next)
    total += next
    #print("Running total is:", total)
print("Final total is:", total)
        