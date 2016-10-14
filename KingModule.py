#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/26/2016


"""
King moves:
"""


class King:

    def __init__(self, row, col, player_num):
        self.row = row
        self.col = col
        self.first_move = 1
        self.symbol = 'K'
        self.player_num = player_num


    def get_position(self):
        return (self.row, self.col)

    def update_first_move(self):
        self.first_move = 0

    def get_symbol(self):
        return self.symbol

    def is_first_move(self):
        return self.first_move

    def move(self, to_row, to_col):
        self.row = to_row
        self.col = to_col
        if(self.first_move):
            self.update_first_move()


    def is_valid(self, piece_positions, from_row, from_col, to_row, to_col):
        if(from_row == to_row):
            if(from_col + 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            elif(from_col - 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False

                
            elif(from_col - 2 == to_col and self.first_move):                                               #Checks for castling 
                piece_a, num_a = piece_positions.get_piece(to_row, from_col - 1)
                piece_b, num_b = piece_positions.get_piece(to_row, from_col - 2)
                piece_c, num_c = piece_positions.get_piece(to_row, from_col - 3)
                if(piece_a != '-' or piece_b != '-' or piece_c != 'R' or num_c != self.player_num):
                    print num_c
                    print self.player_num
                    return False
                else:
                    return True

            elif(from_col + 2 == to_col and self.first_move):                                               #Checks for castling 
                piece_a, num_a = piece_positions.get_piece(to_row, from_col + 1)
                piece_b, num_b = piece_positions.get_piece(to_row, from_col + 2)
                piece_c, num_c = piece_positions.get_piece(to_row, from_col + 3)
                piece_d, num_d = piece_positions.get_piece(to_row, from_col + 4)
                if(piece_a != '-' or piece_b != '-' or piece_c != '-' or piece_d != 'R' or num_d != self.player_num):
                    return False
                else:
                    return True
                
            else:
                return False

        elif(from_row + 1 == to_row):
            if(from_col + 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            elif(from_col - 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            elif(from_col  == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            else:
                return False
        elif(from_row - 1 == to_row):
            if(from_col + 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            elif(from_col - 1 == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            elif(from_col  == to_col):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(num != self.player_num):
                    return True
                else:
                    return False
            else:
                return False
        
