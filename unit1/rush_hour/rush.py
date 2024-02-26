import matplotlib.pyplot as plt

from helper import *
from util import *
from copy import deepcopy

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

            possible_left = False
            possible_right = False

            if cars[car][0][1] != 0:
                possible_left = board[cars[car][0][0]][cars[car][0][1] - 1] == -1
            if cars[car][-1][1] != 5:
                possible_right = board[cars[car][-1][0]][cars[car][-1][1] + 1] == -1


            if possible_left:
                new_cars = copyCars(cars)
                for i in range(len(new_cars[car])):
                    new_cars[car][i] = (new_cars[car][i][0], new_cars[car][i][1] - 1)
                successors.append(makeBoard(new_cars))

            if possible_right:
                new_cars = copyCars(cars)
                for i in range(len(new_cars[car])):
                    new_cars[car][i] = (new_cars[car][i][0], new_cars[car][i][1] + 1)
                successors.append(makeBoard(new_cars))
        else:
            #vertical

            possible_up = False
            possible_down = False

            if cars[car][0][0] != 0:
                possible_up = board[cars[car][0][0] - 1][cars[car][0][1]] == -1
            if cars[car][-1][0] != 5:
                possible_down = board[cars[car][-1][0] + 1][cars[car][0][1]] == -1

            if possible_up:
                new_cars = copyCars(cars)
                for i in range(len(new_cars[car])):
                    new_cars[car][i] = (new_cars[car][i][0] - 1, new_cars[car][i][1])
                successors.append(makeBoard(new_cars))
            
            if possible_down:
                new_cars = copyCars(cars)
                for i in range(len(new_cars[car])):
                    new_cars[car][i] = (new_cars[car][i][0] + 1, new_cars[car][i][1])
                successors.append(makeBoard(new_cars))

    return successors






def goalTest(board):
    return board[2][5] == 0 and board[2][4] == 0

def BFS(start):
    '''
    Implement basic BFS below, using an expanded set to speed
    up the search.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [start])]
    visited = set()
    while q:
        cur, path = q.pop(0)
        string_state = getStringBoard(cur)
        if goalTest(cur):
            return path, len(visited)
        if string_state in visited:
            continue
        visited.add(string_state)
        for s in getSuccessors(cur):
            if getStringBoard(s) not in visited:
                q.append((s, path + [s]))
    return None
        


def astarDistToExit(start):
    '''
    A* using distToExitHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [start], 0)]
    visited = set()
    while q:
        cur, path, cost = q.pop(0)
        string_state = getStringBoard(cur)
        if goalTest(cur):
            return path, len(visited)
        if string_state in visited:
            continue
        visited.add(string_state)
        for s in getSuccessors(cur):
            if getStringBoard(s) not in visited:
                q.append((s, path + [s], cost + 1))
        q.sort(key=lambda x: cost + distToExitHeuristic(x[0]))
    return None

def distToExitHeuristic(board):
    '''
    How far is the car from the exit location?-09
    '''
    cars = makeCars(board)
    return 6 - cars[0][1][1]

def astarCarsBlocking(start):
    '''
    A* using carsBlockingHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [start], 0)]
    visited = set()
    while q:
        cur, path, cost = q.pop(0)
        string_state = getStringBoard(cur)
        if goalTest(cur):
            return path, len(visited)
        if string_state in visited:
            continue
        visited.add(string_state)
        for s in getSuccessors(cur):
            if getStringBoard(s) not in visited:
                q.append((s, path + [s], cost + 1))
        q.sort(key=lambda x: cost + carsBlockingHeuristic(x[0]))
    return None

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    cars = makeCars(board)
    red_car = cars[0]
    blocking = 0
    for i in range(red_car[1][1] + 1, 6):
        if board[red_car[1][0]][i] != -1:
            blocking += 1
    return blocking

def astarYourHeuristic(start):
    '''
    A* using myHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [start], 0)]
    visited = set()
    while q:
        cur, path, cost = q.pop(0)
        string_state = getStringBoard(cur)
        if goalTest(cur):
            return path, len(visited)
        if string_state in visited:
            continue
        visited.add(string_state)
        for s in getSuccessors(cur):
            if getStringBoard(s) not in visited:
                q.append((s, path + [s], cost + 1))
        q.sort(key=lambda x: cost + myHeuristic(x[0]))
    return None

def myHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write an admissible heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    return carsBlockingHeuristic(board) + distToExitHeuristic(board)


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)

    # uncomment for successors!
    successors = getSuccessors(board)
    plotSuccessors(board, successors)
    plt.show()
