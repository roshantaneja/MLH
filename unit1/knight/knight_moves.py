from util import *

def minKnightMoves(start, goal):
	# BFS
	visited = set()
	queue = [(start, 0)]
	while queue:
		# print(queue)
		# print(visited)
		curr = queue.pop(0)
		if curr[0] == goal:
			return curr[1]
		if curr[0] in visited:
			continue
		visited.add(curr[0])
		# Add all possible moves
		x, y = curr[0]
		
		queue.append(((x+1, y+2), curr[1]+1))
		queue.append(((x+2, y+1), curr[1]+1))
		queue.append(((x-1, y+2), curr[1]+1))
		queue.append(((x-2, y+1), curr[1]+1))
		queue.append(((x+1, y-2), curr[1]+1))
		queue.append(((x+2, y-1), curr[1]+1))
		queue.append(((x-1, y-2), curr[1]+1))
		queue.append(((x-2, y-1), curr[1]+1))
	return -1

if __name__=="__main__":
	pass