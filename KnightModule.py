#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/26/2016


"""
Knight moves:

"""




class Knight:

    def __init__(self, row, col, player_num):
        self.row = row
        self.col = col
        self.symbol = 'N'
        self.player_num = player_num


    def get_position(self):
        return (self.row, self.col)

    def get_symbol(self):
        return self.symbol

    def get_nuber(self):
        return self.player_num

    def move(self, to_row, to_col):
        self.row = to_row
        self.col = to_col


    def is_valid(self, piece_positions, from_row, from_col, to_row, to_col):
        piece, num = piece_positions.get_piece(to_row, to_col)
        if(num == self.player_num):
            return False

        if((from_col - 2 == to_col) or (from_col + 2 == to_col)):
            if((from_row - 1 == to_row) or (from_row + 1 == to_row)):
                return True

        elif((from_col - 1 == to_col) or (from_col + 1 == to_col)):
            if((from_row - 2 == to_row) or (from_row + 2 ==  to_row)):
                return True
        else:
            return False
    
