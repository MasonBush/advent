stones = []
with open("input.txt", "r") as f:
	line = f.read().rstrip()
	for stone in line.split():
		stones.append(int(stone))


blinks = 25
for i in range(blinks):
	nextStones = []

	for stone in stones:
		strStone = str(stone)
		if stone == 0:
			nextStones.append(1)

		elif len(strStone) % 2 == 0:
			middle = int(len(strStone)/2)

			left = int(strStone[0:middle])
			right = int(strStone[middle:])

			nextStones.append(int(left))
			nextStones.append(int(right))

		else:
			nextStones.append(stone * 2024)

	stones = nextStones

print(len(stones))