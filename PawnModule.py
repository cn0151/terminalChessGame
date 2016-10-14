#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/13/2016

"""
Pawn moves:
    * Can only move 2 squares forward at first move
    * After first move, can only move 1 square forward
    * Can be promoted to higher piece (queen, knight, rook or bishop) if it reaches its eighth rank (row)
"""


class Pawn:
    
    def __init__(self, row, col, player_num):
        self.row = row
        self.col = col
        self.first_move = 1
        self.num_moves  = 0         #will be used for epsilon move in future
        self.symbol = 'P'
        self.player_num = player_num

    def get_position(self):
        return (self.row,self.col)

    def update_first_move(self):
        self.first_move = 0

    def can_promote(self):
        if(self.player_num == 1 and self.row == 8):
            return True
        elif(self.player_num == 2 and self.row == 1):
            return True
        else:
            return False

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.player_num

    def move(self, to_row, to_col):
        self.row = to_row
        self.col = to_col
        self.num_moves += 1
        if(self.first_move):
            self.update_first_move()
        

    def is_valid(self, piece_positions,from_row, from_col, to_row, to_col):
        if(self.player_num == 2):
            if(from_col == to_col):
                if(from_row + 1 == to_row):
                    chess_piece, piece_num = piece_positions.get_piece(to_row, to_col)
                    if(piece_num == '-'):
                        return True
                    else:
                        return False

                elif(from_row + 2 == to_row and self.first_move == 1):
                    chess_piece_a, piece_num_a = piece_positions.get_piece(from_row + 1, from_col)
                    chess_piece_b, piece_num_b = piece_positions.get_piece(from_row + 2, from_col)
                    if(piece_num_a == '-' and piece_num_b == '-'):
                        return True
                    else:
                        return False
                else:
                    return False

            elif(from_row + 1 == to_row):
                chess_piece, piece_num = piece_positions.get_piece(to_row, to_col)
                if((from_col + 1 == to_col) or (from_col - 1 == to_col)):
                    if(piece_num == 1):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False



        elif(self.player_num == 1):
            if(from_col == to_col):
                if(from_row - 1 == to_row):
                    chess_piece, piece_num = piece_positions.get_piece(to_row, to_col)
                    if(piece_num == '-'):
                        return True
                    else:
                        return False

                elif(from_row - 2 == to_row and self.first_move == 1):
                    chess_piece_a, piece_num_a = piece_positions.get_piece(from_row - 1, from_col)
                    chess_piece_b, piece_num_b = piece_positions.get_piece(from_row - 2, from_col)
                    if(piece_num_a == '-' and piece_num_b == '-'):
                        return True
                    else:
                        return False
                else:
                    return False

            elif(from_row - 1 == to_row):
                chess_piece, piece_num = piece_positions.get_piece(to_row, to_col)
                if((from_col + 1 == to_col) or (from_col - 1 == to_col)):
                    if(piece_num == 2):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
           
    
