
def readMap(input:str) -> list[list[str]]:
	map = []
	with open(input, "r") as f:
		for line in f.readlines():

			row = []
			for char in line.rstrip():
				row.append(char)

			map.append(row)

	return map


def isValidIndex(point: tuple[int], map: list[list[str]]):
	x, y = point
	if x < 0 or y < 0: return False

	try:
		char = map[y][x]
		return True
	except IndexError:
		return False


def recursiveFind(startingPoint: tuple[int], map: list[list[str]], onlyFind: str, found: list[tuple[int]], borderValue):
	start_x, start_y = startingPoint
	found.append((start_x, start_y))
	# print(startingPoint, found)

	offsets = [
		(1, 0),
		(0, 1),
		(-1, 0),
		(0, -1)
	]

	for i in offsets:
		off_x, off_y = i

		x, y = (start_x + off_x, start_y + off_y)
		if isValidIndex((x, y), map):
			char = map[y][x]
			if char == onlyFind:
				if (x, y) not in found:
					found, borderValue = recursiveFind((x, y), map, onlyFind, found, borderValue)
			else:
				borderValue += 1
		else:
			borderValue += 1

	
	return found, borderValue
			



garden = readMap("test2.txt")

totalPrice = 0
alreadyChecked = []
for y, row in enumerate(garden):
	for x, char, in enumerate(row):
		if (x, y) not in alreadyChecked:
			result, borderValue = recursiveFind((x, y), garden, char, [], 0)

			totalPrice += len(result) * borderValue
			alreadyChecked = alreadyChecked + result
			print(char, borderValue, result)
		break
	break

print(totalPrice)