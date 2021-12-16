import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
template = "OOVSKSPKPPPNNFFBCNOV"
# template = "NNCB"
size = len(template)
start_time = utils.time_check()
height = len(lines)
cc_map = {}
for i in range(height):
    m = lines[i].strip().split(" -> ")
    cc_map[m[0]] =  m[1]

chars = {}
input = template
for c in template:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1
inc = 0

def gen(src):
    pp = ''
    cnt = 0
    for c in src:
        cnt += 1
        pp += c
        if len(pp) > 2:
            pp = pp[1:]
        if pp in cc_map:
            ch = cc_map[pp]
            chars[ch] = 1 if ch not in chars else (chars[ch] + 1)
            # print(f"step {step} pos {cnt}-> {pp} insert: yield {ch}")
            yield ch
        # print(f"step {step} pos {cnt} ->{pp} origin: yield {c}")
        yield c

def queued(queues, ch, q_no, max_q_no):
    queues[q_no] += ch
    if len(queues[q_no]) > 2:
        queues[q_no] = queues[q_no][1:]
    if queues[q_no] in cc_map:
        c = cc_map[queues[q_no]]
        chars[c] = 1 if c not in chars else (chars[c] + 1)
        if q_no < max_q_no:
            queued(queues, c, q_no + 1, max_q_no)
    if q_no < max_q_no:
        queued(queues, ch, q_no + 1, max_q_no)
    
def part1(step = 10):
    queues = ["" for i in range(step)]
    for ch in template:
        queued(queues, ch, 0, step - 1)
    most = max(chars.values())
    least = min(chars.values())
    return most - least      

def part1x(step = 10):
    input = (c for c in template)
    for i in range(step):
        # print(f"Started: step {i}")
        input = (c for c in gen(input))
    s = sum(1 for _ in input)
    # print(f"size = {inc}")
    most = max(chars.values())
    least = min(chars.values())
    return f"final size after {step} steps: {s} result: {most - least}"

def part2():
    return part1(40)

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
    print(f"{sys.argv[1]} result: {result}")
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")

