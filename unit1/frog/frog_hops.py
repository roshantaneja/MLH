from util import *

def getMinHoppingPath(home):

	visited = set()
	q = [(0, 1, [0])]

	while q:
		loc, speed, path = q.pop(0)
		if loc == home:
			return path
		# if loc in visited:
		# 	continue  # redundant
		if loc not in visited:
			visited.add(loc)
			# same_speed = loc+speed
			# new_speed = loc+speed+1
			q.append((loc+speed, speed+1, path+[loc+speed]))
			q.append((loc+speed-1, speed, path+[loc+speed-1]))
	return []


if __name__=="__main__":
	'''
	Feel free to use the main method to try your own tests!
	I've put one down here for you (the example from the 
	instructions)
	'''
	path = getMinHoppingPath(10)
	print(path)
	print(len(path))

	path = getMinHoppingPath(100)
	print(path)
	print(len(path))

	path = getMinHoppingPath(1000)
	print(path)
	print(len(path))