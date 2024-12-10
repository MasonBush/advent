import re

with open("input.txt", "r") as f:
	data = f.read()


found = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", data)


numbers = []
multiply = True
for i in found:
	if i == "do()":
		multiply = True
	elif i == "don't()":
		multiply = False
	else:
		if multiply:
			x, y = i[4:-1].split(",")
			numbers.append(int(x) * int(y))


print(sum(numbers))