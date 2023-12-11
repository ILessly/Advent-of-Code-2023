#Advent of Code Day 5 Part 1

input = open(r"input.txt", "r")
inputlist = input.readlines()


def GetSeeds():
  seeds = inputlist[0].split()[1:]
  inputlist.pop(0)
  return seeds


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
seeds = GetSeeds()
maps = GetMaps()
least = 0

for seed in seeds:
  num = seed
  for x in maps:
    for y in x:
      sourcerange = GetRange(y)
      if int(num) >= sourcerange[0] and int(num) <= sourcerange[
          len(sourcerange) - 1]:
        num = ConvertNum(int(num), y, sourcerange)
        break
  if least == 0:
    least = num
  elif num < least:
    least = num
print("Least is:", least)
