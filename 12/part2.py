
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


def getSize(plots):
	smallest = (float('inf'), float('inf'))
	largest = (float('-inf'), float('-inf'))
	for x, y in plots:
		s_x, s_y = smallest
		l_x, l_y = largest

		if x < s_x:
			s_x = x
		if y < s_y:
			s_y = y


		if x > l_x:
			l_x = x
		if y > l_y:
			l_y = y
		
		smallest = (s_x, s_y)
		largest = (l_x, l_y)

	return smallest, largest
			

def test(plots):
	if len(plots) == 1:
		return 4


	smallest, largest = getSize(plots)

	x, y = largest
	testMap = []
	for i in range(y + 1):
		testMap.append([0] * (x + 1))


	plotter = {}
	for key in plots:
		plotter[key] = 1


	for start_x, start_y in plots:
		testMap[start_y][start_x] = 1

	
	for i in range(len(testMap)):
		testMap[i].insert(0, 0)
		testMap[i].insert(len(testMap[i]), 0)

	testMap.insert(0, [0] * len(testMap[0]))
	testMap.insert(len(testMap), [0] * len(testMap[0]))

	cornors = 0
	for y in range(len(testMap) - 1):
		for x in range(len(testMap[y]) - 1):

			square = [
				testMap[y][x],
				testMap[y][x+1],
				testMap[y+1][x],
				testMap[y+1][x+1]
			]

			count = sum(square)

			if count == 1 or count == 3:
				cornors += 1

	# for i in testMap:
	# 	print(i)

	return cornors
				
				
garden = readMap("test3.txt")

totalPrice = 0
alreadyChecked = []
for y, row in enumerate(garden):
	for x, char, in enumerate(row):
		if (x, y) not in alreadyChecked:
			result, borderValue = recursiveFind((x, y), garden, char, [], 0)

			print(char, test(result))
			totalPrice += len(result) * test(result)
			alreadyChecked = alreadyChecked + result


print(totalPrice)