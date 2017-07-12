from chess.objects.pieces import *
from chess.io import output

# import numpy

"""
#################################################################################################
#     A    B    C    D    E    F    G    H      #                    Usage                      #
#   -----------------------------------------   #   -----------------------------------------   #
# 1 | rr | rk | rb | rK | rq | rb | rk | rr |   #   player num: <command>                       #
#   -----------------------------------------   #                                               #
# 2 | rp | rp | rp | rp | rP | rP | rP | rP |   #   commands                                    #
#   -----------------------------------------   #   * move <piece> <location> <destination>     #
# 3 | -- | -- | -- | -- | -- | -- | -- | -- |   #       - piece: The piece to move              #
#   -----------------------------------------   #       - location: piece's position on board   #
# 4 | -- | -- | -- | -- | -- | -- | -- | -- |   #       - destination: place to move piece to   #
#   -----------------------------------------   #   * save                                      #
# 5 | -- | -- | -- | -- | -- | -- | -- | -- |   #       - saves game                            #
#   -----------------------------------------   #   * quit                                      #
# 6 | -- | -- | -- | -- | -- | -- | -- | -- |   #       - quits game                            #
#   -----------------------------------------   #                                               #
# 7 | bp | bp | bp | bp | bp | bp | bp | bp |   #                                               #
#   -----------------------------------------   #                                               #
# 8 | br | bk | bb | bK | bq | bB | bk | br |   #                                               #
#   -----------------------------------------   #                                               #
#################################################################################################
"""


class Board:
    letter_mapper = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
    }
    number_mapper = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7
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

    def __init__(self):
        output.run_log('write', "Chess Board Created")
        self.board_piece = Board.board_piece
        self.players = {}
        self.taken_pieces = {1: [], 2: []}

    # Called External to Program
    def move_piece(self, piece_name, piece_location, destination, player_number):
        if self.get_piece(piece_location[0], piece_location[1]) is None:
            return "No Piece At Location"
        if piece_name[0] != self.get_player_color(player_number)[0]:
            return "Not Player's Piece"
        if self.get_piece(piece_location[0], piece_location[1]).get_name() != piece_name:
            return "Piece Not At Location"
        if destination[0] not in self.letter_mapper or destination[1] not in self.number_mapper:
            return "Location Not On Board"
        response = self.can_piece_make_move(piece_location, destination, player_number)
        if response != "True":
            return response

        return_string = self.make_move(piece_location, destination, player_number)
        return return_string

    def make_move(self, piece_location, destination, player_number):
        piece = self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]]
        piece_dest = self.board_piece[Board.letter_mapper[destination[0]]][Board.number_mapper[destination[1]]]
        if piece_dest is not None:
            if piece_dest.get_name()[1] == "K":
                return "Game Over"
            self.taken_pieces[player_number].append(piece_dest)
        self.board_piece[Board.letter_mapper[destination[0]]][Board.number_mapper[destination[1]]] = piece
        self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]] = None
        piece.set_position(destination)
        return "True"

    def can_piece_make_move(self, piece_location, destination, player_number):
        piece = self.get_piece(piece_location[0], piece_location[1])
        valid_moves = piece.get_valid_moves()
        if destination in valid_moves:
            piece_dest = self.get_piece(destination[0], destination[1])
            if piece_dest is None or piece_dest.get_name()[0] != piece.get_name()[0]:
                if not piece.get_need_clear_path() or self.check_if_path_is_clear(piece_location, destination):
                    return "True"
                else:
                    return "Path Not Clear"
            else:
                return "Destination Is Help By Friendly Piece"
        else:
            valid_moves_string = ""
            for move in valid_moves:
                valid_moves_string = valid_moves_string + ' ' + move
            return "This Piece Can Not Make That Move. Valid Moves As Follows\n" + valid_moves_string

    def check_if_path_is_clear(self, piece_location, destination):

        def get_number_mapper_key(value) -> str:
            for key in self.number_mapper:
                if self.number_mapper[key] == value:
                    return str(key)

        def get_letter_mapper_key(value) -> str:
            for key in self.letter_mapper:
                if self.letter_mapper[key] == value:
                    return str(key)

        new_location = piece_location
        if self.letter_mapper[new_location[0]] < self.letter_mapper[destination[0]]:
            new_letter_num = self.letter_mapper[new_location[0]] + 1
            new_location = get_letter_mapper_key(new_letter_num) + new_location[1]
        elif self.letter_mapper[new_location[0]] > self.letter_mapper[destination[0]]:
            new_letter_num = Board.letter_mapper[new_location[0]] - 1
            new_location = get_letter_mapper_key(new_letter_num) + new_location[1]

        if self.number_mapper[new_location[1]] < self.number_mapper[destination[1]]:
            new_letter_num = Board.number_mapper[new_location[1]] + 1
            new_location = new_location[0] + get_number_mapper_key(new_letter_num)
        elif self.number_mapper[new_location[1]] > self.number_mapper[destination[1]]:
            new_letter_num = self.number_mapper[new_location[1]] - 1
            new_location = new_location[0] + get_number_mapper_key(new_letter_num)

        if new_location == destination:
            return True
        elif self.board_piece[Board.letter_mapper[new_location[0]]][Board.number_mapper[new_location[1]]] is None:
            return self.check_if_path_is_clear(new_location, destination)
        else:
            return False

    def get_piece(self, number, letter):
        return self.board_piece[Board.letter_mapper[number]][Board.number_mapper[letter]]

    def place_piece(self, piece, letter, number):
        piece.set_position(letter + number)
        self.board_piece[Board.letter_mapper[letter]][Board.number_mapper[number]] = piece

    def print_board(self):
        board = self.board_piece

        print("#################################################################################################")
        print("#     A    B    C    D    E    F    G    H      #                    Usage                      #")
        print("#   -----------------------------------------   #   -----------------------------------------   #")
        for row_num in range(8):
            print("# " + str(row_num + 1), end=' | ')
            for col_num in range(8):
                if board[col_num][row_num] is not None:
                    print(board[col_num][row_num].get_name(), end=' | ')
                else:
                    print('--', end=' | ')

            if row_num == 1:
                print('  #   player num: <command>                       #')
                print("#   -----------------------------------------   #                                              "
                      " #")
            elif row_num == 2:
                print("  #   commands                                    #")
                print("#   -----------------------------------------   #   * move <piece> <location> <destination>    "
                      " #")
            elif row_num == 3:
                print("  #       - piece: The piece to move              #")
                print("#   -----------------------------------------   #       - location: piece's position on board  "
                      " #")
            elif row_num == 4:
                print("  #       - destination: place to move piece to   #")
                print("#   -----------------------------------------   #   * save                                     "
                      " #")
            elif row_num == 5:
                print("  #       - saves game                            #")
                print("#   -----------------------------------------   #   * quit                                     "
                      " #")
            elif row_num == 6:
                print("  #       - quits game                            #")
                print("#   -----------------------------------------   #                                              "
                      " #")
            else:
                print("  #                                               #")
                print("#   -----------------------------------------   #                                              "
                      " #")
        print("#################################################################################################")

    def get_player_color(self, player_number):
        return self.players[player_number]

    def init_board(self):
        self.board_piece = Board.board_piece

    def init_player_pieces(self, color, number):
        self.players[number] = color

        translate_pieces = 0
        translate_pawns = 0
        if number == 2:
            translate_pieces = 7
            translate_pawns = 5

        self.place_piece(Rook(color), 'A', str(1 + translate_pieces))
        self.place_piece(Knight(color), 'B', str(1 + translate_pieces))
        self.place_piece(Bishop(color), 'C', str(1 + translate_pieces))
        self.place_piece(King(color), 'D', str(1 + translate_pieces))
        self.place_piece(Queen(color), 'E', str(1 + translate_pieces))
        self.place_piece(Bishop(color), 'F', str(1 + translate_pieces))
        self.place_piece(Knight(color), 'G', str(1 + translate_pieces))
        self.place_piece(Rook(color), 'H', str(1 + translate_pieces))
        self.place_piece(Pawn(color, number), 'A', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'B', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'C', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'D', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'E', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'F', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'G', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'H', str(2 + translate_pawns))
