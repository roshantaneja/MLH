from mancala import *

def badEvaluationFunction(p1side, p2side, player):
	'''
	This is not a great evaluation function. This function
	returns the differences in the number of stones in each
	Mancala between the player and the opponent.
	'''
	if player == 1:
		return p1side[-1]-p2side[-1]
	else:
		return p2side[-1] - p1side[-1]

def evaluationFunction(p1side, p2side, player):
	'''
	Write a better evaluation function here. You should 
	have a few! The one above is an example of a pretty bad 
	evaluation function - yours should definitely be better!
	'''
	if player == 1:
		my_side = p1side
		other_side = p2side
	else:
		my_side = p2side
		other_side = p1side
	
	# scale stones closer to the end of the board higher
	# and scale stones in the Mancala higher
	
	score = 0
	for i in range(6):
		score += my_side[i]*(i)
		score -= other_side[i]*(i)
	score += my_side[6]*10
	score -= other_side[6]*10

	return score

def instantMovePlayer(p1side, p2side, player):
	'''
	The instantMovePlayer does not look ahead at all, just
	evaluates the possible moves it can make and chooses the 
	one that the evaluation function says will be the best.
	'''
	bestMove = 0
	bestMoveScore = -float('inf')
	for move in getAllPossibleMoves(p1side, p2side, player):
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)

		score = badEvaluationFunction(p1sideNext, p2sideNext, player)
		if score > bestMoveScore:
			bestMoveScore = score
			bestMove = move
	return bestMove

def minimaxPlayer(p1side, p2side, player):
	'''
	Make the best move possible using depth-limited
	'''
	maxDepth = 5 # adjust this as needed!
	
	alpha = -float('inf')
	beta = float('inf')
	_, bestMove = maximizer(p1side, p2side, player, maxDepth, alpha, beta)

	return bestMove


def minimizer(p1side, p2side, player, depth, alpha, beta):

	if isVictory(p1side, p2side) != "ongoing" or depth == 0:
		return badEvaluationFunction(p1side, p2side, player), None
	
	all_moves = getAllPossibleMoves(p1side, p2side, player)
	
	best_score = float('inf')
	best_move = None

	for move in all_moves:
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)

		score, _ = maximizer(p1sideNext, p2sideNext, swapPlayer(player), depth-1, alpha, beta)

		if score < best_score:
			best_score = score
			best_move = move
		if score < beta:
			beta = score
		if beta <= alpha:
			break
	
	return best_score, best_move

def maximizer(p1side, p2side, player, depth, alpha, beta):

	if isVictory(p1side, p2side) != "ongoing" or depth == 0:
		return badEvaluationFunction(p1side, p2side, player), None
	
	all_moves = getAllPossibleMoves(p1side, p2side, player)
	
	best_score = -float('inf')
	best_move = None

	for move in all_moves:
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)

		score, _ = minimizer(p1sideNext, p2sideNext, swapPlayer(player), depth-1, alpha, beta)

		if score > best_score:
			best_score = score
			best_move = move
		if score > alpha:
			alpha = score
		if beta <= alpha:
			break
	
	return best_score, best_move

def myCustomPlayer(p1side, p2side, player):
	pass