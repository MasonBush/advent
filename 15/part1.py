
def readInput(input:str):

	with open(input, "r") as f:
		map: list[list[str]] = []
		moves: list[tuple[int, int]] = []
		startPoint: tuple[int, int] = None

		readMap = True
		for y, line in enumerate(f.readlines()):
			if line == "\n":
				readMap = False

			line = line.rstrip()
			if readMap:
				row = []
				for x, i in enumerate(line):
					if i == ".":
						i = None
					elif i == "@":
						startPoint = (x, y)

					
					row.append(i)
				map.append(row)
			else:
				for i in line:
					match i:
						case "<":
							move = (-1, 0)
						case ">":
							move = (1, 0)
						case "^":
							move = (0, -1)
						case "v":
							move = (0, 1)

					moves.append(move)


	return map, moves, startPoint


def printMap(map):
	for row in map:
		for i in row:
			if i == None:
				i = "."
			print(i, end="")

		print("")


def getMoves(startPos, direction, map, moves: dict = {}):
	if not moves:
		moves = {}

	s_x, s_y = startPos
	d_x, d_y = direction

	n_x = s_x + d_x
	n_y = s_y + d_y

	nextPos = map[n_y][n_x]

	match nextPos:
		case "#":
			moves.clear()
		case None:
			moves[(s_x, s_y)] = (n_x, n_y)
		case _:
			moves[(s_x, s_y)] = (n_x, n_y)
			getMoves((n_x, n_y), direction, map, moves)

	return moves


def makeMoves(moves: dict, map):

	lastIndex = list(moves.keys())[0]

	for start, move in reversed(moves.items()):
		o_x, o_y = start
		m_x, m_y = move


		map[m_y][m_x] = map[o_y][o_x]

	
	l_x, l_y = lastIndex
	map[l_y][l_x] = None
	return moves[lastIndex]
		

map, moves, startPoint = readInput("input.txt")


for i in moves:
	moves = getMoves(startPoint, i, map)
	if moves:
		startPoint = makeMoves(moves, map)


total = 0
for y, row in enumerate(map):
	for x, char in enumerate(row):
		if char == "O":
			total += 100 * y + x
			print()

print(total)