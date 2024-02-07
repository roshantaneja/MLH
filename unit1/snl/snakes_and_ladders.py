from util import *

def snakesAndLadders(finalLocation, snakes, ladders):
	q = []
	visited = set()
	q.append((0, 0))
	while q:
		loc, moves = q.pop(0)
		if loc == finalLocation:
			return moves
		if loc in visited:
			continue
		visited.add(loc)
		for i in range(1, 7):
			new_loc = loc + i
			if new_loc in visited:
				continue
			if new_loc in snakes:
				new_loc = snakes[new_loc]
			if new_loc in ladders:
				new_loc = ladders[new_loc]
			q.append((new_loc, moves+1))
	return -1


if __name__=="__main__":
	# if you'd like to make your own test cases, you
	# can do so here! Otherwise, you can run test.py
	pass
