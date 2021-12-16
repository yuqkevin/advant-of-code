import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
start_time = utils.time_check()
height = len(lines)
width = len(lines[0])
lines = utils.int_lines(lines)
stack = []

def next_step(pt, dm, min_risk):
    if pt[0] < dm - 1:
        if pt[1] < dm - 1:
            low_pt = [pt[0], pt[1] + 1, pt[2] + lines[pt[0]][pt[1] + 1]]
            if low_pt[2] < min_risk or min_risk == 0:
                stack.append(low_pt)
        pt[0] += 1
    elif pt[1] < dm - 1:
        pt[1] += 1
    pt[2] += lines[pt[0]][pt[1]]
    # print(f"dm:{dm} pt: {pt}, min_risk: {min_risk}")
    if pt[2] < min_risk or min_risk == 0:
        return pt
    else:
        return [0, 0, 0]

def get_paths(dm):
    o = [0, 0, 0]
    max_pos = dm - 1
    cnt = 0
    p_cnt = 0
    min_risk = 0
    # print(f"{cnt} start from {o}: {stack}")
    while True:
        # print(f"{cnt} start from {o}: {stack}")
        while (o[0] < max_pos or o[1] < max_pos):
            o = next_step(o, dm, min_risk)
            if o[0] == 0 and o[1] == 0:
                # aborted path
                break
        cnt += 1
        if o[0] == max_pos:
            # full went through path, pick up one with lower risk
            p_cnt += 1
            min_risk = o[2] if min_risk == 0 else min(min_risk, o[2])
            # print(f"{p_cnt}/{cnt}: stack size: {len(stack)} lowest risk: {min_risk} vs {o}")
        if len(stack) == 0:
            break
        # for pt in stack:
        #     print(f"{cnt}: {pt}")
        o = stack.pop()
        while min_risk < o[2]:
            print(f"give up {o}")
            o = stack.pop()
    print(f"{p_cnt}/{cnt}: lowest risk: {min_risk}")
    return min_risk

def part1():
    # utils.print_lines(lines)
    return get_paths(20)

def part2():
    return "result of part2"

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
    print(f"{sys.argv[1]}: the lowet total risk: {result}")
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")

