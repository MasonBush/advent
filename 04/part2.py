
data = []
with open("input.txt", "r") as f:

	for line in f.readlines():
		splitLine = []
		for char in line.rstrip():
			splitLine.append(char)

		data.append(splitLine)



variants = [
	[
		["M", None, "S"],
		[None, "A", None],
		["M", None, "S"],
	],
	[
		["S", None, "M"],
		[None, "A", None],
		["S", None, "M"],
	],
	[
		["S", None, "S"],
		[None, "A", None],
		["M", None, "M"],
	],
	[
		["S", None, "M"],
		[None, "A", None],
		["S", None, "M"],
	],
	[
		["M", None, "M"],
		[None, "A", None],
		["S", None, "S"],
	]
]



count = 0
for origin_y in range(len(data)):
	for origin_x in range(len(data[origin_y])):


		if origin_x <= 0 or origin_y <= 0:
			continue

		if data[origin_y][origin_x] != "A":
			continue

		try:
			arr = [
				[data[origin_y - 1][origin_x - 1], None, data[origin_y - 1][origin_x + 1]],
				[None, data[origin_y][origin_x], None],
				[data[origin_y + 1][origin_x - 1], None, data[origin_y + 1][origin_x + 1]],
			]

			if arr in variants:
				count += 1

		except IndexError:
			pass


print(count)