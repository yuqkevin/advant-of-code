import os
import sys

from aoc import utils
input_file = os.path.dirname(os.path.realpath(__file__)) + '/input.txt'
lines = utils.read(input_file)
height = len(lines)
width = len(lines[0])
for i in range(height):
    lines[i] = [int(x) for x in lines[i]]

def stepup():
    fpoints = []
    for i in range(height):
        for j in range(width):
            lines[i][j] = int(lines[i][j]) + 1
            if lines[i][j] > 9:
                lines[i][j] = 0
                fpoints.append([i, j])
    return fpoints

# def check_flash():
#     fpoints = []
#     for i in range(height):
#         for j in range(width):
#             if lines[i][j] == 10:
#                 adjacent_inc(i, j)
#                 fpoints.append([i, j])
#     return fpoints

def adjacent_inc(i, j):
    if 9 > lines[i][j] > 0:
        lines[i][j] += 1
    elif lines[i][j] == 9:
        lines[i][j] = 0
        return True
    return False

def adjacent(i, j):
    fpoints = []
    for n in [-1, 0, 1]:
        if i > 0 and 0 <= (j + n) < width:
            if (adjacent_inc(i - 1, j + n)):
                adjacent(i - 1, j + n)
        # else:
        #     print(f"boundary: [{i - 1},{j + n}] from [{i},{j}]")
    for n in [-1, 1]:
        if 0 <= (j + n) < width:
            if (adjacent_inc(i, j + n)):
                adjacent(i, j + n)
        # else:
        #     print(f"boundary: [{i},{j + n}] from [{i},{j}]")
    for n in [-1, 0, 1]:
        if (i + 1) < height and 0 <= (j + n) < width:
            if (adjacent_inc(i + 1, j + n)):
                adjacent(i + 1, j + n)
        # else:
        #     print(f"boundary: [{i + 1},{j + n}] from [{i},{j}]")
    return fpoints

def count_flash():
    flash = 0
    for line in lines:
        flash += line.count(0)
    return flash

def print_lines(step, flash=0):
    print(f"printing lines at [step={step},flash={flash}]:")
    for line in lines:
        print(line)

def part1():
    total_flash = 0
    # print_lines(0, total_flash)
    for step in range(100):
        fpoints = stepup()
        for p in fpoints:
            adjacent(*p)
        total_flash += count_flash()
        # print_lines(step + 1, total_flash)
    print(f"Total flashes: {total_flash}")

def part2():
    print("result of part2")

if sys.argv[1]:
	globals()[sys.argv[1]]()

