import os
from time import perf_counter_ns

def read_puzzle(caller, puzzle = "input.txt"):
    pfile = os.path.join(os.path.dirname(os.path.realpath(caller)), puzzle)
    with open(pfile) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def read_content(caller, puzzle = "input.txt"):
    pfile = os.path.join(os.path.dirname(os.path.realpath(caller)), puzzle)
    with open(pfile) as file:
        content = file.read().strip()
    return content

def print_lines(lines):
    for line in lines:
        print(line)

def print_cells(lines):
    for line in lines:
        for c in line:
            print(c)

def int_lines(lines):
    height = len(lines)
    for i in range(height):
        lines[i] = [int(x) for x in lines[i]]
    return lines

def time_check(count_from = None):
    cur_time = perf_counter_ns()
    if count_from is None:
        return cur_time
    d = perf_counter_ns() - count_from
    seconds = d//(10**9)
    mils = (d%(10**9))//(10**6)
    mics = (d%(10**6))//(10**3)  # µs
    ns = d%(1000)
    return {
        "total_in_ns": d,
        "s": seconds,
        "ms": mils,
        "µs": mics,
        "ns": ns
    }
