import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
template = "OOVSKSPKPPPNNFFBCNOV"
start_time = utils.time_check()
height = len(lines)
cvt_map = {}
for i in range(height):
    m = lines[i].strip().split(" -> ")
    cvt_map[m[0]] =  m[1]

chars = {}
input = template
for c in template:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

def insert(input):
    size = len(input)
    output = input[0]
    for i in range(2, size + 1):
        pair = input[i-2:i]
        if pair in cvt_map:
            output += cvt_map[pair]
            if cvt_map[pair] in chars:
                chars[cvt_map[pair]] += 1
            else:
                chars[cvt_map[pair]] = 1
        output += input[i-1]
    return output

def part1():
    input = template
    for i in range(40):
        input = insert(input)
    most = max(chars.values())
    least = min(chars.values())
    return f"part1 result: {most - least}"

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

