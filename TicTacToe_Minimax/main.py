import tkinter
from TicTacToe import TicTacToe
from GUI import GUI



def main():
	# Instantiate a root window
	root = tkinter.Tk()

	# Instantiate a Game object
	gen_game = GUI(root, TicTacToe())

	# Enter the main event loop
	root.mainloop()



if __name__ == '__main__':
	main()