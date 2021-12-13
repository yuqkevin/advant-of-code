import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
# foldes = [["y", 7], ["x", 5]]
foldes = [["x", 655], ["y", 447], ["x", 327], ["y", 223], ["x", 163], ["y", 111], ["x", 81], ["y", 55], ["x", 40], ["y", 27], ["y", 13], ["y", 6]]

start_time = utils.time_check()
height = len(lines)
for i in range(height):
    ps = lines[i].split(",")
    lines[i] = [int(x) for x in ps]

def fold_page(fold, fold_x = False):
    for i in range(height):
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
        return f"dots after {cnt} fold: {dots}"
    # print(f"Part1 dots: {dots}")

def part2():
    dots = 0
    cnt = 0
    for fold in foldes:
        cnt += 1
        dots += fold_page(fold[1], fold[0] == "x")
    
    max_x, max_y = max_xy()
    result = ""
    for y in range(max_y+1):
        for x in range(max_x+1):
            if [x, y] in lines:
                result += "#"
            else:
                result += " "
        result += "\n"
    return result

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
