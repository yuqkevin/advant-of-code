import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
height = len(lines)
width = len(lines[0])

segments = [
    "ABCEFG",
    "CF",
    "ACDEG",
    "ACDFG",
    "BCDF",
    "ABDFG",
    "ABDEFG",
    "ACF",
    "ABCDEFG",
    "ABCDFG"
]

def part1():
    ucodes = 0
    for line in lines:
        digits = line.split('|')[1].split(' ')
        for d in digits:
            if len(d) in [2, 3, 4, 7]:
                ucodes += 1
    print(f"Total unique codes are: {ucodes}")

def decode(pattern, codes):
    mset = {}
    char_map = {}
    for code in pattern:
        size = len(code)
        if size in [2, 3, 4, 7]:
            scode = ''.join(sorted(code))
            if size == 2:
                mset[segments[1]] = scode
            elif size == 3:
                mset[segments[7]] = scode
            elif size == 4:
                mset[segments[4]] = scode
            else:
                mset[segments[8]] = scode

    for c in mset[segments[7]]:
        if c not in mset[segments[1]]:
            char_map["A"] = c
    set5 = [x for x in pattern if len(x) == 5]
    acdfg = [x for x in set5 if mset[segments[1]][0] in x and mset[segments[1]][1] in x][0]
    set5.remove(acdfg)
    dg = ''
    for c in acdfg:
        if c != char_map["A"] and c not in mset[segments[1]]:
            dg += c
    b = mset[segments[4]]
    for c in mset[segments[1]] + dg:
        b = b.replace(c, "")
    char_map["B"] = b
    for c in mset[segments[4]]:
        if c != char_map["B"] and c not in mset[segments[1]]:
            char_map["D"] = c
            char_map["G"] = dg.replace(c, "")
            break
    for str5 in set5:
        for c in list(char_map.values()):
            str5 = str5.replace(c, "")
        if len(str5) == 1:
            char_map["F"] = str5
            char_map["C"] = mset[segments[1]].replace(str5, "")
            break    
    char_map["E"] = [c for c in mset[segments[8]] if c not in list(char_map.values())][0]
    return get_digits(char_map, codes)

def get_digits(char_map, codes):
    cmap = dict((v,k) for k,v in char_map.items())
    # print(f"char_map: {char_map}, codes: {codes}")
    digits = ''
    for code in codes:
        mcode = ''
        for c in code:
            mcode += cmap[c]
        smcode = ''.join(sorted(mcode))
        digits += str(segments.index(smcode))
    return digits

def part2():
    total = 0
    for line in lines:
        data = line.split('|')
        pattern = data[0].strip().split(' ')
        codes = data[1].strip().split(' ')
        digits = decode(pattern, codes)
        total += int(digits)
    print(f"Sum of codes: {total}")

if sys.argv[1]:
	globals()[sys.argv[1]]()

