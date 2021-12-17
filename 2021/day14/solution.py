import sys
import threading
from time import sleep

from aoc import utils
lines = utils.read_puzzle(__file__)
template = "OOVSKSPKPPPNNFFBCNOV"
# template = "NNCB"
# pattern map
start_time = utils.time_check()
cc_map = {}
# char frequence counter
chars = {}
# process step char stream queues, each queue will be maintained in zise of 2 
queues = []
# end character
end_char = "0"

def init(step):
    global lines, cc_map, chars, queues
    queues = ["" for i in range(step)]
    height = len(lines)
    cc_map = {}
    for i in range(height):
        m = lines[i].strip().split(" -> ")
        cc_map[m[0]] =  m[1]

    chars = {}
    for c in template:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

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

def queue_consumer_thread(idx):
    global cc_map, queues, end_char
    next_idx = None if idx == (len(queues) - 1) else idx + 1
    # print(f"Starting thread {idx}, next thread is {next_idx}")
    while True:
        size = len(queues[idx])
        if size == 0:
            continue
        c = queues[idx][0]
        if next_idx is not None:
            queues[next_idx] += c
        # else:
        #     print(queues[idx][0], end='')
        if c == end_char:
            break
        while size < 2:
            # sleep(0.005)
            size = len(queues[idx])
        cc = queues[idx][0:2]
        # if next_idx is None:
        #     print(f"Thread {idx} read {cc}")
        if cc in cc_map:
            c = cc_map[cc]
            chars[c] = 1 if c not in chars else (chars[c] + 1)
            if next_idx is not None:
                queues[next_idx] += c
            # else:
            #     print(c, end='')
        queues[idx] = queues[idx][1:]

def part1_t(step = 10):
    global template, chars, queues, end_char
    init(step)
    threads = []
    for idx in range(step):
        x = threading.Thread(target=queue_consumer_thread, args=(idx,))
        x.start()
        threads.append(x)

    for c in template:
        queues[0] += c
    queues[0] += end_char

    for t in threads:
        t.join()
    most = max(chars.values())
    least = min(chars.values())
    return most - least  


def part1_q(step = 10):
    global template, chars
    init(step)
    queues = ["" for i in range(step)]
    for ch in template:
        queued(queues, ch, 0, step - 1)
    most = max(chars.values())
    least = min(chars.values())
    return most - least      

def part1(step = 10):
    global template, chars
    init(step)
    input = (c for c in template)
    for i in range(step):
        input = (c for c in gen(input))
    s = sum(1 for _ in input)
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
    print(f"\n{sys.argv[1]} result: {result}")
    print(f"{sys.argv[1]} time used: {perf['s']} seconds {perf['ms']} ms {perf['µs']} µs {perf['ns']} ns.")

