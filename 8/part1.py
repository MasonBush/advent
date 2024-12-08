from itertools import permutations

antennaMap: list[list[str]] = []
antenna: dict[str, list[tuple[int]]] = {}

def distance(object_x: tuple[int], object_y: tuple[int]):
	d_x = object_x[0] - object_y[0]
	d_y = object_x[1] - object_y[1]

	return (d_x, d_y)


with open("input.txt", "r") as f:
	for y, line in enumerate(f.readlines()):
		row = []
		line = line.rstrip()
		for x, char in enumerate(line):
			row.append(char)

			if char not in [".", "#"]:
				if char not in antenna:
					antenna[char] = [(x,y)]
				else:
					antenna[char].append((x,y))

		antennaMap.append(row)

mapSize = (len(antennaMap[0]) - 1, len(antennaMap) - 1)

# create antinode map
x, y = mapSize
antiNodeMap: list[list[str]] = []
for i in range(y+1):
	row = []
	for i in range(x+1):
		row.append(".")

	antiNodeMap.append(row)

for k, v in antenna.items():
	
	for combos in permutations(v, r=2):
		antenna_x, antenna_y = combos

		dist = distance(antenna_x, antenna_y)
		antinodePos = (antenna_y[0] - dist[0], antenna_y[1] - dist[1])
		
		x, y = antinodePos
		mapSize_x, mapSize_y = mapSize # # check if node is outside
		if (x < 0 or x > mapSize_x) or (y < 0 or y > mapSize_y):
			continue

		antiNodeMap[antinodePos[1]][antinodePos[0]] = "#"


antiNodeCount = 0
for row in antiNodeMap:
	for char in row:
		if char == "#":
			antiNodeCount += 1


print(antiNodeCount)