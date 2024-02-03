from util import *
'''
grid is a two dimensional m by n grid, represented as a 
list of lists, with a 0 or a 1 in each cell. Find a path of 
1s from top to bottom starting at a 1 in the top row (row 0) 
and ending at a 1 in the bottom row (row n-1), where you must 
continuously move down  if there is a 1 in the cell moved to. 
Return the path as a list of coordinate tuples (row, column). 
If there is no valid path, return None.
'''

def findPath(grid):
	m = len(grid)
	n = len(grid[0])
	visited = set()
	q = [((0, c), []) for c in range(n) if grid[0][c] == 1]
	while q:
		curr = q.pop(0)
		coord, path = curr
		if coord in visited:
			continue
		visited.add(coord)
		row, col = coord
		if row == m - 1:
			return path + [coord]
		if grid[row][col] == 1:
			q.append(((row + 1, col), path + [coord]))
			if col > 0:
				q.append(((row + 1, col - 1), path + [coord]))
			if col < n - 1:
				q.append(((row + 1, col + 1), path + [coord]))
	return None


if __name__=="__main__":
	pass
