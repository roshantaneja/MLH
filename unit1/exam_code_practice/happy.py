from util import *
'''
As you’re walking around throughout the day, you seem to be stuck 
in a series of unfortunate events. Things are constantly going wrong! 
Everywhere you step, you accumulate misfortune – your goal is to get 
the minimum level of sadness.

Your goal is to find a path from left to right (from column 0 to 
column len(field[0])-1) through the field, accumulating misfortune 
as you go, that minimizes overall sadness, where sadness is defined as 
the sum of misfortune amounts along the path. All rows (r, 0) (for r 
values of 0 to len(field)-1) are valid starting positions. Each subsequent 
step of the way, you must proceed to the next column by moving up one row, 
or staying in the same row, or moving down one row (of course, always 
staying on the field) until you come out the right side. Your task is to 
implement the function pathToHappiness that takes a field as an input 
(a 2D tuple), and returns a minimum sadness path as a list of the row 
indices through the field that minimizes sadness.


Let's say the field was:
((100, 3, 5), 
 (2,   4, 6))

For this example, pathToHappiness(field) should return path [1, 0, 0], 
which is the 2 in row 1, the 3 in row 0, and the 5 in row 0.

If there is more than one path with the same min sadness, you can return
either.
'''

def pathToHappiness(field):
	m = len(field)
	n = len(field[0])
	q = PriorityQueue()
	for r in range(m):
		q.push((r, field[r][0], [r]), field[r][0])

	while q:
		row, cost, path = q.pop()
		if len(path) == n:
			return path
		for dr in [-1, 0, 1]:
			if 0 <= row + dr < m:
				q.push((row + dr, field[row + dr][len(path)], path + [row + dr]), cost + field[row + dr][len(path)])
	
	return None


if __name__=="__main__":

	field = ((100, 3, 5),
		  	 (2,   4, 6))

	print(pathToHappiness(field))