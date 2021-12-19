import sys
import threading
from time import sleep
from collections import Counter

from aoc import utils

# for generators/queues/threadings methods
def init(step): 
    global rules, chars, queues, template, end_char
    end_char = "0"
    template, _, *rules = utils.read_puzzle(__file__)
    rules = {a[0]:a[1] for a in [(lambda x: x.strip().split(" -> "))(x) for x in rules]}
    queues = ["" for i in range(step)]
    chars = Counter(template)

# deprecated: for generator method only
def gen(src):
    pp = ''
    cnt = 0
    for c in src:
        cnt += 1
        pp += c
        if len(pp) > 2:
            pp = pp[1:]
        if pp in rules:
            ch = rules[pp]
            chars[ch] = 1 if ch not in chars else (chars[ch] + 1)
            yield ch
        yield c

# deprecated: for queues method only
def queued(queues, ch, q_no, max_q_no):
    queues[q_no] += ch
    if len(queues[q_no]) > 2:
        queues[q_no] = queues[q_no][1:]
    if queues[q_no] in rules:
        c = rules[queues[q_no]]
        chars[c] = 1 if c not in chars else (chars[c] + 1)
        if q_no < max_q_no:
            queued(queues, c, q_no + 1, max_q_no)
    if q_no < max_q_no:
        queued(queues, ch, q_no + 1, max_q_no)

# deprecated: for threading method only
def queue_consumer_thread(idx):
    global rules, queues, end_char
    next_idx = None if idx == (len(queues) - 1) else idx + 1
    # print(f"Starting thread {idx}, next thread is {next_idx}")
    while True:
        size = len(queues[idx])
        if size == 0:
            continue
        c = queues[idx][0]
        if next_idx is not None:
            queues[next_idx] += c
        if c == end_char:
            break
        while size < 2:
            size = len(queues[idx])
        cc = queues[idx][0:2]
        if cc in rules:
            c = rules[cc]
            chars[c] = 1 if c not in chars else (chars[c] + 1)
            if next_idx is not None:
                queues[next_idx] += c
        queues[idx] = queues[idx][1:]

def parse(temp_str):
    ch_counter = Counter(temp_str)
    pairs = Counter()
    size = len(temp_str)
    for i in range(size - 1):
        pair = temp_str[i:(i + 2)]
        pairs[pair] += 1
    return [pairs, ch_counter]
        

def steps(start_str, step, rules):
    pairs, ch_counter = parse(start_str) 
       
    for i in range(step):
        src_pairs = pairs.copy()
        for pair in src_pairs:
            if pair in rules:
                c = rules[pair]
                cnt = src_pairs[pair]
                ch_counter[c] += cnt
                pairs[f"{pair[0]}{c}"] += cnt
                pairs[f"{c}{pair[1]}"] += cnt
                pairs[pair] -= cnt
    most = ch_counter.most_common()[0][1]
    least = ch_counter.most_common()[-1][1]
    return most - least

def test(input = "test-input.txt"):
    step = 10
    start_str, _, *rules = utils.read_puzzle(__file__, input)
    rules = {a[0]:a[1] for a in [(lambda x: x.strip().split(" -> "))(x) for x in rules]}
    return "pass" if steps(start_str, step, rules) == 1588 else "failed"
    
def part1(step = 10):
    start_str, _, *rules = utils.read_puzzle(__file__)
    rules = {a[0]:a[1] for a in [(lambda x: x.strip().split(" -> "))(x) for x in rules]}
    return steps(start_str, step, rules)

def part2():
    return part1(40)

# deprecated: threadings
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

# deprecated: queues
def part1_q(step = 10):
    global template, chars
    init(step)
    queues = ["" for i in range(step)]
    for ch in template:
        queued(queues, ch, 0, step - 1)
    most = max(chars.values())
    least = min(chars.values())
    return most - least      

# deprecated: generators
def part1_g(step = 10):
    global template, chars
    init(step)
    input = (c for c in template)
    for i in range(step):
        input = (c for c in gen(input))
    # iterate generators
    sum(1 for _ in input)
    most = max(chars.values())
    least = min(chars.values())
    return most - least

if __name__ == "__main__":
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

