import sys
from collections import Counter
from aoc import utils

def print_maze(maze, paths = None):
    path_points = set()
    dm = len(maze)
    CGREEN = '\033[92m'
    CEND = '\033[0m'
    risk = 0
    if paths is not None:
        p = (dm - 1, dm - 1)
        while p != (0, 0):
            path_points.add(p)
            p = paths[p]
        path_points.add(p)
        risk = -maze[0][0]
    for i in range(dm):
        for j in range(dm):
            if paths is not None and (i, j) in path_points:
                risk += maze[i][j]
                print(f"{CGREEN}{str(maze[i][j])}{CEND}", end='')
            else:
                print(str(maze[i][j]) + '', end='')
        print(f" .... risk: {risk}")
    print(f"risk of path: {risk}")

def dijkstra(maze):
    dm = len(maze)
    s = (0, 0)
    visited = set()
    checked = {(0, 0): 0}
    end_point = (dm -1, dm -1)
    end_risk = 0
    parents = {}
    while True:
        x, y= s
        skey = f"{x},{y}"
        neighours = {(min(dm - 1, x + 1), y), (x, min(dm - 1, y + 1)), (max(0, x -1), y), (x, max(0 , y - 1))}
        for p in neighours:
            if p == s or p in visited:
                continue
            risk = checked[s] + maze[p[0]][p[1]]
            if p not in checked or checked[p] > risk:
                checked[p] = risk
                parents[p] = s
            # checked[p] = min(checked[p], risk) if p in checked else risk
            # if p[0] == dm - 1 and p[1] == dm - 1:
            #     print(f"s={s}, p={p}, p-value: {maze[p[0]][p[1]]}, checked-s: {checked[s]}, checked-p: {checked[p]}")
        visited.add(s)
        del checked[s]
        if len(checked) == 0:
            break
        min_p = min(checked, key = checked.get)
        if min_p == end_point:
            end_risk = checked[min_p]
            break
        s = min_p
    # print_maze(maze, parents)
    return end_risk

def expand_maze(maze, times):
    tile = maze.copy()
    exp_times = 2 * times
    dm = len(maze)
    for i in range(exp_times):
        tile = [(lambda x: [int(z%9 + 1) for z in list(x)])(y)  for y in tile]
        x = int(i/times)
        y = i % times

        if x == 0:
            for j in range(dm):
                maze[x + j] += tile[j]
        if i < times:
            maze += tile
        else:
            for k in range(times):
                for j in range(dm):
                    maze[dm* (k + 1) + j] += tile[j]
    return maze


def test(input = "test-input.txt"):
    lines = utils.read_puzzle(__file__, input)
    maze = [(lambda x: [int(z) for z in list(x)])(y)  for y in lines]
    result = "part1: " + "pass" if 40 == dijkstra(maze) else "failed"
    print("Part 2:")
    result = dijkstra(expand_maze(maze, 4))
    print(f"result={result}")
    return "pass" if result == 315 else "failed"


def part1():
    lines = utils.read_puzzle(__file__)
    maze = [(lambda x: [int(z) for z in list(x)])(y)  for y in lines]
    return dijkstra(maze)

def part2():
    lines = utils.read_puzzle(__file__)
    maze = [(lambda x: [int(z) for z in list(x)])(y)  for y in lines]
    return dijkstra(expand_maze(maze, 4))

def main():
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

if __name__ == "__main__":
    main()