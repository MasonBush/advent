import re

with open("input.txt", "r") as f:
	data = f.read()


found = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)


numbers = []
for i in found:
	x, y = i[4:-1].split(",")
	numbers.append(int(x) * int(y))


print(sum(numbers))