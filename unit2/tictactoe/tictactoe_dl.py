from helper import *

################################################################
### ---------------- Computer Players ---------------------- ###
################################################################

# Functions below here will act as computer players! Each 
# function should take in the game board and the player, 
# and return a valid move or score (for tic tac toe the location 
# of where the X or O will be placed)

def minimaxMove(board, player):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		the best possible board move, using minimax to find it
	'''
	max_depth = 2

	alpha = -float('inf')
	beta = float('inf')
	_, best_move = maximizer(board, player, max_depth, alpha, beta)

	return best_move


def minimizer(board, player, depth, alpha, beta):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		the highest attainable score from the successors, 
		and the move (tuple row, col coordinate) that gets there
	'''
	if checkVictory(board) != "ongoing" or depth == 0:
		return evaluation_function(board, swapPlayer(player)), None
	
	all_moves = getMoves(board)

	best_score = float("inf")
	best_move = None

	for r, c in all_moves:
		new_board = copyBoard(board)
		new_board[r][c] = player
		score, _ = maximizer(new_board, swapPlayer(player), depth - 1, alpha, beta)
		if score < best_score:
			best_score = score
			best_move = (r, c)
		if score < beta:
			beta = score
		if beta <= alpha:
			break
	return best_score, best_move
		


def maximizer(board, player, depth, alpha, beta):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		the lowest attainable score from the successors, 
		and the move (tuple row, col coordinate) that gets there
	'''
	if checkVictory(board) != "ongoing" or depth == 0:
		return evaluation_function(board, player), None
	
	all_moves = getMoves(board)

	best_score = -float("inf")
	best_move = None


	for move in all_moves:
		new_board = copyBoard(board)
		r, c = move
		new_board[r][c] = player
		score, _ = minimizer(new_board, swapPlayer(player), depth - 1, alpha, beta)
		if score > best_score:
			best_score = score
			best_move = move
		if score > alpha:
			alpha = score
		if alpha >= beta:
			break
	return best_score, best_move

def getScore(board, player, depth):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		10 if the player wins on the board
		-10 if they don't
		0 otherwise
	'''
	victory = checkVictory(board)
	if victory == player:
		return 10 - depth
	elif victory == swapPlayer(player):
		return -10 + depth
	else:
		return 0

def getAllCombinations(board):
	allCombos = []
	diagonal = []
	backDiag = []

	for i in range(3):
		diagonal.append(board[i][i])
		backDiag.append(board[i][-i])
	
	allCombos.append(diagonal)
	allCombos.append(backDiag)

	for row in board:
		allCombos.append(row)
	
	for c in range(3):
		col = []
		for r in range(3):
			col.append(board[r][c])
		allCombos.append(col)
	
	return allCombos

def evaluateOneCombo(combo, player):
	'''
	3 in a row, 				+100
	3 in a row of opponent, 	-100

	2 in a row, 				+ 10
	2 in a row opponent, 		-10

	1 in a row, 				+1
	1 in a row opponent, 		-1
	'''
	player_count = combo.count(player)
	blank_count = combo.count("_")
	opponent_count = 3 - player_count - blank_count

	if player_count == 3:
		return 100
	elif opponent_count == 3:
		return -100
	elif player_count == 2 and blank_count == 1:
		return 10
	elif opponent_count == 2 and blank_count == 1:
		return -10
	elif player_count == 1 and blank_count == 2:
		return 1
	elif opponent_count == 1 and blank_count == 2:
		return -1
	
	return 0



def evaluation_function(board, player):
	'''
	Return some score for the current board
	'''

	combos = getAllCombinations(board)
	score = 0
	for combo in combo:
		score += evaluateOneCombo(board, player)

def getMoves(board):
	'''
	Returns possible move locations as tuples.
	'''
	moves = []
	for r in range(len(board)):
		for c in range(len(board[0])):
			if board[r][c] == '_':
				moves.append((r, c))

	return moves



