import os
import sys

from aoc import utils
input_file = os.path.dirname(os.path.realpath(__file__)) + '/input.txt'
lines = utils.read(input_file)
height = len(lines)
width = len(lines[0])

bracks = [
	['(', ')', 3, 1],
	['[', ']', 57, 2],
	['{', '}', 1197, 3],
	['<', '>', 25137, 4]
]

def part1():
	errors = []
	score = 0
	for line in lines:
		stack = []
		for c in line:
			err = False
			for bk in bracks:
				if c == bk[0]:
					stack.append(c)
					break
				elif c == bk[1]:
					if stack[-1] == bk[0]:
						stack.pop()
					else:
						errors.append([line, c])
						score += bk[2]
						err = True
						break
			if err:
				break
	print(f"score: {score}")

def part2():
	scores = []
	for line in lines:
		stack = []
		err = False
		for c in line:
			for bk in bracks:
				if c == bk[0]:
					stack.append(c)
					break
				elif c == bk[1]:
					if stack[-1] == bk[0]:
						stack.pop()
					else:
						err = True
						break
			if err:
				break
		if err:
			continue
		score = 0
		while len(stack) > 0:
			c = stack.pop()
			for bk in bracks:
				if c in bk:
					score = score * 5 + bk[3]
		scores.append(score)
	#print(scores)
	mid_key = int(len(scores)/2)
	scores.sort()
	#print(scores)
	print(f"size: {len(scores)}, middle key: {mid_key}, middle score: {scores[mid_key]}")
	
if sys.argv[1]:
	globals()[sys.argv[1]]()
