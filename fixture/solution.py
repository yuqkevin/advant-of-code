import sys
from collections import Counter
from aoc import utils


def test(input = "test-input.txt"):
    pass

def part1():
    pass

def part2():
    pass

def main():
    result = None
    if len(sys.argv) < 2 or sys.argv[1] not in ["part1", "part2", "test"]:
        print("\nSorry, I don't get it, \nI need know which part you want to run, part1 or part2?\n")
        sys.exit()
    start_time = utils.time_check()
    if sys.argv[1] == "part1":
        result = part1()
    elif sys.argv[1] == "part2":
        result = part2()
    else:
        result = test()
        
    perf  = utils.time_check(start_time)
    print(f"\n{sys.argv[1]} result: {result}")
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")

if __name__ == "__main__":
    main()