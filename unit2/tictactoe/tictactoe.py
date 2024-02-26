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
	alpha = -float('inf')
	beta = float('inf')
	_, best_move = maximizer(board, player, 0, alpha, beta)

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
	if checkVictory(board) != "ongoing":
		return getScore(board, swapPlayer(player), depth), None
	
	all_moves = getMoves(board)

	best_score = float("inf")
	best_move = None

	for r, c in all_moves:
		new_board = copyBoard(board)
		new_board[r][c] = player
		score, _ = maximizer(new_board, swapPlayer(player), depth + 1, alpha, beta)
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
	if checkVictory(board) != "ongoing":
		return getScore(board, player, depth), None
	
	all_moves = getMoves(board)

	best_score = -float("inf")
	best_move = None


	for move in all_moves:
		new_board = copyBoard(board)
		r, c = move
		new_board[r][c] = player
		score, _ = minimizer(new_board, swapPlayer(player), depth + 1, alpha, beta)
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



