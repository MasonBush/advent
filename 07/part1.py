
equations: dict[int, list[int]] = {}
with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.rstrip()

		numbers = []
		answer, rawNumbers = line.split(":")
		for i in rawNumbers.split(" "):
			if i.isdigit():
				numbers.append(int(i))

		equations[int(answer)] = numbers


def decToBin(x, zfill):
	return list(str(bin(x)[2:]).zfill(zfill))


total = 0
for correctValue, equation in equations.items():

	variations = []
	for i in range(2**(len(equation) - 1)):
		variations.append(equation[0])



	for i in range(len(variations)):
		operations = decToBin(i, len(equation) - 1)
		
		for index in range(len(equation) - 1):
			nextNumber = equation[index + 1]
			
			if int(operations[index]):
				variations[i] = variations[i] + nextNumber
			else:
				variations[i] = variations[i] * nextNumber


	
	if correctValue in variations:
		total += correctValue


print(total)