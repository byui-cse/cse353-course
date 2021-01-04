"""
Course: CS312
File: teach2.py
Description:
   Tic-Tac-Toe

   You are NOT submitting this program.
"""

"""
Instructions:

1) complete the functions below. (No global variables allowed)

2) Using these functions, compute the max number of Tic-Tac-Toe games possible.
   You can create any functions that you need.

There are two Tic-Tac-Toe files to use in your program.  Use these files for testing.

good.txt -> a good board
bad.txt -> a bad board

"""

import numpy as np


def get_file_load():
    """ Ask user for a filename to load """
    pass


def get_file_save():
    """ Ask user for a filename to save to """
    pass


def load_board(filename):
    """ Load the board from the file """
    pass


def save_board(filename, board):
    """ Save the board to a file """
    pass


def display_board(board):
    """ 
    Display a board.

    This is the format:

     X |   | O
    ---+---+--- 
     O | X |   
    ---+---+--- 
     X | O | X 
    """
    pass


def valid_board(board):
    """ Is the board valid """
    pass


def game_won(board):
    """ Did someone win the game """
    pass


def count_possible_games():
    """ Extra: How many possible games can be played 
        Use loops to find this out.
    """
    pass


def main():
    """ Main function """
    filename = get_file_load()
    board = load_board(filename)

    display_board(board)

    if (valid_board(board)):
        print('board is valid')
    else:
        print('board is not valid')

    if (game_won(board)):
        print('Game has been won')
    else:
        print('Game is not finished')

    filename = get_file_save()
    save_board(filename, board)

    # Extra
    # count = count_possible_games()
    # print(f'Max possible games that can be played = {count}')

    # Extra Extra
    # Change the program to handle any size board (ie., N x M)
    # and see what count_possible_games() returns for board sizes of
    # 5 x 5
    # 5 x 8



if __name__ == "__main__":
    # execute only if run as a script
    main()
