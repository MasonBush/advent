
stones = []
with open("input.txt", "r") as f:
	line = f.read().rstrip()
	for stone in line.split():
		stones.append(int(stone))


def recursion(layer, stone: int):
	global alreadyComputed


	if layer == 0:
		return 1
	
	if (layer, stone) in alreadyComputed:
		return alreadyComputed[(layer, stone)]


	strStone = str(stone)
	if stone == 0:
		result = recursion(layer -1, 1)

	elif len(strStone) % 2 == 0:
		middle = int(len(strStone)/2)
		left = int(strStone[0:middle])
		right = int(strStone[middle:])
		result = recursion(layer -1, left) + recursion(layer -1, right)

	else:
		result =  recursion(layer -1, stone * 2024)

	alreadyComputed[(layer, stone)] = result
	return result



alreadyComputed = {}
size = 0
for stone in stones:
	size += recursion(75, stone)

print(size)