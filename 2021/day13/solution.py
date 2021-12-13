import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
height = len(lines)
for i in range(height):
    lines[i] = lines[i].split(",")
lines = utils.int_lines(lines)
# foldes = [["y", 7], ["x", 5]]
foldes = [["x", 655], ["y", 447], ["x", 327], ["y", 223], ["x", 163], ["y", 111], ["x", 81], ["y", 55], ["x", 40], ["y", 27], ["y", 13], ["y", 6]]

def fold_page(fold, fold_x = False):
    for i in range(0, height):
        if fold_x:
            if lines[i][0] > fold:
                lines[i][0] = fold - (lines[i][0] - fold)
        else:
            if lines[i][1] > fold:
                lines[i][1] = fold - (lines[i][1] - fold)
    printed = []
    cnt = 0
    for dot in lines:
        if dot not in printed:
            cnt += 1
            printed.append(dot)
    return cnt

def max_xy():
    max_x = 0
    max_y = 0
    for p in lines:
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])
    return [max_x, max_y]


def part1():
    dots = 0
    cnt = 0
    for fold in foldes:
        cnt += 1
        dots += fold_page(fold[1], fold[0] == "x")
        print(f"dots after {cnt} fold: {dots}")
    print(f"Part1 dots: {dots}")

def part2():
    dots = 0
    cnt = 0
    for fold in foldes:
        cnt += 1
        dots += fold_page(fold[1], fold[0] == "x")
    
    max_x, max_y = max_xy()
    print("Result of part2:")
    for y in range(max_y+1):
        for x in range(max_x+1):
            if [x, y] in lines:
                print('#', end="")
            else:
                print('.', end="")
        print("")

if sys.argv[1]:
	globals()[sys.argv[1]]()
