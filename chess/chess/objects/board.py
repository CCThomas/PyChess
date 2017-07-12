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
        self.taken_pieces = {}
    """
    def is_reference_on_board(self, move_to):
        for row_num in range(8):
            for col_num in range(8):
                if self.board_reference[row_num][col_num] == move_to:
                    return True
        return False

    def is_piece_on_board(self, piece_name):
        for row_num in range(8):
            for col_num in range(8):
                if self.board_piece[row_num][col_num] is not None \
                        and self.board_piece[row_num][col_num].get_name() == piece_name:
                    return True
        return False

    def can_get_to(self, piece_name, row_num, col_num, move_to):
        next_letter = next_number = None
        if Board.letter_converter[piece_name[0]] == row_num:
            pass
        elif Board.letter_converter[piece_name[0]] < row_num:
            next_letter = Board.letter_converter[piece_name[0]] - 1
        elif Board.letter_converter[piece_name[0]] > row_num:
            next_letter = Board.letter_converter[piece_name[0]] + 1

        if next_number == col_num:
            pass
        elif next_number < col_num:
            next_number = Board.letter_converter[piece_name[0]] - 1
        elif next_number > col_num:
            next_number = Board.letter_converter[piece_name[0]] + 1
        next_spot = str(next_letter) + str(next_number)
        if next_spot == move_to:
            return True
        elif self.board_piece[next_number][next_letter] is None:
            self.can_get_to(piece_name, next_letter, next_number, move_to)
        else:
            return False

    def can_piece_make_move(self, piece_name, move_to):
        for row_num in range(8):
            for col_num in range(8):
                if self.board_piece[row_num][col_num] is not None \
                        and self.board_piece[row_num][col_num].get_name() == piece_name:
                    if move_to in self.board_piece[row_num][col_num].get_valid_moves():
                        if self.board_piece[Board.letter_mapper[move_to[0]]][move_to[1]].get_letter != piece_name[0]:
                            if not self.board_piece[row_num][col_num].get_need_clear_path():
                                return self.can_get_to(piece_name, row_num, col_num, move_to)
        return False

    def move_piece(self, piece_name, move_to):
        for row_num in range(8):
            for col_num in range(8):
                if self.board_piece[row_num][col_num].get_name() == piece_name:
                    self.place_piece(self.board_piece[row_num][col_num], move_to[0], int(move_to[1]))
    
    def place_piece(self, piece, letter, number):
        if piece.get_position() is not None:
            self.board_piece[piece.get_number()][piece.get_letter()] = None
        piece.set_position(letter + str(number))
        self.board_piece[number][Board.letter_mapper[letter]] = piece

    def open_spots(self):
        open_spot = []
        for row_num in range(8):
            for col_num in range(8):
                if self.board_piece[row_num][col_num] is not None:
                    open_spot.append(Board.board_reference[row_num][col_num])
    """

    def move_piece(self, piece_name, piece_location, destination, player_number):
        # Checks if piece_name is valid. if piece_name is at piece_location
        # Checks if piece is Player's Piece
        # Checks if move_to is on board
        # Checks if piece can make the move from piece_location to move_to
        tests = []

        if not self.is_piece_at_location(piece_name, piece_location):
            return "Piece Not At Location"
        if not self.is_players_piece(piece_name, player_number):
            return "Not Player's Piece"
        if not self.is_location_on_board(destination):
            return "Location Not On Board"
        response = self.can_piece_make_move(piece_location, destination, player_number)
        if response != "True":
            return response

        self.make_move(piece_location, destination, player_number)
        return "True"

    def make_move(self, piece_location, destination, player_number):
        piece = self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]]
        piece_dest = self.board_piece[Board.letter_mapper[destination[0]]][Board.number_mapper[destination[1]]]
        if piece_dest is not None:
            self.taken_pieces[player_number].append(piece_dest)
        self.board_piece[Board.letter_mapper[destination[0]]][Board.number_mapper[destination[1]]] = piece
        self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]] = None
        piece.set_position(destination)

    def get_number_mapper_key(self, value):
        for key in Board.number_mapper:
            if Board.number_mapper[key] == value:
                return key

    def get_letter_mapper_key(self, value):
        for key in Board.letter_mapper:
            if Board.letter_mapper[key] == value:
                return key

    def check_if_path_is_clear(self, piece_location, destination):
        new_location = piece_location
        if Board.letter_mapper[new_location[0]] < Board.letter_mapper[destination[0]]:
            new_letter_num = Board.letter_mapper[new_location[0]] + 1
            new_location[0] = Board.get_letter_mapper_key(new_letter_num)
        elif Board.letter_mapper[new_location[0]] > Board.letter_mapper[destination[0]]:
            new_letter_num = Board.letter_mapper[new_location[0]] - 1
            new_location[0] = Board.get_letter_mapper_key(new_letter_num)

        if Board.number_mapper[new_location[1]] < Board.number_mapper[destination[1]]:
            new_letter_num = Board.number_mapper[new_location[1]] + 1
            new_location[1] = Board.number_mapper(new_letter_num)
        elif Board.number_mapper[new_location[1]] > Board.number_mapper[destination[1]]:
            new_letter_num = Board.number_mapper[new_location[1]] - 1
            new_location[1] = Board.get_number_mapper_key(new_letter_num)

        if new_location == destination:
            return True
        elif self.board_piece[Board.letter_mapper[new_location[0]]][Board.number_mapper[new_location[1]]] is None:
            return self.check_if_path_is_clear(new_location, destination)
        else:
            return False

    def can_piece_make_move(self, piece_location, destination, player_number):
        piece = self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]]
        print("Piece Name: " + piece.get_name())
        print("Piece Loca: " + piece.get_position())
        valid_moves = piece.get_valid_moves()
        if destination in valid_moves:
            piece_dest = self.board_piece[Board.letter_mapper[destination[0]]][Board.number_mapper[destination[1]]]
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

    def is_location_on_board(self, location):
        if location[0] in Board.letter_mapper and location[1] in Board.number_mapper:
            return True
        else:
            return False

    def is_players_piece(self, piece_name, player_number):
        if piece_name[0] == self.get_player_color(player_number)[0]:
            return True
        else:
            return False

    def is_piece_at_location(self, piece_name, piece_location):
        if self.board_piece[Board.letter_mapper[piece_location[0]]][Board.number_mapper[piece_location[1]]].get_name() == piece_name:
            return True
        else:
            return False

    def place_piece(self, piece, letter, number):
        piece.set_position(letter+number)
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

    def init_player_pieces(self, color, number):
        self.players[number] = color

        translate_pieces = 0
        translate_pawns = 0
        if number == 2:
            translate_pieces = 7
            translate_pawns = 5

        self.place_piece(Rook(color),   'A', str(1 + translate_pieces))
        self.place_piece(Knight(color), 'B', str(1 + translate_pieces))
        self.place_piece(Bishop(color), 'C', str(1 + translate_pieces))
        self.place_piece(King(color),   'D', str(1 + translate_pieces))
        self.place_piece(Queen(color),  'E', str(1 + translate_pieces))
        self.place_piece(Bishop(color), 'F', str(1 + translate_pieces))
        self.place_piece(Knight(color), 'G', str(1 + translate_pieces))
        self.place_piece(Rook(color),   'H', str(1 + translate_pieces))
        self.place_piece(Pawn(color, number), 'A', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'B', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'C', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'D', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'E', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'F', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'G', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'H', str(2 + translate_pawns))
