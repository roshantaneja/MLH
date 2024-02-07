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
	q = [((0, c), []) for c in range(n) if grid[0][c] == 1]
	while q:
		(r, c), path = q.pop(0)
		if r == m - 1:
			return path + [(r, c)]
		for dr, dc in ((1, 0), (1, 1), (1, -1)):
			nr, nc = r + dr, c + dc
			if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
				q.append(((nr, nc), path + [(r, c)]))


if __name__=="__main__":
	pass
