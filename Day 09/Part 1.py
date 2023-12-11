#Advent of Code Day 9 Part 1

input = open(r"Day 9\input.txt", "r")
inputlist = input.readlines()

sequence = []
for x in inputlist:
    sequence.append(x.strip().split())

def FindDifferences(nums, finalnums):
    #print("Recieved", nums)
    difflist = []
    for y in range(len(nums)-1):
        #print("First number:", nums[y])
        #print("Second number:", nums[y+1])
        diff = int(nums[y+1]) - int(nums[y])
        #print("Difference:", diff)
        difflist.append(diff)
    #print("Differences:", difflist)
    #print("Final diff in list:", difflist[-1])
    finalnums.append(difflist[-1])

    return difflist, finalnums
    

total = 0
for x in sequence:
    nonzero = True
    #print("Starting sequence:", x)
    finalnums = [int(x[-1])]
    diffs, finalnums = FindDifferences(x, finalnums)
    #print(diffs)
    while nonzero:
        #print("Non zero diffs! Finding next tier.")
        diffs, finalnums = FindDifferences(diffs, finalnums)
        #print(diffs, finalnums)
        zeros = diffs.count(0)
        if zeros == len(diffs):
            nonzero = False
            
    #print("Done!", diffs)
    #print("Final of each seq:", finalnums)
    next = sum(finalnums)
    #print("Next num is", next)
    total += next
    #print("Running total is:", total)
print("Final total is:", total)
        