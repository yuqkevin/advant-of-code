import sys

from aoc import utils
content = utils.read_content(__file__)
# content = "16,1,2,0,4,2,7,1,2,14"
line1 = content.split(',')
line = [int(x) for x in line1 ]

def compute_fuel(part2 = False):
    counted = []
    min_fuel = 0
    max_in_line = max(line)
    for pos in range(0, max_in_line):
        if pos in counted:
            continue
        po = pos
        fuel = 0
        for p in line:
            if not part2:
                fuel += abs(p - po)
            else:
                fuel += sum(range(1, abs(p - po) + 1))
        if min_fuel == 0:
            min_fuel = fuel
        else:
            min_fuel = min(min_fuel, fuel)
    return min_fuel    

def part1():
    min_fuel = compute_fuel()
    print(f"Part1 min fuel: {min_fuel}")

def part2():
    min_fuel = compute_fuel(True)
    print(f"Part2 min fuel: {min_fuel}")

if sys.argv[1]:
	globals()[sys.argv[1]]()

