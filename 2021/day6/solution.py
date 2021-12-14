import sys

from aoc import utils
content = utils.read_content(__file__)
start_time = utils.time_check()
content = "3,4,3,1,2"
days = 256
sfishes = content.split(',')
sfishes = [int(x) for x in sfishes]

def gen_day(x):
    if x == 0:
        return (n for n in [6, 8])
    else:
        return (n for n in [x-1])

def part1():
    fishes = sfishes
    for day in range(days):
        fishes = (y for x in fishes for y in gen_day(x))
    cnt = 0
    for fish in fishes:
        cnt += 1
    return f"There are {cnt} fishes after {days} day"

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
    print(result)
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")

