from computerHelper import *

class Battleship:
    def __init__(self):
        self.board = initializeGameBoard()
        """
        [[“~”, “D”, “~”, “P”, “P”],
         [“~”, “D”, “~”, “~”, “~”],
         [“~”, “D”, “~”, “~”, “~”],
         [“B”, “B”, “B”, “B”, “~”]]
        """

        self.firedAt = []
        self.ships = self.getShipDictionary()
        """
        {“D”:[(0,1), (1,1), (2,1)],
         “P”:[(0,3), (0,4)],
         “B”:[(3,0), (3,1), (3,2), (3,3)]}
        """

    def getShipDictionary(self):
        '''
        Returns a dictionary mapping ship types to the
        coordinates they are placed in on self.board.
        Make sure "~" is not added to the dictionary since 
        it's not a ship!
        '''

        shipDict = {}

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != "~":
                    if self.board[r][c] in shipDict:
                        shipDict[self.board[r][c]].append((r,c))
                    else:
                        shipDict[self.board[r][c]] = [(r,c)]

        return shipDict

    def getNumShipsRemaining(self):
        '''
        Returns the number of ships that are still afloat 
        (i.e. ships that still have >0 coordinates remaining
        in self.ships)
        '''

        numShips = 0
        for ship in self.ships:
            if len(self.ships[ship]) > 0:
                numShips += 1

        return numShips

    def getLocationsFiredAt(self):
        '''
        Returns the list of locations that have already been
        fired at.
        '''
        return self.firedAt

    def makeMove(self, row, col):
        '''
        Returns True if the shot hit a ship, and False otherwise.
        If a shot was fired at a place it has been fired at previously,
        should also return False

        Updates self.firedAt when a new location has been targeted.
        Updates self.ships to remove a coordinate of a ship 
        if one has been hit.
        '''
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):
            return False

        if (row, col) in self.firedAt:
            return False
        
        self.firedAt.append((row, col))

        if self.board[row][col] != "~":
            self.ships[self.board[row][col]].remove((row, col))
            self.board[row][col] = "*"
            return True

        return False

    def makeHiddenBoard(self):
        '''
        Returns the "visible" version of the board based on these
        rules:
        * A location that hasn't been fired on should be water ("~")
        * A location that has been fired on and is a miss (no ship)
          should be blank (" ")
        * A location that has been fired on but is not a complete
          wrecked ship should be an asterisk ("*")
        * And lastly, a location that has been fired on where the ship
          is completely sunk should be the letter corresponding to that 
          ship (either "C", "B", "D", "S", or "P")
        '''

        hiddenBoard = []

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if (r, c) in self.firedAt:
                    if self.board[r][c] == "~":
                        hiddenBoard.append(" ")
                    elif len(self.ships[self.board[r][c]]) == 0:
                        hiddenBoard.append(self.board[r][c])
                    else:
                        hiddenBoard.append("*")
                else:
                    hiddenBoard.append("~")

        return self.board

    def printBoard(self, hidden): 
        '''
        Prints a version of the board to the terminal.
        Parameter hidden is a boolean, set to true if ships that 
        have not been hit on the board yet should remain hidden,
        false otherwise
        '''
        if hidden:
            boardToUse = self.makeHiddenBoard()
        else:
            boardToUse = self.board

        print(" 0123456789")
        for r in range(len(boardToUse)):
            print(r, end="")
            for c in range(len(boardToUse[0])):
                print(boardToUse[r][c], end="")
            print()
    
    

