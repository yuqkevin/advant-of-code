import sys

from aoc import utils
lines = utils.read_puzzle(__file__)
height = len(lines)
width = len(lines[0])

def basin(point, basin_points = []):
	if point not in basin_points:
		basin_points.append(point)
	i, j = point
	# top
	if i > 0 and lines[i - 1][j] != '9' and [i - 1, j]  not in basin_points:
		basin_points = basin([i - 1, j], basin_points)
	# left
	if j > 0 and lines[i][j - 1] != '9' and [i, j - 1]  not in basin_points:
		basin_points = basin([i, j - 1], basin_points)
	# bottom
	if i < height - 1 and lines[i + 1][j] != '9' and [i + 1, j]  not in basin_points:
		basin_points = basin([i + 1, j], basin_points)
	# right
	if j < width - 1 and lines[i][j + 1] != '9' and [i, j + 1]  not in basin_points:
		basin_points = basin([i, j + 1], basin_points)
	return basin_points

def part1():
	total_risk = 0
	points = []
	for i in range(height):
		for j in range(width):
			p = int(lines[i][j])
			lp = 9 if j == 0 else int(lines[i][j - 1])
			rp = 9 if j == width -1 else int(lines[i][j + 1])
			tp = 9 if i == 0 else int(lines[i - 1][j])
			bp = 9 if i == height - 1 else int(lines[i + 1][j])
			if p < min(lp, rp, tp, bp):
				points.append([i, j])
				total_risk += 1+ int(p)
	risk = 0
	for i in range(len(points)):
		v = lines[points[i][0]][points[i][1]]
		risk += (int(v) + 1)
	
	print(f"Number of basin bottoms: {len(points)},  total risk: {total_risk}")

def part2():
	points = []
	for i in range(height):
		for j in range(width):
			p = int(lines[i][j])
			lp = 9 if j == 0 else int(lines[i][j - 1])
			rp = 9 if j == width -1 else int(lines[i][j + 1])
			tp = 9 if i == 0 else int(lines[i - 1][j])
			bp = 9 if i == height - 1 else int(lines[i + 1][j])
			if p < min(lp, rp, tp, bp):
				points.append([i, j])
	
	basins = [] 
	for point in points:
		basin_points = basin(point, [])
		basins.append(len(basin_points))
	
	basins.sort()
	print(f"Three largest basion: {basins[-3:]}, Sum of their size: {basins[-3]*basins[-2]*basins[-1]}")
	
if sys.argv[1]:
	globals()[sys.argv[1]]()
