import time

def makeMove(p1side, p2side, player, move):
	'''
	Remember, when a player makes a move in Mancala, they
	take all the stones from the chosen pit, then one by one 
	place them in the next pit going counter clock wise. Stones
	are placed in their personal Mancala, but not the other players.

	This method should MODIFY p1side and p2side to reflect the new
	configuration, and should return True if the player ended their turn
	in their Mancala, and False otherwise.

	Remember, if the player ends their turn in an EMPTY location on their
	own side (not including the Mancala) and the opposite side placement has
	stones in it, those stones and the one in the previously empty location
	get captured and put in the player's Mancala.
	'''

	if player == 1:
		own_side = p1side
		other_side = p2side
	else:
		own_side = p2side
		other_side = p1side
	
	# Get the number of stones in the chosen pit
	
	hand = own_side[move]
	own_side[move] = 0

	# Place the stones in the pits, one by one, counter-clockwise
	# If the player is on their own side, they should skip the other player's Mancala
	
	current_side = own_side
	current_pit = move + 1

	while hand > 0:
		if current_pit == 6 and current_side == other_side:
			current_pit = 0
			current_side = own_side
		if current_pit == 7 and current_side == own_side:
			current_pit = 0
			current_side = other_side
		
		
		current_side[current_pit] += 1
		hand -= 1
		current_pit += 1
	
	# If the player ends their turn in an empty pit on their own side, and the opposite pit has stones in it, capture them

	if current_side == own_side and current_pit < 6 and current_side[current_pit] == 1 and other_side[5-current_pit] > 0:
		own_side[6] += other_side[5-current_pit] + 1
		other_side[5-current_pit] = 0
		current_side[current_pit] = 0
		current_side[6] += 1

	if current_pit == 7 and current_side == own_side:
		return True
	elif current_pit == 6 and current_side == other_side:
		return False

def getAllPossibleMoves(p1side, p2side, player):
	'''
	Returns all the valid moves a player can make.
	A player can not make a move at an empty pit.
	'''
	moves = []
	for i in range(0,6):
		if player == 1:
			if p1side[i]!=0:
				moves.append(i)
		else:
			if p2side[i]!=0:
				moves.append(i)
	return moves

def isVictory(p1side, p2side):
	'''
	Returns the player (1 or 2) who has won, or
	"ongoing" if the game is still in progress.
	'''
	if p1side[:-1].count(0) == len(p1side[:-1]):
		p2side[-1]+=sum(p2side[:-1])
		for i in range(len(p2side)-1):
			p2side[i]=0
	if p2side[:-1].count(0) == len(p2side[:-1]):
		p1side[-1]+=sum(p1side[:-1])
		for i in range(len(p1side)-1):
			p1side[i]=0
		
	if p1side[:-1].count(0)!=len(p1side[:-1]) and p2side[:-1].count(0)!=len(p2side[:-1]):
		return "ongoing"
	if p1side[-1]>p2side[-1]:
		return 1
	return 2

def copySide(side):
	'''
	Returns a non-aliasing copy of this side of the board.
	This will be useful when coding your minimax player.
	'''
	return [s for s in side]

def swapPlayer(player):
	'''
	Returns the opposite of the current player, useful in 
	implementing minimax.
	'''
	if player == 1:
		return 2
	return 1

def displayBoard(p1side, p2side):
    '''
    Displays the game board as ASCII-art based on the 
    two board lists.
    '''
    seedAmounts = []
    for pit in p2side[:-1][::-1]+p2side[-1:]+p1side[-1:]+p1side[:-1]:
        numSeedsInThisPit = str(pit).rjust(2)
        seedAmounts.append(numSeedsInThisPit)
    # print(seedAmounts)
    print("""
        +------+------+--<<<<<-Player 2----+------+------+------+
        P      |5     |4     |3     |2     |1     |0     |      P
        2      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      1
        S      |      |      |      |      |      |      |      S
        T  {}  +------+------+------+------+------+------+  {}  T
        O      |0     |1     |2     |3     |4     |5     |      O
        R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
        E      |      |      |      |      |      |      |      E
        +------+------+------+-Player 1->>>>>-----+------+------+
    
        """.format(*seedAmounts))

def humanMove(p1side, p2side, player):
    '''
    Code to get input for player move. Should ensure that move
    is valid.
    '''
    move = input("Player "+str(player)+", choose move 0-5: ")

    while (not move.isdigit() or int(move)<0 or int(move)>5 or 
        (player==1 and p1side[int(move)]==0) or
        (player==2 and p2side[int(move)]==0)):
        print("Not a valid move.")
        move = input("Player "+str(player)+", choose move 0-5: ")
    return int(move)

def anyMove(func, p1side, p2side, player):
    '''
    Makes a generic using the specific given function.
    Prints out the amount of time it takes to make the move.
    Handles moving multiple times in one turn.
    '''
    tic = time.time()
    move = func(p1side, p2side, player)
    toc = time.time()
    print("You took",toc-tic,"seconds to move!")
    while makeMove(p1side, p2side, player, move):
        displayBoard(p1side, p2side)
        print("You get to move again!")
        tic = time.time()
        move = func(p1side, p2side, player)
        toc = time.time()
        print("You took",toc-tic,"seconds to move!")
