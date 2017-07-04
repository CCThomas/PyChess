from chess.objects.pieces import *
import os


class Board:
    board_reference = [
        ['A1', 'B2', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
        ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
        ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
    ]
    board_piece = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    board_text = [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

    def __init__(self):
        print("Chess Board Created")
        current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(current_path, '../resources/images/board/board.png')
        self.board_text = Board.board_text

    def get_image_path(self):
        return self.image_path

    def place_piece(self, piece, letter, number):
        if letter == 'A':
            self.board_piece[number][0] = piece
        if letter == 'B':
            self.board_piece[number][1] = piece
        if letter == 'C':
            self.board_piece[number][2] = piece
        if letter == 'D':
            self.board_piece[number][3] = piece
        if letter == 'E':
            self.board_piece[number][4] = piece
        if letter == 'F':
            self.board_piece[number][5] = piece
        if letter == 'G':
            self.board_piece[number][6] = piece
        if letter == 'H':
            self.board_piece[number][7] = piece

    def print_board(self):
        print('  A B C D E F G H')
        for row in range(0,8):
            print(row+1, end=' ')
            for column in range(0,8):
                if self.board_piece[row][column] is not None:
                    print(self.board_piece[row][column].get_name(), end=' ')
            print('')

    def draw_board(self,canvas):
        from chess.game import dimensions
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    canvas.create_rectangle(col * dimensions["cell_width"], row * dimensions['cell_height'], (col + 1) * dimensions['cell_width'],
                                            (row + 1) * dimensions['cell_height'], fill='black')
                if self.board_piece[row][col] is not None:
                    print(str(col * dimensions["cell_width"]) + ' ' + str(row * dimensions['cell_height']))
                    canvas.create_text(col * dimensions["cell_width"] + dimensions['piece_translation'], row * dimensions['cell_height'] + dimensions['piece_translation'],
                                       text=self.board_piece[row][col].get_name(), font=('Helvetica',dimensions['piece_size']),
                                       fill=self.board_piece[row][col].get_color(), activefill='green')

    def init_player(self, color, number):
        translate_pieces = 0
        translate_pawns = 0
        if number == 2:
            translate_pieces = 7
            translate_pawns = 5

        self.place_piece(Rook(color), 'A', 0 + translate_pieces)

    """
    def init_player(self, color):
        self.color = color
        self.pieces = {
            'left_rook': Piece,
            'left_knight': Piece,
            'left_bishop': Piece,
            'king': Piece,
            'queen': Piece,
            'right_bishop': Piece,
            'right_knight': Piece,
            'right_rook': Piece,
            'pawn_1': Piece,
            'pawn_2': Piece,
            'pawn_3': Piece,
            'pawn_4': Piece,
            'pawn_5': Piece,
            'pawn_6': Piece,
            'pawn_7': Piece,
            'pawn_8': Piece
        }

    def get_pieces(self):
        return self.pieces

    def init_pieces(self, side):
        translate = 0
        translate_pawns = 0
        print(side)
        if side == 'south':
            translate = 7
            translate_pawns = 5

        self.pieces['left_rook'] = Rook(self.color)
        self.pieces['left_rook'].set_position('A', 0 + translate)
        self.pieces['left_knight'] = Knight(self.color)
        self.pieces['left_knight'].set_position('B', 0 + translate)
        self.pieces['left_bishop'] = Bishop(self.color)
        self.pieces['left_bishop'].set_position('C', 0 + translate)
        self.pieces['king'] = King(self.color)
        self.pieces['king'].set_position('D', 0 + translate)
        self.pieces['queen'] = Queen(self.color)
        self.pieces['queen'].set_position('E', 0 + translate)
        self.pieces['right_bishop'] = Bishop(self.color)
        self.pieces['right_bishop'].set_position('F', 0 + translate)
        self.pieces['right_knight'] = Knight(self.color)
        self.pieces['right_knight'].set_position('G', 0 + translate)
        self.pieces['right_rook'] = Rook(self.color)
        self.pieces['right_rook'].set_position('H', 0 + translate)
        self.pieces['pawn_1'] = Pawn(self.color)
        self.pieces['pawn_1'].set_position('A', 1 + translate_pawns)
        self.pieces['pawn_2'] = Pawn(self.color)
        self.pieces['pawn_2'].set_position('B', 1 + translate_pawns)
        self.pieces['pawn_3'] = Pawn(self.color)
        self.pieces['pawn_3'].set_position('C', 1 + translate_pawns)
        self.pieces['pawn_4'] = Pawn(self.color)
        self.pieces['pawn_4'].set_position('D', 1 + translate_pawns)
        self.pieces['pawn_5'] = Pawn(self.color)
        self.pieces['pawn_5'].set_position('E', 1 + translate_pawns)
        self.pieces['pawn_6'] = Pawn(self.color)
        self.pieces['pawn_6'].set_position('F', 1 + translate_pawns)
        self.pieces['pawn_7'] = Pawn(self.color)
        self.pieces['pawn_7'].set_position('G', 1 + translate_pawns)
        self.pieces['pawn_8'] = Pawn(self.color)
        self.pieces['pawn_8'].set_position('H', 1 + translate_pawns)
        """
