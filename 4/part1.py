
data = []
with open("input.txt", "r") as f:

	for line in f.readlines():
		splitLine = []
		for char in line.rstrip():
			splitLine.append(char)

		data.append(splitLine)



variants = {
	"normal": 		[[0,0], [0, 1], 	[0, 2], 	[0, 3]],
	"backwards": 	[[0,0], [0,-1], 	[0,-2], 	[0,-3]],
	"upwards": 		[[0,0], [-1,0], 	[-2,0],		[-3,0]],
	"downwards": 	[[0,0], [1,0], 		[2,0], 		[3,0]],
	"upRight": 		[[0,0], [-1,1], 	[-2,2], 	[-3,3]],
	"upLeft": 		[[0,0], [-1,-1], 	[-2,-2], 	[-3,-3]],
	"downRight":	[[0,0], [1,1],		[2,2], 		[3,3]],
	"downLeft": 	[[0,0], [1,-1], 	[2,-2], 	[3,-3]]
}




count = 0
for origin_y in range(len(data)):
	for origin_x in range(len(data[origin_y])):
		
		for offsets in variants.values():
			word = []

			for offset in offsets:
				y, x = offset

				offset_x = origin_x + x
				offset_y = origin_y + y

				if offset_x < 0 or offset_y < 0:
					continue

				try:
					char = data[origin_y + y][origin_x + x]
				except IndexError:
					break
				

				word.append(char)

			if word == ["X", "M", "A", "S"]:
				count += 1


print(count)