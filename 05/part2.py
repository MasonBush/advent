
rules: dict[int, list[int]] = {}

pages: list[list[int]] = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		if "|" in line:
			x, y = line.rstrip().split("|")

			x = int(x)
			y = int(y)

			if x not in rules:
				rules[x] = []

			rules[x].append(y)

			
		elif "\n" == line:
			continue
		else:
			line = line.rstrip().split(",")
			
			numbers = []
			for i in line:
				numbers.append(int(i))

			pages.append(numbers)


keys = list(rules.keys())
keys.sort()

rules = {i: rules[i] for i in keys}

# for k, v in rules.items():
# 	v.sort()
# 	print(f"{k}: {v}")


total = 0
for page in pages:
	fixedOrder = []

	pageRules = {}
	for i in page:
		pageRules[i] = rules[i]

	order = {}
	for k, v in pageRules.items():
		v.sort()
		print(f"{k}: {v}")
		for i in v:
			if i not in order:
				order[i] = 1
			else:
				order[i] += 1

	print()
	order = {k: v for k, v in sorted(order.items(), key=lambda item: item[1])}
	for k, v in order.items():
		if k in page:
			fixedOrder.append(k)

	for i in page:
		if i not in fixedOrder:
			fixedOrder.insert(0, i)

	print(page)
	print(fixedOrder)

	if page != fixedOrder:

		middle = int((len(fixedOrder) - 1) / 2)
		total += fixedOrder[middle]

	print("\n---------------------------------------------\n")

print(total)