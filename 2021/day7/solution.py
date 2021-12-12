import sys

from aoc import utils
content = utils.read_content(__file__)
# content = "16,1,2,0,4,2,7,1,2,14"
line1 = content.split(',')
line = [int(x) for x in line1 ]

# def ordered_pos():
#     pos_counts = {x: line.count(x) for x in line}
#     spos = dict(sorted(pos_counts.items(), key=lambda item: item[1]))
#     return list(reversed(list(spos.keys())))

def compute_pos_fuel(pos, part2 = False):
    fuel = 0
    for p in line:
        moves = abs(p - pos)
        if not part2:
            fuel += moves
        else:
            fuel += sum(range(1, moves + 1))
    return fuel

def compute_min_fuel(points, fuels = {}, part2 = False):
    # points = [min, max]
    start_fuel = 0
    end_fuel = 0
    if points[0] in fuels:
        start_fuel = fuels[points[0]]
    else:
        start_fuel = compute_pos_fuel(points[0], part2)
        fuels[points[0]] = start_fuel
    if points[1] in fuels:
        end_fuel = fuels[points[1]]
    else:
        end_fuel = compute_pos_fuel(points[1], part2)
        fuels[points[1]] = end_fuel
    mid = int((points[0] + points[1])/2)
    if mid in points:
        result = points[0] if start_fuel < end_fuel else points[1]
        return [result, fuels[result]]
    mid_fuel = compute_pos_fuel(mid, part2)
    fuels[mid] = mid_fuel
    if (start_fuel - mid_fuel) > (end_fuel - mid_fuel):
        points = [mid, points[1]]
    else:
        points = [points[0], mid]
    return compute_min_fuel(points, fuels, part2)

def part1():
    points = [min(line), int((max(line) + min(line))/2), max(line)]
    result = compute_min_fuel(points)
    print(f"Part1 min fuel: {result[1]} at position: {result[0]}")

def part2():
    points = [min(line), int((max(line) + min(line))/2), max(line)]
    result = compute_min_fuel(points, {}, True)
    print(f"Part2 min fuel: {result[1]} at position: {result[0]}")

if sys.argv[1]:
	globals()[sys.argv[1]]()

