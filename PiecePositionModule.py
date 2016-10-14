#Author: NWANKWO CHUKWUEBUKA JUSTIN
#  Date: 5/13/2016   


"""
The first letter identifies the chess piece
'x' is player's number 1 or 2
Px -> pawn 
Nx -> Knight
Bx -> Bishop
Kx -> King
Qx -> Queen
"""


class PiecePositions:
    chess_board =   [['R2','N2','B2','K2','Q2','B2','N2','R2'],
                     ['P2','P2','P2','P2','P2','P2','P2','P2'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['--','--','--','--','--','--','--','--'],
                     ['P1','P1','P1','P1','P1','P1','P1','P1'],
                     ['R1','N1','B1','K1','Q1','B1','N1','R1']]

    vertical_label = range(8, 0, -1)
    horizontal_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    def display_board(self):
        print '',               #for indentation
        for col in self.horizontal_label:
            print ' | ',col,
        
        print ' |'

        board_row = 0
        for row in self.vertical_label:
            print row, '|',
            for piece in self.chess_board[board_row]:
                print piece, ' |',
        
            print row
            board_row += 1
        
        print '',               #for indentation
        for col in self.horizontal_label:
            print ' | ',col,
        
        print ' |'
        print
        print


    def get_piece(self, row, col):
        piece = self.chess_board[row][col]
        chess_piece = piece[0]
        piece_num = piece[1]
        if(piece_num != '-'):
            piece_num = int(piece_num)
        return (chess_piece, piece_num)

    def update_board(self,from_row, from_col, to_row, to_col):
        self.chess_board[to_row][to_col] = self.chess_board[from_row][from_col]
        self.chess_board[from_row][from_col] = '--'
        

    def replace_piece(self, piece, row, col):
        self.chess_board[row][col] = piece

                

            
