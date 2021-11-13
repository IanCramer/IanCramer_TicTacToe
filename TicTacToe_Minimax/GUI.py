import tkinter
from TicTacToe import TicTacToe


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