
leftList = []
rightList = []



with open("data.txt", "r") as f:

	for line in f.readlines():
		left, right = line.rstrip().split("   ")
		leftList.append(int(left))
		rightList.append(int(right))

leftList.sort()
rightList.sort()

data = {}
for i in leftList:
	data[i] = 0

	for x in rightList:
		if i == x:
			data[i] += 1



total = 0
for k, v in data.items():
	total += k*v


print(total)