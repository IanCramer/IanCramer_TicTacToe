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



class Game(object):
	'''
	Tic Tac Toe Game Class. Inherits from object.
	'''
	# Add your class variables if needed here - square size, etc...)
	tile_size = 150
	blank_color = 'white'
	player_color = 'blue'
	computer_color = 'red'


	def __init__(self, parent):
		'''
		Constructor takes the tkinter parent structure. Creates and starts the game.
		'''
		parent.title('Tic Tac Toe')
		self.parent = parent

		# Create the restart button widget
		restart_btn = tkinter.Button(self.parent, text='Restart', width=20, command=self.restart)
		restart_btn.grid()

		# Create a canvas widget
		# Create a label widget for the win/lose message
		self.draw_board()

		# Create any additional instance variable you need for the game
		self.game_over = False
		


	def restart(self):
		"""
		Handles game restart and reconstruction.
		"""
		self.game_over = False
		self.win_lose_label.destroy()
		self.canvas.destroy()
		self.draw_board()



	def play(self, event):
		"""
		Facilitates playing the game. Takes an event and changes the gui accordingly.
		"""
		if self.game_over != True:

			clicked_square = self.canvas.find_closest(event.x, event.y)
			if self.canvas.itemcget(clicked_square, 'fill') == Game.blank_color:
				self.canvas.itemconfig(clicked_square, fill=Game.player_color)
				self.players_moves.append(clicked_square)
				self.open_spaces.remove(clicked_square)

				if not self.check_game_over():
					self.computer_play()


	def computer_play(self):
		"""
		The computer play function. Determines where the computer will move.
		"""
		if self.game_over != True:
			square = self.choose_place()
			# print(square)
			self.canvas.itemconfig(square, fill=Game.computer_color)
			self.computer_moves.append(square)
			self.open_spaces.remove(square)
			self.check_game_over()
      
      
	def choose_place(self):
   		center_square = (5,)
   		if self.canvas.itemcget(center_square, 'fill') == Game.blank_color:
   			return center_square

   		if len(self.players_moves) == 1:
   			return (1,)

   		if self.players_moves == [ (5,), (9,) ]:
   			return(3,)

   		game_state = []
   		i = 1
   		for row in range(9):
   			if self.canvas.itemcget((i,), 'fill') == Game.blank_color:
   				game_state.append(0)
   			elif self.canvas.itemcget((i,), 'fill') == Game.player_color:
   				game_state.append(1)
   			elif self.canvas.itemcget((i,), 'fill') == Game.computer_color:
   				game_state.append(10)
   			i += 1

   		# Check Rows
   		for i in range(3):
   			row = [ game_state[3*i], game_state[3*i+1], game_state[3*i+2] ]
   			# First Defend
   			if sum(row) == 2:
   				for j in range(3):
   					if row[j] == 0:
   						return (3*i+j+1,)
   			# Then Attack
   			elif sum(row) == 20:
   				for j in range(3):
   					if row[j] == 0:
   						return (3*i+j+1,)
   		# Check Columns
   		for i in range(3):
   			col = [ game_state[i], game_state[i+3], game_state[i+6] ]
   			# First Defend
   			if sum(col) == 2:
   				for j in range(3):
   					if col[j] == 0:
   						return (3*j+i+1,)
   			# Then Attack
   			elif sum(col) == 20:
   				for j in range(3):
   					if col[j] == 0:
   						return (3*j+i+1,)
   		# Check Diagonals
   		#First Defend
   		if game_state[2] + game_state[4] + game_state[6] == 2:
   			if game_state[2] == 0:
   				return (3,)
   			else:
   				return (7,)
   		# Then Attack
   		if game_state[0] + game_state[4] + game_state[8] == 20:
   			if game_state[0] == 0:
   				return (1,)
   			else:
   				return (9,)
   		if game_state[2] + game_state[4] + game_state[6] == 20:
   			if game_state[2] == 0:
   				return (3,)
   			else:
   				return (7,)
   		# Nowhere Urgent, Go on offensive
   		for i in range(0,8,2):
   			if game_state[i] == 0:
   				return (i+1,)



	def draw_board(self):
		"""
		Draw a blank tic tac toe board
		"""
		self.canvas = tkinter.Canvas(self.parent, width=self.tile_size * 3, height=self.tile_size * 3)
		self.canvas.grid()
		self.canvas.bind('<Button-1>', self.play)

		self.board = []
		for row in range(3):
			for column in range(3):
				id = self.canvas.create_rectangle(self.tile_size * column, self.tile_size * row, self.tile_size * (column + 1), self.tile_size * (row + 1), fill=Game.blank_color)
				self.board.append(id)

		self.win_lose_label = tkinter.Label(self.parent, text='', width=20)
		self.win_lose_label.grid()
		self.players_moves = []
		self.computer_moves = []
		self.open_spaces = [ (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,) ]



	def check_game_over(self):
		"""
		Checks the state of the game and determines if/who the winner is.
		"""
		self.game_over = False
		self.winner = Game.blank_color

		square_vals = []
		for square in self.board:
			square_vals.append(self.canvas.itemcget(square, 'fill'))

		# Checks the rows
		for i in range(3):
			if square_vals[3*i] == square_vals[3*i+1] and square_vals[3*i] == square_vals[3*i+2]: 
				self.winner = square_vals[3*i]
		# Checks the columns
		for i in range(3):
			if square_vals[i] == square_vals[i+3] and square_vals[i] == square_vals[i+6]:
				self.winner = square_vals[i]
		# Checks the diagonals
		if square_vals[0] == square_vals[4] and square_vals[4] == square_vals[8]:
			self.winner = square_vals[4]
		if square_vals[2] == square_vals[4] and square_vals[4] == square_vals[6]:
			self.winner = square_vals[4]

		if self.winner == Game.player_color:
			self.win_lose_label.config(text='You won!')
			self.game_over = True
		elif self.winner == Game.computer_color:
			self.win_lose_label.config(text='You lost!')
			self.game_over = True
		elif not Game.blank_color in square_vals:
			self.win_lose_label.config(text="It's a tie!")
			self.game_over = True
		return self.game_over



def main():
	# Instantiate a root window
	root = tkinter.Tk()

	# Instantiate a Game object
	gen_game = Game(root)

	# Enter the main event loop
	root.mainloop()



if __name__ == '__main__':
	main()