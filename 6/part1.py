inputMap: list[list[str]] = []
guardPos: list[int] = []


guardDirIndex: int = 0
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
				guardPos = [i, len(inputMap)]

			chars.append(char)

		inputMap.append(chars)


while True:
	guard_x, guard_y = guardPos
	offset_x, offset_y = guardDirections[guardDirIndex]

	nextPos_x = guard_x + offset_x
	nextPos_y = guard_y + offset_y

	#check if next pos is outside of map
	if nextPos_x < 0 or nextPos_x > (len(inputMap[guard_y]) - 1):
		inputMap[guard_y][guard_x] = "X"
		break
	elif nextPos_y < 0 or nextPos_y > (len(inputMap) - 1):
		inputMap[guard_y][guard_x] = "X"
		break

	
	nextChar = inputMap[nextPos_y][nextPos_x]
	if nextChar == "#":
		if guardDirIndex == len(guardDirections) - 1:
			guardDirIndex = 0
		else:
			guardDirIndex += 1
	else:
		inputMap[guard_y][guard_x] = "X"
		guardPos = [nextPos_x, nextPos_y]
	


for i in inputMap:
	print(i)

count = 0
for line in inputMap:
	for char in line:
		if char == "X":
			count += 1

print(count)