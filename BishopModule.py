#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/26/2016


"""
Bishop moves:

"""


class Bishop:
    def __init__(self, row, col, player_num):
        self.row = row
        self.col = col
        self.symbol = 'B'
        self.player_num = player_num


    def get_position(self):
        return (self.row, self.col)

    def get_symbol(self):
        return self.symbol

    def get_number(self):
        return self.player_num


    def move(self, to_row, to_col):
        self.row = to_row
        self.col = to_col


    def is_valid(self, piece_positions, from_row, from_col, to_row, to_col):
        if((from_row == to_row) or (from_col == to_col)):
            return False
        
        if(from_row < to_row):
            start_row_index = from_row + 1
            stop_row_index = to_row
            start_col_index = from_col
            stop_col_index = to_col
            is_from_row = 1
        else:
            piece, num = piece_positions.get_piece(to_row, to_col)
            if(num != self.player_num):
                start_row_index = to_row + 1
                stop_row_index = from_row
                start_col_index = to_col
                stop_col_index = from_col
                is_from_row = 0
            else:
                return False

        if(start_col_index < stop_col_index):
            col_increment = 1
        else:
            col_increment = -1

        start_col_index += col_increment
        

        break_reached = 0

        
        while(start_row_index <= stop_row_index):
            piece, num = piece_positions.get_piece(start_row_index, start_col_index)
            if(num != '-' or start_col_index == stop_col_index):
                break_reached = 1
                break
            start_row_index += 1
            start_col_index += col_increment

        
        if(not break_reached):
            start_row_index -= 1
            start_col_index += (-col_increment)
            
        if(start_row_index != stop_row_index):
            return False


        if(start_col_index != stop_col_index):
            return False
        
        else:
            if(num == '-'):
                return True

            if(is_from_row):
                if(num != self.player_num):
                    return True
                else:
                    return False

            else:
                if(num == self.player_num):
                    return True
                else:
                    return False



        

            

            
            
        

    
