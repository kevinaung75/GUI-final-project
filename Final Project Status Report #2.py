"""
Author: Aung Zin Paing
This is a TicTacToe Gui tkinter app
"""
from tkinter import *
from tkinter import messagebox

# Game logic module
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    #checks moves made
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    #checks winner
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]

        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]

        # Check for tie
        if ' ' not in self.board:
            return 'Tie'

        return None