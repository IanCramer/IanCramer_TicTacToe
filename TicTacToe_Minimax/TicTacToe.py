


from Minimax_Algorithm import minimax



class TicTacToe(object):

	def __init__(self):
		self.winner = ''
		self.over = False
		self.turn = 'X'
		self.make_board()

	def make_board(self):
		self.board = ['','','','','','','','','']
		self.open_spaces = [0,1,2,3,4,5,6,7,8]

	def run(self):
		while not self.game_over():
			print(self)
			x = input("Choose Place: ")
			try:
				x = int(x)
			except:
				print("Invalid. Please Choose")
				print(self.open_spaces)
				continue

			if x in self.open_spaces:
				self.play(x)
			else:
				print("Invalid. Please Choose")
				print(self.open_spaces)
				continue

			if self.game_over():
				break

			self.computer_play()

		print(self)

	def play(self, x):
		if self.move(x) and not self.game_over():
			self.switch_turn()
		return self

	def computer_play(self):
		if self.game_over():
			return False
		best_space = minimax(self)
		if self.move(best_space):
			self.switch_turn()
			return best_space
		return False

	def move(self, x):
		if self.valid_play(x):
			self.board[x] = self.turn
			self.open_spaces.remove(x)
			return True
		return False

	def valid_play(self, x):
		if self.game_over():
			return False
		if self.board[x]:
			return False
		return True


	def other_player(self, player):
		if player == 'X':
			return 'O'
		if player == 'O':
			return 'X'

	def switch_turn(self):
		self.turn = self.other_player(self.turn)
		return self

	def game_over(self):
		# Check rows and cols
		for i in range(3):
			if self.board[3*i] == self.board[3*i+1] and self.board[3*i] == self.board[3*i+2]:
				if self.board[3*i]:
					self.winner = self.board[3*i]
			if self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6]:
				if self.board[i]:
					self.winner = self.board[i]
		# Check Diagonals
		if (self.board[0] == self.board[4] and self.board[4] == self.board[8]) or (self.board[2] == self.board[4] and self.board[4] == self.board[6]):
			if self.board[4]:
				self.winner = self.board[4]

		if self.winner:
			self.over = True
		if len(self.open_spaces) == 0:
			self.over = True

		return self.over



	def __str__(self):
		self_str = f"Current Player: {self.turn}"
		self_str += "\n-------------\n"
		for i,r in enumerate(self.board):
			self_str += "| "
			if r:
				self_str += f'{r} '
			else:
				self_str += "  "
			if not (i+1)%3:
				self_str += "|\n-------------\n"
		return self_str

	def __repr__(self):
		return str(game)

	def copy(self):
		new_game = TicTacToe()
		new_game.turn = self.turn
		new_game.winner = self.winner
		new_game.over = self.over
		for i,x in enumerate(self.board):
			new_game.board[i] = x
		new_game.open_spaces = []
		for i,x in enumerate(self.open_spaces):
			new_game.open_spaces.append(x)

		return new_game