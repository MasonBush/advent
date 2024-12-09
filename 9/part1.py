
diskMap = []
with open("test3.txt", "r") as f:
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


defraged = []
for i in blockedMap:
	if i == None:
		lastIndex = None
		while True:
			lastIndex = blockedMap.pop(-1)

			if lastIndex != None:
				break

		
		defraged.append(lastIndex)
	else:
		defraged.append(i)

total = 0
for i, id in enumerate(defraged):
	total += i * id

print(total)