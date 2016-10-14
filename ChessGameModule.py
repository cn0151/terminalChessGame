#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/13/2016

from PiecePositionModule import PiecePositions
from PawnModule import Pawn
from RookModule import Rook
from KnightModule import Knight
from BishopModule import Bishop
from QueenModule import Queen
from KingModule import King


class ChessGame:
    QUEEN  =  1
    BISHOP =  2
    KNIGHT =  3
    ROOK   =  4
    
    chess_board =   [['R2','N2','B2','K2','Q2','B2','N2','R2'],
                     ['P2','P2','P2','P2','P2','P2','P2','P2'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['P1','P1','P1','P1','P1','P1','P1','P1'],
                     ['R1','N1','B1','K1','Q1','B1','N1','R1']]

    ROWS = 7
    COLS = 7
    
    king_1_on_check = False
    king_2_on_check = False
    
    piece_positions = PiecePositions()
    is_from_file = False
    
    def __init__(self):
        player_row_a = 0           #for player 2
        player_row_b = 7           #for player 1

        
        player_1 = 1
        player_2 = 2

        #--------------------------------------------------------------------------------------

        #Creates pawn objects for both player 1 and player 2
        col = 0
        while(col <= self.COLS):
            self.chess_board[player_row_a + 1][col] = Pawn(player_row_a + 1, col, player_2)
            self.chess_board[player_row_b - 1][col] = Pawn(player_row_b - 1, col, player_1)
            col += 1

        #-------------------------------------------------------------------------------------
        
        #creates rook objects for player 2
        self.rook_2a = self.chess_board[player_row_a][0] = Rook(player_row_a, 0, player_2)
        self.rook_2b = self.chess_board[player_row_a][7] = Rook(player_row_a, 7, player_2)

        #creates rook objects for player 1
        self.rook_1a = self.chess_board[player_row_b][0] = Rook(player_row_b, 0, player_1)
        self.rook_1b = self.chess_board[player_row_b][7] = Rook(player_row_b, 7, player_1)

        #--------------------------------------------------------------------------------------
        
        #creates knight objects for player 2
        self.knight_2a = self.chess_board[player_row_a][1] = Knight(player_row_a, 1, player_2)
        self.knight_2b = self.chess_board[player_row_a][6] = Knight(player_row_a, 6, player_2)

        #creates knight objects for player 1
        self.knight_1a = self.chess_board[player_row_b][1] = Knight(player_row_b, 1, player_1)
        self.knight_1b = self.chess_board[player_row_b][6] = Knight(player_row_b, 6, player_1)

        #--------------------------------------------------------------------------------------

        #creates bishop objects for player 2
        self.bishop_2a = self.chess_board[player_row_a][2] = Bishop(player_row_a, 2, player_2)
        self.bishop_2b = self.chess_board[player_row_a][5] = Bishop(player_row_a, 5, player_2)

        #creates bishop objects for player 1
        self.bishop_1a = self.chess_board[player_row_b][2] = Bishop(player_row_b, 2, player_1)
        self.bishop_1b = self.chess_board[player_row_b][5] = Bishop(player_row_b, 5, player_1)

        #--------------------------------------------------------------------------------------
        
        #creates queen objects for player 1 and player 2
        self.queen_2 = self.chess_board[player_row_a][4] = Queen(player_row_a, 4, player_2)
        self.queen_1 = self.chess_board[player_row_b][4] = Queen(player_row_b, 4, player_1)


        #--------------------------------------------------------------------------------------
        
        #creates king objects for player 1 and player 2
        self.king_2 = self.chess_board[player_row_a][3] = King(player_row_a, 3, player_2)
        self.king_1 = self.chess_board[player_row_b][3] = King(player_row_b, 3, player_1)
        
    def moves_from_file(self, from_file):
        self.is_from_file = from_file

    def modify_rook_pos(self, row, col, is_from_col, player_num):
        player_row_a = 0           #for player 2
        player_row_b = 7           #for player 1
        if(is_from_col):
            if(player_num == 1):
                self.chess_board[player_row_b][col - 1] = self.rook_1b
                self.chess_board[player_row_b][7] = "--"
                self.piece_positions.update_board(player_row_b, 7, player_row_b, col - 1)
            else:
                self.chess_board[player_row_a][col - 1] = self.rook_2b
                self.chess_board[player_row_a][7] = "--"
                self.piece_positions.update_board(player_row_a, 7, player_row_a, col - 1)

        else:
            if(player_num == 1):
                self.chess_board[player_row_b][col + 1] = self.rook_1a
                self.chess_board[player_row_b][0] = "--"
                self.piece_positions.update_board(player_row_b, 0, player_row_b, col + 1)
            else:
                self.chess_board[player_row_a][col + 1] = self.rook_2a
                self.chess_board[player_row_a][0] = "--"
                self.piece_positions.update_board(player_row_a, 0, player_row_a, col + 1)
            

    def castle(self,from_row, from_col, to_row, to_col, player_num, piece_obj):
        if(from_col < to_col):
            is_from_col = True
            if(self.king_on_check(from_row, from_col, to_row, from_col + 1, True, player_num)):      ## checks if a move will put the player's king on check
                print "Error: King will be on check"
                print ".......Invalid castling move"
                return False

        elif(from_col > to_col):
            is_from_col = False
            if(self.king_on_check(from_row, from_col, to_row, from_col - 1, True, player_num)):      ## checks if a move will put the player's king on check
                print "Error: King will be on check"
                print ".......Invalid castling move"
                return False

        valid =  self.on_check(from_row, from_col, to_row, to_col, player_num, piece_obj)
        if(not valid):
            print ".......Invalid castling move"
            return valid

        else:
            self.modify_rook_pos(to_row, to_col, is_from_col, player_num)
            return valid
                

        
        

    def on_check(self, from_row, from_col, to_row, to_col, player_num, piece_obj):
        if(player_num == 1):
            opponent_num = 2
        else:
            opponent_num = 1


        ### the below if elif statements checks if a move will put the player's king on check
        ### and if the opponenets king will on check after the move

        

                 
        
        if(self.king_on_check(from_row, from_col, to_row, to_col, True, player_num)):      ## checks if a move will put the player's king on check
            print "Error: King will be on check"
            return False

        self.move_piece(piece_obj, from_row, from_col, to_row, to_col, player_num)
        if(self.king_on_check(from_row, from_col, to_row, to_col, False, opponent_num)): ##checks if the opponent's king is on check
            if(opponent_num == 1):
                self.king_1_on_check = True
            else:
                self.king_2_on_check = True
        return True





    def king_on_check(self, from_row, from_col, to_row, to_col, piece_moved, player_num):
        if(piece_moved):
            from_pos_piece, from_pos_num = self.piece_positions.get_piece(from_row, from_col)
            to_pos_piece, to_pos_num     = self.piece_positions.get_piece(to_row, to_col)
            
            from_piece_obj = self.get_piece_obj(from_row, from_col)
            to_piece_obj = self.get_piece_obj(to_row, to_col)
            
            self.piece_positions.update_board(from_row, from_col, to_row, to_col)
            self.move_piece(from_piece_obj, from_row, from_col, to_row, to_col, player_num)

        
        if(player_num == 1):
            not_valid = False
            king_row, king_col = self.king_1.get_position()
            rook_2a_row, rook_2a_col = self.rook_2a.get_position()
            rook_2b_row, rook_2b_col = self.rook_2b.get_position()

            if(self.rook_2a.is_valid(self.piece_positions, rook_2a_row, rook_2a_col, king_row, king_col) or
               self.rook_2b.is_valid(self.piece_positions, rook_2b_row, rook_2b_col, king_row, king_col)):
                not_valid = True

            knight_2a_row, knight_2a_col = self.knight_2a.get_position()
            knight_2b_row, knight_2b_col = self.knight_2b.get_position()


            if(self.knight_2a.is_valid(self.piece_positions, knight_2a_row, knight_2a_col, king_row, king_col) or
               self.knight_2b.is_valid(self.piece_positions, knight_2b_row, knight_2b_col, king_row, king_col)):
                not_valid = True

            bishop_2a_row, bishop_2a_col = self.bishop_2a.get_position()
            bishop_2b_row, bishop_2b_col = self.bishop_2b.get_position()

       
            if(self.bishop_2a.is_valid(self.piece_positions, bishop_2a_row, bishop_2a_col, king_row, king_col) or
               self.bishop_2b.is_valid(self.piece_positions, bishop_2b_row, bishop_2b_col, king_row, king_col)):
                not_valid = True

            queen_2_row, queen_2_col = self.queen_2.get_position()

           
            if(self.queen_2.is_valid(self.piece_positions, queen_2_row, queen_2_col, king_row, king_col)):
                not_valid = True

            king_2_row, king_2_col = self.king_2.get_position()

            
            if(self.king_2.is_valid(self.piece_positions, king_2_row, king_2_col, king_row, king_col)):
                not_valid = True            
                

                    
    
        else:
            not_valid = False           #Base assumption
            king_row, king_col = self.king_2.get_position()
    
            rook_1a_row, rook_1a_col = self.rook_1a.get_position()
            rook_1b_row, rook_1b_col = self.rook_1b.get_position()

            
            if(self.rook_1a.is_valid(self.piece_positions, rook_1a_row, rook_1a_col, king_row, king_col) or
               self.rook_1b.is_valid(self.piece_positions, rook_1b_row, rook_1b_col, king_row, king_col)):   
               not_valid = True
        

            knight_1a_row, knight_1a_col = self.knight_1a.get_position()
            knight_1b_row, knight_1b_col = self.knight_1b.get_position()

            
            if(self.knight_1a.is_valid(self.piece_positions, knight_1a_row, knight_1a_col, king_row, king_col) or
               self.knight_1b.is_valid(self.piece_positions, knight_1b_row, knight_1b_col, king_row, king_col)):
                not_valid = True

            bishop_1a_row, bishop_1a_col = self.bishop_1a.get_position()
            bishop_1b_row, bishop_1b_col = self.bishop_1b.get_position()

           
            if(self.bishop_1a.is_valid(self.piece_positions, bishop_1a_row, bishop_1a_col, king_row, king_col) or
               self.bishop_1b.is_valid(self.piece_positions, bishop_1b_row, bishop_1b_col, king_row, king_col)):
               not_valid = True
               

            queen_1_row, queen_1_col = self.queen_1.get_position()
            
            if(self.queen_1.is_valid(self.piece_positions, queen_1_row, queen_1_col, king_row, king_col)):
                not_valid = True

            
            king_1_row, king_1_col = self.king_1.get_position()

            
            if(self.king_1.is_valid(self.piece_positions, king_1_row, king_1_col, king_row, king_col)):
                not_valid = True

 
        ### Checks if pawns will be able to put the king on check and the
        ### below statements checks when king is at the edge of the boards
        ### so that when I check the piece in those positions, it doesn't go
        ### out of range

        
        king_corner_a_set = False
        king_corner_b_set = False
        king_corner_c_set = False
        king_corner_d_set = False
        
            
        if(king_row + 1 <= self.ROWS and king_row + 1 >= 0):
            if(king_col + 1 <= self.COLS and king_col + 1 >= 0):
                king_corner_a = self.get_piece_obj(king_row + 1, king_col + 1)
                if(king_corner_a != '--'):
                    piece, num = king_corner_a.get_symbol(), king_corner_a.get_number()
                    if(piece == 'P' and num != player_num):
                        if(king_corner_a.is_valid(piece_positions, king_row + 1, king_col + 1, king_row, king_col)):
                            king_corner_a_set = True

            if(king_col - 1 <= self.COLS and king_col - 1 >= 0):
                king_corner_b = self.get_piece_obj(king_row + 1, king_col - 1)
                if(king_corner_b != '--'):
                    piece, num = king_corner_b.get_symbol(), king_corner_b.get_number()
                    if(piece == 'P' and num != player_num):
                        if(king_corner_b.is_valid(piece_positions, king_row + 1, king_col - 1, king_row, king_col)):
                            king_corner_b_set = True

        if(king_row - 1 <= self.ROWS and king_row - 1 >= 0):
            if(king_col + 1 <= self.COLS and king_col + 1 >= 0):
                king_corner_c = self.get_piece_obj(king_row - 1, king_col + 1)
                if(king_corner_c != '--'):
                    piece, num = king_corner_c.get_symbol(), king_corner_c.get_number()
                    if(piece == 'P' and num != player_num):
                        if(king_corner_c.is_valid(piece_positions, king_row - 1, king_col + 1, king_row, king_col)):
                            king_corner_c_set = True

            if(king_col - 1 <= self.COLS and king_col - 1 >= 0):
                king_corner_d = self.get_piece_obj(king_row - 1, king_col - 1)
                if(king_corner_d != '--'):
                    piece, num = king_corner_d.get_symbol(), king_corner_d.get_number()
                    if(piece == 'P' and num != player_num):
                        if(king_corner_d.is_valid(piece_positions, king_row - 1, king_col - 1, king_row, king_col)):
                            king_corner_d_set = True


        if(king_corner_a_set or king_corner_b_set or king_corner_c_set or king_corner_d_set):
            not_valid = True
            


        if(piece_moved):
            from_piece = from_pos_piece + str(from_pos_num)
            to_piece   = to_pos_piece + str(to_pos_num)

            self.piece_positions.replace_piece(from_piece, from_row, from_col)
            self.piece_positions.replace_piece(to_piece, to_row, to_col)


            self.modify_piece_pos(from_row, from_col, from_piece_obj)
            self.modify_piece_pos(to_row, to_col, to_piece_obj)


       

        return not_valid
            
                
        

    def pawn_promote_menu(self):
        print "Promote pawn to ..."
        print "1. Queen \t  2. Rook"
        print "3. Knight \t 4. Bishop"
        choice = raw_input("Enter choice: ")
        #######do error checking for choice #######
        return choice
        

    def display_board(self):
        self.piece_positions.display_board()
        if(self.king_1_on_check and not self.is_from_file):
            print "Player 1 King on check"
            self.king_1_on_check = False
        elif(self.king_2_on_check and not self.is_from_file):
            print "Player 2 King on check"
            self.king_2_on_check = False
        

    def get_piece_obj(self, row, col):
        return self.chess_board[row][col]

    def get_row_col(self, pos):
        col = ord((pos[0]).upper()) - ord('A')
        row = 8 - int(pos[1])
        return (row,col)

    def in_range(self, row, col):
        if(row < 0 or row > 7):
            return False
        if(col < 0 or col > 7):
            return False

        return True
    
        
    def serialize_user_input(self, user_input):
        user_input = user_input.strip()
        if(',' in user_input):
            user_input = user_input.replace(',',' ')
        
        user_input = user_input.split()
        return(len(user_input), user_input[0].strip(), user_input[1].strip()) 



            
    def is_valid_user_input(self, player_num, user_input):
        count, from_pos, to_pos = self.serialize_user_input(user_input)
        if(count != 2):
            return False
    
        from_row, from_col = self.get_row_col(from_pos)
        to_row, to_col = self.get_row_col(to_pos)

        if(self.in_range(to_row, to_col)):
            chess_piece, piece_num = self.piece_positions.get_piece(from_row, from_col)
            if(piece_num != player_num):
                return False
            else:
                piece_obj = self.get_piece_obj(from_row, from_col)
                if(piece_obj.is_valid(self.piece_positions, from_row, from_col, to_row, to_col)):
                    #####put castling and check code here
                    if(piece_obj.get_symbol() == 'K' and from_row == to_row and piece_obj.is_first_move() and ((from_col + 2 == to_col) or (from_col - 2 == to_col))):
                        return self.castle(from_row, from_col, to_row, to_col, player_num, piece_obj)
                    else:
                        return self.on_check(from_row, from_col, to_row, to_col, player_num, piece_obj)

            
                else:
                   return False
        else:
            return False

        

    def update_board_obj(self, piece_obj, from_row, from_col, to_row, to_col):
        self.chess_board[to_row][to_col] = piece_obj
        self.chess_board[from_row][from_col] = '--'


    def modify_piece_pos(self, row, col, piece_obj):
        self.chess_board[row][col] = piece_obj

        

    def replace_piece(self, player_num, piece_type, row, col):
        if(piece_type == 1):
            self.chess_board[row][col] = Queen(row, col, player_num)
            symbol = self.chess_board[row][col].get_symbol()
            
        elif(piece_type == 2):
            self.chess_board[row][col] = Bishop(row, col, player_num)
            symbol = self.chess_board[row][col].get_symbol()
            
        elif(piece_type == 3):
            self.chess_board[row][col] = Knight(row, col, player_num)
            symbol = self.chess_board[row][col].get_symbol()
            
        elif(piece_type == 4):
            self.chess_board[row][col] = Rook(row, col, player_num)
            symbol = self.chess_board[row][col].get_symbol()

        piece = symbol + str(player_num)
        self.piece_positions.replace_piece(piece, row, col)




    def move_piece(self, piece_obj, from_row, from_col, to_row, to_col, player_num):
        piece_obj.move(to_row, to_col)
        self.update_board_obj(piece_obj, from_row, from_col, to_row, to_col)
        self.piece_positions.update_board(from_row, from_col, to_row, to_col)

        if(piece_obj.get_symbol == 'P' and piece_obj.can_promote()):
            user_choice = int(self.pawn_promote_menu())
            if(user_choice == 1):
                piece = 'Q' + str(player_num)
                
            elif(user_choice == 2):
                piece = 'B' + str(player_num)

            elif(user_choice == 3):
                piece = 'N' + str(player_num)

            elif(user_choice == 4):
                piece = 'R' + str(player_num)

                
            self.piece_positions.replace_piece(piece, to_row, to_col)    
            self.replace_piece(piece_obj.get_number(),user_choice, to_row, to_col)
            self.on_check(from_row, from_col, from_row, from_col, player_num, piece_obj)
