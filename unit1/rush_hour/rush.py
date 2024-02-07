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
    for car in cars:
        if cars[car[0][0]] == cars[1][0]:
            #its horizonal
            return True
            

def goalTest(board):
    '''
    The red car (car idNum 0) must take up locations 
    (2,4) and (2,5) to be a "finished" search.
    '''
    pass

def BFS(start):
    '''
    Implement basic BFS below, using an expanded set to speed
    up the search.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
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

    # # uncomment for successors!
    # successors = getSuccessors(board)
    # plotSuccessors(board, successors)
    plt.show()
