
diskMap = []
with open("input.txt", "r") as f:
	line = list(f.read().rstrip())

	lineSize = int((len(line) + 1) / 2)
	for i in range(lineSize):
		index = i * 2
		files = int(line[index])


		if i == lineSize - 1:
			freeSpace = 0
		else:
			freeSpace = int(line[index + 1])

		diskMap.append((files, freeSpace))


blockedMap = []
for id, i in enumerate(diskMap):
	files, freeSpace = i

	for i in range(files):
		blockedMap.append(id)

	for i in range(freeSpace):
		blockedMap.append(None)


def getFreeSpaces(blockedMap):
	#dict[freespace size, starting index]
	freeSpaces: dict[int, list[int]] = {}
	index = 0
	while True:
		if index == len(blockedMap): break

		if blockedMap[index] == None:
			for i in range(index, len(blockedMap)):
				if blockedMap[i] != None:
					size = i - index
					if size not in freeSpaces:
						freeSpaces[size] = [index]
					else:
						freeSpaces[size].append(index)

					index = i
					break

		index += 1

	return freeSpaces


def getAvaliableSpace(requiredSize, freeSpaces: dict[int, list[int]]):

	sortedSpaces = {}
	for size, spaces in freeSpaces.items():
		if size < requiredSize:
			continue

		spaces.sort()

		for i in spaces:
			sortedSpaces[i] = size

	keys = list(sortedSpaces.keys())
	keys.sort()

	sortedSpaces = {i: sortedSpaces[i] for i in keys}

	if not sortedSpaces:
		return


	index = list(sortedSpaces.keys())[0]

	size = sortedSpaces[index]
	return size, index


#print(blockedMap)
freeSpaces = getFreeSpaces(blockedMap)
index = len(blockedMap) - 1
while True:
	if index == 0: break
	
	if blockedMap[index] != None:
		blockID = blockedMap[index]
		block = [blockID]
		for i in range(index - 1, 0, -1):
			if blockID == blockedMap[i]:
				block.append(blockID)
			else:
				break

		
		result = getAvaliableSpace(len(block), freeSpaces)

		# print(blockedMap, block, result)
		if result:
			size, posIndex = result

			if posIndex > index:
				index -= len(block)
				continue

			for i in range(len(block)):
				blockedMap[posIndex + i] = blockedMap[index - i]
				blockedMap[index - i] = None

			freeSpaces[size].pop(0)

			
			remainingSpace = size - len(block)
			if remainingSpace > 0:
				if remainingSpace not in freeSpaces:
					freeSpaces[remainingSpace] = [posIndex + len(block)]
				else:
					freeSpaces[remainingSpace].append(posIndex + len(block))

			# print(blockedMap, block)

		else:
			index -= len(block)
			continue


	index -= 1

#print()
# print(blockedMap)

total = 0
for i, id in enumerate(blockedMap):
	if id:
		total += i * id

print(total)