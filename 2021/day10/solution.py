import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
start_time = utils.time_check()
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
	return f"score: {score}"

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
	return f"size: {len(scores)}, middle key: {mid_key}, middle score: {scores[mid_key]}"
	
if __name__ == "__main__":
    result = None
    if len(sys.argv) < 2 or sys.argv[1] not in ["part1", "part2"]:
        print("\nSorry, I don't get it, \nI need know which part you want to run, part1 or part2?\n")
        sys.exit()
    if sys.argv[1] == "part1":
        result = part1()
    else :
        result = part2()
        
    perf  = utils.time_check(start_time)
    print(result)
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")
