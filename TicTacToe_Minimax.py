# -----------------------------------------------------------------------------
# Name:       Assignment 9: Tic Tac Toe
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:     Ian Cramer
# -----------------------------------------------------------------------------



'''
A game of Tic Tac Toe against the computer. Imports tkinter and random.
'''



import tkinter
import random



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
	return minimax_score(new_game, game.turn, -score)



class GUI:
	tile_size = 150

	def __init__(self, parent, game):
		self.game = game

		parent.title('Tic Tac Toe')
		self.parent = parent

		# Create the restart button widget
		restart_btn = tkinter.Button(self.parent, text='Restart', width=20, command=self.restart)
		restart_btn.grid()

		# Create a canvas widget
		# Create a label widget for the win/lose message
		self.draw_board()

	def restart(self):
		"""
		Handles game restart and reconstruction.
		"""
		self.game = TicTacToe()
		self.win_lose_label.destroy()
		self.canvas.destroy()
		self.draw_board()

	def on_click(self, event):
		if self.game_over():
			return

		click = self.canvas.find_closest(event.x, event.y)
		
		if self.game.valid_play(click[0]-1):
			self.game.play(click[0]-1)
			self.configure_board()
			self.game.computer_play()
		self.configure_board()

	def draw_board(self):
		"""
		Draw a blank tic tac toe board
		"""
		self.canvas = tkinter.Canvas(self.parent, width=self.tile_size * 3, height=self.tile_size * 3)
		self.canvas.grid()
		self.canvas.bind('<Button-1>', self.on_click)

		self.display = []
		for row in range(3):
			for column in range(3):
				id = self.canvas.create_rectangle(self.tile_size * column, self.tile_size * row, self.tile_size * (column + 1), self.tile_size * (row + 1), fill='white')
				self.display.append(id)

		self.win_lose_label = tkinter.Label(self.parent, text='', width=20)
		self.win_lose_label.grid()

	def configure_board(self):
		for i,x in enumerate(self.display):
			if self.game.board[i] == 'X':
				self.canvas.itemconfig(x, fill='red')
			elif self.game.board[i] == 'O':
				self.canvas.itemconfig(x, fill='blue')
			else:
				self.canvas.itemconfig(x, fill='white')
		self.game_over()

	def game_over(self):
		if self.game.game_over():
			self.winner = self.game.winner
			if self.winner == 'X':
				self.win_lose_label.config(text='X/Red wins!')
			elif self.winner == 'O':
				self.win_lose_label.config(text='O/Blue wins!')
			else:
				self.win_lose_label.config(text="It's a tie!")
			return True
		return False




if __name__ == '__main__':
	# Instantiate a root window
	root = tkinter.Tk()

	# Instantiate a Game object
	gen_game = GUI(root, TicTacToe())

	# Enter the main event loop
	root.mainloop()


