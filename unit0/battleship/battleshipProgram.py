from battleship import Battleship

game = Battleship()

print ("Welcome to Battleship!")
print ("There are 5 ships hidden on the board.")

while game.getNumShipsRemaining() > 0:
    print ("There are", game.getNumShipsRemaining(), "ships left.")
    print ("Here is the board:")
    game.printBoard(True)
    print("Where would you like to guess?")
    row = int(input("Row: "))
    col = int(input("Column: "))
    hit = game.makeMove(row, col)
    if hit:
        print ("Hit!")
    else:
        print ("Miss!")

    print ("")