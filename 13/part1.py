import re
import itertools

def readInput(input:str) -> list[tuple[int]]:

	machines = []
	with open(input, "r") as f:
		while True:
			buttonA = f.readline()
			buttonB = f.readline()
			prize = f.readline()
			f.readline()

			if not buttonA:
				break
				
			machine = []
			for i in [buttonA, buttonB, prize]:
				results = re.search(r"X.(?P<xPos>\d+), ..(?P<yPos>\d+)", i)
				machine.append((int(results.group('xPos')), int(results.group('yPos'))))		
			machines.append(machine)

	return machines


combos = itertools.product(range(100), repeat=2)

machines = readInput("input.txt")
totalCost = 0
for machine in machines:
	a, b, prize = machine

	a_x, a_y = a
	b_x, b_y = b

	costs = []
	for i in itertools.product(range(100), repeat=2):
		m_x, m_y = i

		r_x = m_x * a_x + m_y * b_x
		r_y = m_x * a_y + m_y * b_y


		if (r_x, r_y) == prize:
			costs.append(m_x * 3 + m_y * 1)

	if costs:
		costs.sort()
		totalCost += costs[0]


print(totalCost)

