import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter
    
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.name = input(f"Enter name for player with marker '{self.letter}': ")

    # to get the value of next position from the player
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.name}\'s ({self.letter}) turn. Input move (0-8): ")
            print('')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try Again.')
        
        return val

