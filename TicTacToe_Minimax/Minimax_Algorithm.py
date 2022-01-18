



def minimax(game):
	scores = []
	# For each possible move, score the move
	for space in game.open_spaces:
		new_game = game.copy().play(space)
		score = minimax_score(new_game, game.turn, 1)
		scores.append(score)

	# This player is the maximizer, return move with maximum score
	i = scores.index(max(scores))
	return game.open_spaces[i]





def minimax_score(game, player, score):
	# If the game is over, give it a score
	if game.game_over():
		if game.winner == player:
			return score
		return 0

	# If it is not over:
	# Assume opponent will choose best possible move
	opp_move = minimax(game)
	new_game = game.copy().play(opp_move)

	# Return game score
	# Initial Player is maximizer, since the player switches on each recursion to determine that player's best move, change sign of score accordingly
	# Reduce score by half to prioritize earlier vicotries
	return minimax_score(new_game, game.turn, -score/2.)



