
levels = []

with open("data.txt", "r") as f:
	for line in f.readlines():
		numbers = []

		for i in line.split(" "):
			numbers.append(int(i))

		levels.append(numbers)


safeLevels = 0
for level in levels:

	maxDiff = 3
	positves = 0
	negatives = 0
	unsafeJumps = 0
	nochanges = 0

	temp = []
	for i in range(1, len(level)):
		diff = level[i] - level[i-1]
		# print(diff)
		temp.append(diff)

		if abs(diff) > maxDiff:
			unsafeJumps += 1
		
		if diff > 0:
			positves += 1
		elif diff < 0:
			negatives += 1
		else:
			nochanges += 1

	print(temp)
	if positves != 0 and negatives == 0 and unsafeJumps == 0 and nochanges == 0:
		print(f"{positves = }, {negatives = }, {unsafeJumps = }, {nochanges = } | Safe\n")
		safeLevels += 1
		continue
	elif positves == 0 and negatives != 0 and unsafeJumps == 0 and nochanges == 0:
		print(f"{positves = }, {negatives = }, {unsafeJumps = }, {nochanges = } | Safe\n")
		safeLevels += 1
		continue
	else:
		print(f"{positves = }, {negatives = }, {unsafeJumps = }, {nochanges = } | unsafe\n")

print(safeLevels)