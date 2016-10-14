#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/26/2016

from RookModule   import Rook
from BishopModule import Bishop


"""
Queen moves:

"""


class Queen(Rook, Bishop):
    def __init__(self, row, col, player_num):
        Rook.__init__(self, row, col, player_num)
        self.symbol = 'Q'

    def is_valid(self, piece_positions, from_row, from_col, to_row, to_col):
        if(Rook.is_valid(self, piece_positions, from_row, from_col, to_row, to_col)):
            is_valid_rook_move = 1
        else:
            is_valid_rook_move = 0

        if(Bishop.is_valid(self, piece_positions, from_row, from_col, to_row, to_col)):
            is_valid_bishop_move = 1
        else:
            is_valid_bishop_move = 0


        if(is_valid_rook_move or is_valid_bishop_move):
            return True
        else:
            return False
