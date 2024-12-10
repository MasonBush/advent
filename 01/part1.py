
leftList = []
rightList = []

with open("data.txt", "r") as f:

	for line in f.readlines():
		left, right = line.rstrip().split("   ")
		leftList.append(int(left))
		rightList.append(int(right))

leftList.sort()
rightList.sort()

totalDistance = 0
for i in range(len(leftList)):
	totalDistance += abs(leftList[i] - rightList[i])


print(totalDistance)