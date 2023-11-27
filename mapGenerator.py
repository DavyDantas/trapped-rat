map = open("MAP.txt", "r")

size = map.readline().split()
rows = int(size[0]) + 2
coluns = int(size[1]) + 2

linesMap = map.readlines()
mapCells = []
firstEndLines = [] 

mapCells.append(["1"] * coluns)

for line in range(1, rows-1):

    mapCells.append(list(linesMap[line-1].strip()))
    mapCells[-1].insert(0,"1")
    mapCells[-1].append("1")

mapCells.append(["1"] * coluns)

# for map in mapCells:
#     print(map)


# [print(mapCells[row][col]) for row in range(rows) for col in range(coluns)]

