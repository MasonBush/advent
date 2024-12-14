import re
import math

import PIL.Image

def readInput(input:str) -> list[tuple[int]]:

	robots = []
	with open(input, "r") as f:
		for i in f.readlines():

			results = re.search(r"p=(?P<xPos>\d+),(?P<yPos>\d+) v=(?P<xVel>\d+|-\d+),(?P<yVel>\d+|-\d+)", i)
			robot = ((int(results.group('xPos')), int(results.group('yPos'))), (int(results.group('xVel')), int(results.group('yVel'))))
			robots.append(robot)

	return robots


def printBoard(board):
	for i in board:
		for k in i:
			amount = len(k)
			if amount == 0:
				amount = "."

			print(amount, end="")
		print("")


def generateBoard(size) -> list[list[tuple[int]]]:
	height, width = size

	board = []
	for y in range(height):
		row = []
		for i in range(width):
			row.append([])

		board.append(row)
	return board


def getQuadrants(board: list[list[tuple[int, int]]]) -> tuple[list[list[tuple[int, int]]]]:
	height = len(board)
	width = len(board[0])

	heightSize = math.floor((height / 2) * 1)
	widthSize = math.floor((width / 2) * 1)

	topHalf = board[0:heightSize]
	bottomHalf = board[height-heightSize:height]

	topLeft = list((i[0:widthSize] for i in topHalf))
	topRight = list((i[width-widthSize:width] for i in topHalf))

	bottomLeft = list((i[0:widthSize] for i in bottomHalf))
	bottomRight = list((i[width-widthSize:width] for i in bottomHalf))
	return (topLeft, topRight, bottomLeft, bottomRight)


def simulateBoard(board):
	robots = []
	for y, row in enumerate(board):
		for x, grid in enumerate(row):
			for i in grid:
				robots.append(((x,y), i))

	height = len(board)
	width = len(board[0])
	board = generateBoard((height, width))

	for robot in robots:
		pos, vel = robot
		nextPos_x = pos[0] + vel[0]
		nextPos_y = pos[1] + vel[1]

		if nextPos_x < 0:
			nextPos_x += width
		elif nextPos_x > width - 1:
			nextPos_x -= width

		if nextPos_y < 0:
			nextPos_y += height
		elif nextPos_y > height - 1:
			nextPos_y -= height

		board[nextPos_y][nextPos_x].append(vel)

	return board

robots = readInput("input.txt")
boardSize = (103, 101)

board = generateBoard(boardSize)
for robot in robots:
	pos, vel = robot
	pos_x, pos_y = pos

	board[pos_y][pos_x].append(vel)



from PIL import Image

#yup I really generated 10,000 images and look for a tree
height, width = boardSize
for i in range(10000):
	board = simulateBoard(board)
	image = Image.new(mode="RGB", size=(width, height))

	for y, row in enumerate(board):
		for x, arr in enumerate(row):
			if arr:
				image.putpixel((x, y), (255,255,255))

	image.save(f"images/{i}.png", format="png")