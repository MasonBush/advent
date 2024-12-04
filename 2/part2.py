def checkUnsafe(level):
	maxDiff = 3
	unsafeJumps = 0
	nochanges = 0
	positves = 0
	negatives = 0


	temp = []
	jumpErrors = [False]
	for i in range(1, len(level)):
		diff = level[i] - level[i-1]
		temp.append(diff)

		if abs(diff) > maxDiff:
			unsafeJumps += 1
			jumpErrors.append(True)
		else:
			jumpErrors.append(False)

		if diff > 0:
			positves += 1
		elif diff < 0:
			negatives += 1
		else:
			nochanges += 1

		
	changes = 0
	if positves > negatives:
		changes = negatives
	elif positves < negatives:
		changes = positves
	elif positves == negatives:
		changes = negatives


	unsafeAmmount = unsafeJumps + nochanges + changes
	

	if unsafeJumps > 0:
		print(f"{positves = }, {negatives = }, {unsafeJumps = }, {nochanges = } | {unsafeAmmount = } | {unsafeAmmount <= 1} | {level}")

	return unsafeAmmount <= 1
	


levels = []
with open("test.txt", "r") as f:
	for line in f.readlines():
		numbers = []

		for i in line.split(" "):
			numbers.append(int(i))

		levels.append(numbers)


safeLevels = 0
for level in levels:
	if checkUnsafe(level):
		safeLevels += 1


print(safeLevels)