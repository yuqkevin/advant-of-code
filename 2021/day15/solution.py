import sys
from collections import Counter
from aoc import utils

def print_maze(maze):
    for line in maze:
        for i in line:
            print(str(max(0, i)) + ' ', end='')
        print("")

def path_risk(paths, maze):
    min_risk = 0
    min_path = None
    for path in paths:
        risk = sum([maze[p[0]][p[1]] for p in path])
        if min_risk == 0 :
            min_risk = risk
            min_path = path
        elif risk < min_risk:
            min_risk = risk
            min_path = path
    dm = len(maze)
    print(f"min path: {min_path}")
    return min_risk - maze[0][0]    

def find_paths(maze):
    paths = []
    stack = []
    points = []
    dm = len(maze)
    x = y = 0
    cnt = 0
    maze = [(lambda x: [ z - 1 for z in x])(y)  for y in maze]
    while True:
        if x == dm - 1 and y == dm - 1:
            paths.append(points)
            if len(stack) == 0:
                break
        cnt += 1
        # print(f"cnt={cnt}: [{x}, {y}] {points}, {stack}")
        val = maze[x][y]
        if val <= 0:
            points.append([x, y])
            # neighours = [[min(dm - 1, x + 1), y], [x, min(dm - 1, y + 1)], [max(0, x -1), y], [x, max(0 , y - 1)]]
            neighours = [[min(dm - 1, x + 1), y], [x, min(dm - 1, y + 1)]]
            next_steps = []
            for p in neighours:
                if maze[p[0]][p[1]] <= 0 and p not in points:
                    next_steps.append([p, [x, y]])
            if len(next_steps):
                p, _ = next_steps.pop()
                # print(f"next: {p} and save branch: {next_steps}")
                stack += next_steps
                x = p[0]
                y = p[1]
                # print(f"stack={stack}")
                continue
            elif len(stack) > 0:
                p, prev = stack.pop()
                points = points[0:points.index(prev) + 1]
                # print(f"sliced points to prev={prev}: points={points}")
                x = p[0]
                y = p[1]
            elif len(paths) == 0:
                maze = [(lambda x: [ z - 1 for z in x])(y)  for y in maze]
                x = y = 0
                points = []
                stack = []
            else:
                break
    print_maze(maze)
    print(f"found {len(paths)} paths")
    return paths

def is_for_pool(maze, pool, x, y):
    dm = len(maze)
    val = maze[x][y]
    if val > 0:
        return False
    if (x, y) in pool:
        return False
    neighours = [[min(dm - 1, x + 1), y], [x, min(dm - 1, y + 1)], [max(0, x -1), y], [x, max(0 , y - 1)]]
    for p in neighours:
        if maze[p[0]][p[1]] < 1 and tuple(p) in pool:
            return True

def find_pools(maze, a, b):
    pools = [{tuple(a)}, {tuple(b)}]
    dm = len(maze)
    pointers = [[0, 0], [dm - 1, dm - 1]]
    for x in range(a[0], dm):
        for y in range(a[0], dm):
            # print(f"check pt [{x}, {y}] for pool 0")
            if is_for_pool(maze, pools[0], x, y):
                pools[0].add((x, y))
                pointers[0] = [max(pointers[0][0], x), max(pointers[0][1], y)]
            elif x > pointers[0][0] + 1 and y > pointers[0][1] + 1:
                break
    dm_b = b[1] + 1
    for i in range(dm_b):
        for j in range(dm_b):
            x = b[1] - i
            y = b[1] - j
            if is_for_pool(maze, pools[1], x, y):
                pools[1].add((x, y))
                pointers[1] = [min(pointers[1][0], x), min(pointers[1][1], y)]
            elif x < pointers[1][0] - 1 and y < pointers[1][1] - 1:
                break
    return (pools, pointers)
    # return  (pools[0].intersection(pools[1]))

def find_point(pools, pointers):
    pass
def find_points(maze, a, b):
    points = []
    point = None
    cnt = 0
    off_pools = []
    off_pointers = []
    on_pools = []
    off_maze = []
    while cnt < 3 and True:
        cnt += 1
        pools, pointers = find_pools(maze, a, b)
        if len(pools[0]) == 1 and len(pools[1]) == 1:
            maze = [(lambda x: [ z - 5 for z in x])(y)  for y in maze]
            continue
        if len(pools[0].intersection(pools[1])) == 0:
            off_pools = pools
            off_pointers = pointers
            off_maze = maze.copy()
            if len(on_pools) == 0:
                maze = [(lambda x: [ z - 1 for z in x])(y)  for y in maze]
                continue
        else:
            on_pools = pools
            if len(off_pools) == 0:
                maze = [(lambda x: [ z + 1 for z in x])(y)  for y in maze]
                continue
        print(off_pools)
        print_maze(off_maze)
        print(off_pointers)
        # print_maze(maze)
            
        
     
def test(input = "test-input.txt"):
    lines = utils.read_puzzle(__file__, input)
    # dm = len(lines)
    # a = lines[0][0]
    # z = lines[dm -1][dm - 1]
    
    # pool = []
    # for line in lines:
    #     pool += [int(x) for x in line]
    # pool = [x - 1 for x in pool]
    # find_pools(pool, a, z)
    # print(pool)
    maze = [(lambda x: [int(z) for z in list(x)])(y)  for y in lines]
    # maze = [(lambda x: [ int(z) - 5 for z in x])(y)  for y in lines]
    dm = len(maze)
    find_points(maze, [0, 0], [dm - 1, dm - 1])
    print("============")
    print_maze(maze)

    # paths = find_paths(maze.copy())
    # return path_risk(paths, maze)

def part1():
    maze = utils.read_puzzle(__file__)
    maze = [(lambda x: [int(z) for z in list(x)])(y)  for y in maze]
    paths = find_paths(maze.copy())
    return path_risk(paths, maze)

def part2():
    pass

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