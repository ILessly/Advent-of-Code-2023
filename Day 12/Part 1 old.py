#Advent of Code Day 12 Part 1

input = open(r"Day 12\example.txt", "r")
inputlist = input.readlines()

def GetSprings(row):
    print("Getting springs in row", row)
    springs = row[0]
    sizes = []
    temp_springs = ""
    for i in row[1].split(","):
        sizes.append(int(i))
    length_needed = sum(sizes) + len(sizes)-1
    
    
    def GetVariations(spring):
        variations = 2**(spring.count("?"))
        #print("Getting variations for", spring)
        
        return variations
    
    if len(springs) == length_needed:
        print("For", springs, "Number of variations:", 1)
        return 1 #If the length is what is required there can be only 1 variation
    
    
    spring_size = 0
    spring_count = 0
    spring = ""
    spring_size_list = []
    for c in springs:
        if c in "?#":
            spring_size += 1
            spring += c
            #print("Spring found", spring_size)
        
        elif c == "." and spring_size != 0:
            #print("End of spring found. Final size", spring_size)
            variations = GetVariations(spring)
            #print("Variations:", variations)
            spring_size_list.append(spring_size)
            spring_size = 0
            spring_count += 1
        
    spring_count = 1 if spring_count == 0 else spring_count
    if spring_size != 0: 
        print("End of spring found. Final size", spring_size)
        spring_size_list.append(spring_size)
        variations = GetVariations(spring)    
    print("Found", len(spring_size_list), "springs of sizes", spring_size_list)    
    
    
    
    
    
    
    return variations
    
    
    
    # print("Needs", length_needed, "spaces of", len(springs))
    # if len(springs) == length_needed:
    #     print("For", springs, "Number of variations:", 1)
    # else:
    #     print("For", springs, "Number of variations:", variations)
    
    #print(springs)            
            
    
    
            
    



total = 0

for line in inputlist:
    row = line.strip().split(" ")
    variations = GetSprings(row)
    #print("For spring", line, "variations:", variations)

print("Done! Total is:", total)