




def minimax(game):
	scores = []
	for space in game.open_spaces:
		new_game = game.copy().play(space)
		score = minimax_score(new_game, game.turn, 1)
		scores.append(score)

	i = scores.index(max(scores))
	return game.open_spaces[i]


def minimax_score(game, player, score):
	if game.game_over():
		if game.winner == player:
			return score
		else:
			return 0
	# Opponent will choose their best move
	opp_move = minimax(game)
	new_game = game.copy().play(opp_move)
	return minimax_score(new_game, game.turn, -score/2.)