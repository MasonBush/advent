trailMap: list[int, list[int]] = []
startPoints: list[tuple[int]] = []
mapSize: tuple[int] = ()

with open("input.txt", "r") as f:
	for y, line in enumerate(f.readlines()):
		row = []
		for x, i in enumerate(line.rstrip()):
			if i == ".":
				i = -1

			point = int(i)

			row.append(point)

			if point == 0:
				startPoints.append((x, y))
		
		trailMap.append(row)

	mapSize = (len(trailMap[0]), len(trailMap))


def isVaildOffset(offset):
	global mapSize

	x, y = offset
	mapX, mapY = mapSize

	if x >= 0 and y >= 0:
		if x < mapX and y < mapY:
			return True

	return False

def checkTrail(currentPos: tuple[int], trailHeads: list):

	offsets = [
		(0, 1),
		(1, 0),
		(0, -1),
		(-1, 0)
	]

	x, y = currentPos
	currentHight = trailMap[y][x]
	for offset in offsets:
		offset = (currentPos[0] + offset[0], currentPos[1] + offset[1])

		if isVaildOffset(offset):
			x, y = offset
			option = trailMap[y][x]

			if option == currentHight + 1:

				if option == 9:
					if offset not in trailHeads:
						trailHeads.append(offset)
				else:
					trailHeads = checkTrail(offset, trailHeads)

	return trailHeads


# for i in trailMap:
# 	print(i)

total = 0
for startPoint in startPoints:
	trailHeads = checkTrail(startPoint, [])
	total += len(trailHeads)


print(total)