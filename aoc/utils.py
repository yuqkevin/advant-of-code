import os
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