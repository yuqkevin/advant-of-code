import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
height = len(lines)
width = len(lines[0])

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

def has_lower(path):
    for n in path:
        if n != "start" and n.islower():
            return True
    return False

def find_path(chain, parent, path, found_path, p2 = False):
    path.append(parent)
    for child in chain[parent]:
        if child == "end":
            found_path.append(f"{','.join(path)},end")
            continue
        elif child.islower() and child in path:
            if not p2:
                continue
            # # this method much slower than use for loop
            # if len([x for x in path if x.islower() and path.count(x) > 1]) > 0:
            #     continue
            stop = False
            for p in path:
                if p.islower() and path.count(p) > 1:
                    stop = True
                    break
            if stop:
                continue
                    
        org_path = path.copy()
        find_path(chain, child, path, found_path, p2)
        path = org_path

        

def part1():
    # rule1: can not go back to start
    # rule2: visit small caves at most once
    chain = link_caves()
    # print(chain)
    found_path = []
    find_path(chain, "start", [], found_path)
    # print('\n'.join(found_path))
    print(f"total found paths: {len(found_path)}")

def part2():
    chain = link_caves()
    # print(chain)
    found_path = []
    find_path(chain, "start", [], found_path, True)
    # print('\n'.join(found_path))
    print(f"total found paths: {len(found_path)}")

if sys.argv[1]:
	globals()[sys.argv[1]]()

