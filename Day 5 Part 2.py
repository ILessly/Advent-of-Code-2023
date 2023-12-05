#Advent of Code Day 5 Part 2

input = open(r"Example.txt", "r")
inputlist = input.readlines()

def GetSeeds():
  print("Getting seeds")
  rawseeds = inputlist[0].split()[1:]
  seeds = []
  seedrange = []
  inputlist.pop(0)
  print("Seed list:", rawseeds)
  for seed in rawseeds:
    if rawseeds.index(seed) % 2 == 0:
      seeds.append(seed)
    else:
      seedrange.append(seed)
  print("New list:", seeds)
  print("With ranges:", seedrange)
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
  return maps


def GetRange(map):
  splitmap = map.split()
  maprange = [int(splitmap[1]), int(splitmap[1]) + int(splitmap[2])]

  return maprange


def ConvertNum(num, map, sourcerange):
  num = num
  splitmap = map.split()
  num = int(splitmap[0]) + (num - int(splitmap[1]))
  return num


numtype = ["Seed", "Soil", "Fertilizer", "Water", "Light", "Temp", "Humidity"]
seeds, seedrange = GetSeeds()
maps = GetMaps()
least = 0
leastseed = 0
for seed in seeds:
  num = seed
  for x in maps:
    for y in x:
      sourcerange = GetRange(y)
      if int(num) >= sourcerange[0] and int(num) <= sourcerange[
          len(sourcerange) - 1]:
        num = ConvertNum(int(num), y, sourcerange)
        break
  print("Seed", seeds.index(seed), ":", seed, "is", num)
  if least == 0:
    least = num
    leastseed = seed
  elif num < least:
    least = num
    leastseed = seed
print("Least is:", least, "for seed", seeds.index(leastseed), "value of",
      leastseed)
