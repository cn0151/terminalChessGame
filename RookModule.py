#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/24/2016 


"""
    Rook Moves:
"""


class Rook:
    def __init__(self, row, col, player_num):
        self.row = row
        self.col = col
        self.first_move = 1
        self.symbol = 'R'
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
        if((from_row == to_row) and  (from_col != to_col)):
            is_row_move = 0               # 1 if move is by row else 0 if move is by column
            lesser_to_move = 0            # 1 if to_row or to_col is less than from _row or from_col
            if(from_col < to_col):
                start_index = from_col + 1
                stop_index = to_col
                

            elif(from_col > to_col):
               piece, num =  piece_positions.get_piece(to_row, to_col)
               if(self.player_num != num):
                   start_index = to_col + 1
                   stop_index = from_col
                   lesser_to_move = 1
               else:
                   return False

            else:
                return False

        elif((from_row != to_row) and (from_col == to_col)):
            is_row_move = 1               # 1 if move is by row else 0 if move is by column
            lesser_to_move = 0            # 1 if to_row or to_col is less than from _row or from_col
            if(from_row < to_row):
                start_index = from_row + 1
                stop_index = to_row

            elif(from_row > to_row):
                piece, num = piece_positions.get_piece(to_row, to_col)
                if(self.player_num != num):
                    start_index = to_row + 1
                    stop_index = from_row
                    lesser_to_move = 1
                else:
                    return False

            else:
                return False

        else:
            return False


    
        #piece, num = None, None             #Used so that variables dont go out of scope after while loop below  
        
        while(start_index <= stop_index):
            if(is_row_move):
                piece, num = piece_positions.get_piece(start_index, from_col)
            else:
                piece, num = piece_positions.get_piece(from_row, start_index)
                
            if(num != '-'):
                break
            start_index += 1

        if(start_index < stop_index):
            return False

        if(lesser_to_move):
            if(num == self.player_num):
                return True
            else:
                return False

        else:
            if(num != self.player_num):
                return True
            else:
                return False
            

        
        
                
            
                
                
                    
                   





                
                
            
            
