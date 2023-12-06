#Advent of Code Day 5 Part 2

input = open(r"2023\Day 5\Day 5 Input.txt", "r")
inputlist = input.readlines()

def GetSeeds():
  #print("Getting seeds")
  rawseeds = inputlist[0].split()[1:]
  seeds = []
  seedrange = []
  inputlist.pop(0)
  #print("Seed list:", rawseeds)
  for seed in rawseeds:
    if rawseeds.index(seed) % 2 == 0:
      seeds.append(seed)
    else:
      seedrange.append(seed)
  #print("New list:", seeds)
  #print("With ranges:", seedrange)
  return seeds, seedrange


def GetMaps():
  currentmap = []
  x = -1
  maps = [[], [], [], [], [], [], []]
  for i in inputlist:
    if "to" in i:
      x += 1
      currentmap = maps[x]
    elif i == "\n":
      pass
    else:
      currentmap.append(i.strip())
  #print (maps)
  return maps


def GetRange(map):
  splitmap = map.split()
  maprange = [int(splitmap[0]), int(splitmap[0]) + int(splitmap[2])]

  return maprange


def ConvertNum(num, map):
  num = num
  splitmap = map.split()
  num = int(splitmap[1]) + (num - int(splitmap[0]))
  return num


def CheckSeedRange(num, seeds, seedrange):
    x = 0
    for x in range(len(seeds)):
        if num >= int(seeds[x]) and num <= (int(seeds[x]) + int(seedrange[x])):
            return True
    return False 


numtype = ["Seed", "Soil", "Fertilizer", "Water", "Light", "Temp", "Humidity"]
seeds, seedrange = GetSeeds()
maps = GetMaps()[::-1]
max = 265018614
valid = False
partcomp = 0

while valid is False:
    for loc in range(max):
        num = loc
        for map in maps:
            for row in map:
                sourcerange = GetRange(row)
                if num >= sourcerange[0] and num <= sourcerange[len(sourcerange) - 1]:
                    num = ConvertNum(num, row)
                    break
        if CheckSeedRange(num, seeds, seedrange):
            valid = True
            break
        #print("Loc", loc, "becomes", num)
        if loc % 100000 == 0 and loc != 0:
            partcomp += 1
            print("Completed part", partcomp, "of 2650")
print("Valid location of:", loc)    
