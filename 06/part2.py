inputMap: list[list[str]] = []
startingGuardPos: list[int] = []


guardDirections = [
	[0,-1], 	# up
	[1,0], 		# right
	[0, 1],		# down
	[-1, 0] 	# left
] # [x, y]


with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.rstrip()

		chars = []
		for i in range(len(line)):
			char = line[i]

			if char == "^":
				startingGuardPos = [i, len(inputMap)]

			chars.append(char)

		inputMap.append(chars)


def runMap(map: list[list[str]]):
	exitable = False
	guardPos = startingGuardPos
	guardDirIndex: int = 0


	maxLoops = 10000
	loops = 0
	while True:
		loops += 1

		if loops > maxLoops:
			break

		guard_x, guard_y = guardPos
		offset_x, offset_y = guardDirections[guardDirIndex]

		nextPos_x = guard_x + offset_x
		nextPos_y = guard_y + offset_y

		#check if next pos is outside of map
		if nextPos_x < 0 or nextPos_x > (len(map[guard_y]) - 1):
			map[guard_y][guard_x] = "X"
			exitable = True
			break
		elif nextPos_y < 0 or nextPos_y > (len(map) - 1):
			map[guard_y][guard_x] = "X"
			exitable = True
			break

		
		nextChar = map[nextPos_y][nextPos_x]
		if nextChar == "#":
			if guardDirIndex == len(guardDirections) - 1:
				guardDirIndex = 0
			else:
				guardDirIndex += 1
		else:
			map[guard_y][guard_x] = "X"
			guardPos = [nextPos_x, nextPos_y]

	return exitable, map


def copyMap(map: list[list[str]]):
	copiedMap: list[list[str]] = []

	for subList in map:
		copiedMap.append(subList.copy())

	return copiedMap



exitable, completedMap = runMap(copyMap(inputMap))

xPostions = []
for y in range(len(completedMap)):
	for x in range(len(completedMap[y])):
		char = completedMap[y][x]
		if char == "X":
			xPostions.append([x, y])


incompletable = 0
for i in xPostions:
	if i == startingGuardPos:
		continue

	x, y = i
	map = copyMap(inputMap)
	map[y][x] = "#"

	exitable, completedMap = runMap(map)

	if exitable == False:
		incompletable += 1

print(incompletable)