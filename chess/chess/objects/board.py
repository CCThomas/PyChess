from chess.objects.pieces import *
from chess.io import output

"""
    A    B    C    D    E    F    G    H
  -----------------------------------------
1 | rr | rk | rb | rK | rq | rb | rk | rr |
  -----------------------------------------
2 | rp | rp | rp | rp | rP | rP | rP | rP |
  -----------------------------------------
3 | -- | -- | -- | -- | -- | -- | -- | -- |
  -----------------------------------------
4 | -- | -- | -- | -- | -- | -- | -- | -- |
  -----------------------------------------
5 | -- | -- | -- | -- | -- | -- | -- | -- |
  -----------------------------------------
6 | -- | -- | -- | -- | -- | -- | -- | -- |
  -----------------------------------------
7 | bp | bp | bp | bp | bp | bp | bp | bp |
  -----------------------------------------
8 | br | bk | bb | bK | bq | bB | bk | br |
  -----------------------------------------

"""


class Board:
    letter_converter = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
    }
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
        output.run_log('write', "Chess Board Created")
        self.board_piece = Board.board_piece

    def get_image_path(self):
        return self.image_path

    def place_piece(self, piece, letter, number):
        self.board_piece[Board.letter_converter[letter]][7] = piece

    def print_board(self):
        print('    A    B    C    D    E    F    G    H\n  |---------------------------------------|')
        for row_num in range(8):
            print(row_num, end=' | ')
            for col_num in range(8):
                if self.board_piece[row_num][col_num] is not None:
                    print(self.board_piece[row_num][col_num].get_name(), end=' | ')
                else:
                    print('--', end=' | ')
            print('\n  |---------------------------------------|')

    def init_player_pieces(self, color, number):
        translate_pieces = 0
        translate_pawns = 0
        if number == 2:
            translate_pieces = 7
            translate_pawns = 5

        self.place_piece(Rook(color),   'A', 0 + translate_pieces)
        self.place_piece(Knight(color), 'B', 0 + translate_pieces)
        self.place_piece(Bishop(color), 'C', 0 + translate_pieces)
        self.place_piece(King(color),   'D', 0 + translate_pieces)
        self.place_piece(Queen(color),  'E', 0 + translate_pieces)
        self.place_piece(Bishop(color), 'F', 0 + translate_pieces)
        self.place_piece(Knight(color), 'G', 0 + translate_pieces)
        self.place_piece(Rook(color),   'H', 0 + translate_pieces)
        self.place_piece(Pawn(color),   'A', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'B', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'C', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'D', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'E', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'F', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'G', 1 + translate_pawns)
        self.place_piece(Pawn(color),   'H', 1 + translate_pawns)


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
