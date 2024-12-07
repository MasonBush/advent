
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


def decToTernary(n, zfill):
    if n == 0:
        return list('0'.zfill(zfill))
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return list(''.join(reversed(nums)).zfill(zfill))


total = 0
for correctValue, equation in equations.items():

	variations = []
	for i in range(3**(len(equation) - 1)):
		variations.append(equation[0])


	for i in range(len(variations)):
		operations = decToTernary(i, len(equation) - 1)
		
		for index in range(len(equation) - 1):
			nextNumber = equation[index + 1]

			operation = int(operations[index])
			
			if operation == 0:
				variations[i] = variations[i] + nextNumber
			elif operation == 1:
				variations[i] = variations[i] * nextNumber
			elif operation == 2:
				variations[i] = int(f"{variations[i]}{nextNumber}")

		if correctValue == variations[i]:
			total += correctValue
			break



print(total)