import sys

from aoc import utils
lines = utils.read_puzzle(__file__)

def add_chain(chain, k, v):
    if k == 'end' or v == "start":
        return chain
    if k not in chain:
        chain[k] = [v]
    elif v not in chain[k]:
        chain[k].append(v)
    return chain

def link_caves():
    link_chain = {}
    pairs = []
    for line in lines:
        a, b = line.split("-")
        link_chain = add_chain(link_chain, a, b)
        link_chain = add_chain(link_chain, b, a)
    return link_chain

def find_path(chain, parent, path, found_path, p2 = False):
    if len(path) == 0:
        # max lower cave visited times
        path.append(0)
    path.append(parent)
    if parent.islower():
        path[0] = max(path[0], path.count(parent))
    for child in chain[parent]:
        if child == "end":
            found_path.append(f"{','.join(path[1:])},end")
            continue
        elif child.islower() and child in path:
            if not p2:
                continue
            if path[0] > 1:
                continue
                    
        org_path = path.copy()
        find_path(chain, child, path, found_path, p2)
        path = org_path    

def part1():
    chain = link_caves()
    found_path = []
    find_path(chain, "start", [], found_path)
    print(f"total found paths: {len(found_path)}")

def part2():
    chain = link_caves()
    found_path = []
    find_path(chain, "start", [], found_path, True)
    print(f"total found paths: {len(found_path)}")

if sys.argv[1]:
	globals()[sys.argv[1]]()

