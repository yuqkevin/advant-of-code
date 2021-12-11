import os
def read_puzzle(caller, puzzle = "input.txt"):
    pfile = os.path.join(os.path.dirname(os.path.realpath(caller)), puzzle)
    with open(pfile) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
