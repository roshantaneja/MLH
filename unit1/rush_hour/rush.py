import matplotlib.pyplot as plt

from helper import *
from util import *

def makeCars(board):
    car_dict = {}
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == -1:
                continue
            if board[r][c] in car_dict:
                car_dict[board[r][c]].append((r, c))
            else:
                car_dict[board[r][c]] = [(r, c)]
    return car_dict

def makeBoard(cars):
    board = [[-1] * 6 for i in range(6)]

    for car in cars:
        for x, y in cars[car]:
            board[x][y] = car
    
    return board

def getSuccessors(board):
    cars = makeCars(board)
    successors = []
    for car in cars:
        if cars[car][0][0] == cars[car][1][0]:
            # horizontal
            possible_left = board[car[0][0]][car[0][1] - 1] == -1
            possible_right = board[car[0][0]][car[-1][1] + 1] == -1

            if possible_left:
                new_cars = cars.copy()
                for section in new_cars[car]:
                    section[1] -= 1
                successors.append(makeBoard(new_cars))

            if possible_right:
                new_cars = cars.copy()
                for section in new_cars[car]:
                    section[1] += 1
                successors.append(makeBoard(new_cars))
        else:
            #vertical
            possible_up = board[car[0][0] - 1][car[0][1]] == -1
            possible_down = board[car[-1][0] + 1][car[0][1]] == -1

            if possible_up:
                new_cars = cars.copy()
                for section in new_cars[car]:
                    section[0] -= 1
                successors.append(makeBoard(new_cars))
            
            if possible_down:
                new_cars = cars.copy()
                for section in new_cars[car]:
                    section[0] += 1
                successors.append(makeBoard(new_cars))

        

    return successors

def goalTest(board):
    cars = makeCars(board)
    return cars[0] == [(2, 4), (2, 5)]

def BFS(start):
    '''
    Implement basic BFS below, using an expanded set to speed
    up the search.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [])]
    visited = set()
    while q:
        cur, path = q.pop(0)
        if goalTest(cur):
            return path, len(visited)
        visited.add(cur)
        for s in getSuccessors(cur):
            if s not in visited:
                q.append((s, path + [s]))
    
    
    pass

def astarDistToExit(start):
    '''
    A* using distToExitHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    pass

def distToExitHeuristic(board):
    '''
    How far is the car from the exit location?
    '''
    pass

def astarCarsBlocking(start):
    '''
    A* using carsBlockingHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    pass

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    pass

def astarYourHeuristic(start):
    '''
    A* using myHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    pass

def myHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write an admissible heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    pass


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)

    # uncomment for successors!
    successors = getSuccessors(board)
    plotSuccessors(board, successors)
    plt.show()
