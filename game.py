import time
import random
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for num in range(9)] # to store values of different positions
        self.current_winner = None 

    # function to print board after every player's move
    def print_board(self):
        print("Current Game            Position Numbers")
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        current_board = [self.board[i*3:(i+1)*3] for i in range(3)]
        for row in range(3):
            print('| '+' | '.join(current_board[row])+ ' |            '+'| '+' | '.join(number_board[row]) + ' |')
        
        print('')
        print('--------------------------------------')

    # function to print board showing positions at the beginning of the game 
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row) + ' |')
        print('')

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']

    # to check for empty positions on the board
    def empty_squares(self):
        return ' ' in self.board # returns true if empty spaces are left on the board

    # def num_empty_squares(self):
    #     return self.board.count(' ')

    def make_move(self, square, letter):

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # check if someone has won
    def winner(self, square, letter):
        
        # checking for all values in a row to be similar
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True 

        # checking for all values in a column to be similar
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # checking for diagonal values to be similar
        if square % 2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game = True):
    if print_game:
        print('\nWelcome to TIC-TAC-TOE!!!!\n')
        game.print_board_nums()

    letter = random.choice(('O', 'X')) # Randomly choose which player goes first

    while game.empty_squares():
        
        if letter == 'O':
            square = o_player.get_move(game)
            letter = o_player.letter
            try:
                name = o_player.name
            except:
                name = 'Computer'
        else:
            square = x_player.get_move(game)
            letter = x_player.letter
            try:
                name = x_player.name
            except:
                name = 'Computer'  

        if game.make_move(square, letter):
            if print_game:
                print(f'{name} ('+letter + f') makes a move to square {square}\n')
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(f"{name}({letter}) wins!!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(2) # to add 2 sec delay after each move

    if print_game:
        print(" It\'s a Tie!!!")


if __name__ == '__main__': 
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    # o_player = RandomComputerPlayer('O') # Uncomment to play with the computer
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)
