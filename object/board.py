from object.piece import Rook, Knight, Bishop, Queen, King, Pawn
from resources.globalvariables import dimensions
from object.tile import Tile
from object.hud import Hud


class Board:
    letter_converter = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
    }
    number_converter = {
        "8": 0,
        "7": 1,
        "6": 2,
        "5": 3,
        "4": 4,
        "3": 5,
        "2": 6,
        "1": 7,
    }
    letter_mapper = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H"
    }
    number_mapper = {
        0: "8",
        1: "7",
        2: "6",
        3: "5",
        4: "4",
        5: "3",
        6: "2",
        7: "1"
    }
    board_reference = [
        ['A8', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1'],
        ['B8', 'B7', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1'],
        ['C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'C1'],
        ['D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1'],
        ['E8', 'E7', 'E6', 'E5', 'E4', 'E3', 'E2', 'E1'],
        ['F8', 'F7', 'F6', 'F5', 'F4', 'F3', 'F2', 'F1'],
        ['G8', 'G7', 'G6', 'G5', 'G4', 'G3', 'G2', 'G1'],
        ['H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2', 'H1']
    ]

    board = [
        [Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'),
         Tile('Dark')],
        [Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'),
         Tile('Light')],
        [Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'),
         Tile('Dark')],
        [Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'),
         Tile('Light')],
        [Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'),
         Tile('Dark')],
        [Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'),
         Tile('Light')],
        [Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'),
         Tile('Dark')],
        [Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'), Tile('Light'), Tile('Dark'),
         Tile('Light')]
    ]

    def __init__(self):
        """Initialize Chess Board"""
        self.valid_moves = []
        self.piece_selected_pointer = None
        self.piece_selected = None
        self.king_in_check = False
        self.hud = Hud()

    def clicked(self, x, y):
        """Called when Chess Board is Clicked"""
        my_x = int(x / dimensions["cell_width"])
        my_y = int(y / dimensions["cell_height"])

        # Hud Was Clicked
        if my_y == 8:
            print('Hud pressed')

        # Player Unselected a Piece
        elif self.piece_selected is not None and self.piece_selected == self.board[my_x][my_y].get_piece():
            self.valid_moves = []
            self.piece_selected = None

        # Player is moving the Piece to a Valid Position
        elif self.letter_mapper[my_x] + self.number_mapper[my_y] in self.valid_moves:
            piece = self.board[self.piece_selected_pointer[0]][self.piece_selected_pointer[1]].get_piece()
            self.board[self.piece_selected_pointer[0]][self.piece_selected_pointer[1]].set_piece(None)
            self.moving_piece(piece, self.letter_mapper[my_x], self.number_mapper[my_y])
            self.piece_selected = None
            self.valid_moves = []

        # Player Selected a Piece
        elif self.board[my_x][my_y].get_piece() is not None:
            self.piece_selected = self.board[my_x][my_y].get_piece()
            color_selected = self.board[my_x][my_y].get_piece().get_color()
            if color_selected == 'white':
                self.hud.set_player_turn(1)
            elif color_selected == 'black':
                self.hud.set_player_turn(2)
            self.valid_moves = []
            valid_moves = self.board[my_x][my_y].clicked(self)
            self.piece_selected_pointer = [my_x, my_y]
            for move in valid_moves:
                self.valid_moves.append(move[0])
                if move[1] == "empty":
                    self.board[self.letter_converter[move[0][0]]][self.number_converter[move[0][1]]].set_state(
                        'highlighted')
                else:
                    self.board[self.letter_converter[move[0][0]]][self.number_converter[move[0][1]]].set_state('target')

        # Player Clicked the Board where no piece is located
        else:
            self.piece_selected = None
            self.hud.set_player_turn(0)
            self.valid_moves = []

        self.update()

    def update(self):
        """
        Updates the HUD, showing which player has the advantage
        TODO: Improve the Worth System!
        """
        white_worth = 0
        black_worth = 0
        for row in range(8):
            for col in range(8):
                if self.board[row][col].get_piece() is not None:
                    if self.board[row][col].get_piece().get_color() == 'white':
                        white_worth = white_worth + self.board[row][col].get_piece().get_worth()
                    if self.board[row][col].get_piece().get_color() == 'black':
                        black_worth = black_worth + self.board[row][col].get_piece().get_worth()

        self.hud.set_worth(white_worth - black_worth)

    def draw(self, canvas):
        """Draw Chess Board"""

        # Draw Chess Board
        for row in range(8):
            for col in range(8):
                self.board[row][col].draw(canvas, row, col)

        # Draw Coordinates (A-H & 1=8)
        for key, value in self.letter_converter.items():
            number = (2 * dimensions['number_of_tiles']) - (dimensions['number_of_tiles'] + value)
            canvas.create_text(0 * dimensions["cell_width"] + dimensions['coordinates_translation'],
                               value * dimensions['cell_height'] + dimensions['coordinates_translation'],
                               text=number, font=('Helvetica', dimensions['coordinates_size']),
                               fill='white')
            canvas.create_text((value + 1) * dimensions["cell_width"] - dimensions['coordinates_translation'],
                               dimensions['number_of_tiles'] * dimensions['cell_height'] - dimensions[
                                   'coordinates_translation'],
                               text=key, font=('Helvetica', dimensions['coordinates_size']),
                               fill='white')

        # Draw Hud
        self.hud.draw(canvas)

    def get_piece(self, letter: object, number: object) -> object:
        """Get Piece at Letter and Number (i.e. A5)"""
        return self.board[letter][number].get_piece()

    def moving_piece(self, piece, letter, number):
        """Moves Piece to Letter and Number"""
        piece.set_has_moved(True)
        self.place_piece(piece, letter, number)

    def place_piece(self, piece, letter, number):
        """Places at location specified"""
        piece.set_position(letter + number)
        self.board[self.letter_converter[letter]][self.number_converter[number]].set_piece(piece)

    def check_for_check(self):
        """Checks for to see if King is in Check"""
        self.king_in_check = False
        for row_num in range(8):
            for col_num in range(8):
                if self.board[row_num][col_num].get_piece() is not None:
                    valid_moves = self.board[row_num][col_num].get_piece().get_valid_moves(self)
                    for move in valid_moves:
                        if move[1] == "enemy":
                            if self.board[self.letter_converter[move[0][0]]][self.number_converter[move[0][1]]].get_piece().get_name() == "King":
                                piece_color = self.board[self.letter_converter[move[0][0]]][
                                    self.number_converter[move[0][1]]].get_piece().get_color()
                                if piece_color == 'white':
                                    self.hud.set_player_in_check(1)
                                if piece_color == 'black':
                                    self.hud.set_player_in_check(2)
                                self.king_in_check = True
        if not self.king_in_check:
            self.hud.set_player_in_check(0)

    def init_player_pieces(self, color, number):
        """Initialize Pieces for Player"""
        translate_pieces = 0
        translate_pawns = 0
        if number == 2:
            translate_pieces = 7
            translate_pawns = 5

        self.place_piece(Rook(color, number), 'A', str(1 + translate_pieces))
        self.place_piece(Knight(color, number), 'B', str(1 + translate_pieces))
        self.place_piece(Bishop(color, number), 'C', str(1 + translate_pieces))
        self.place_piece(Queen(color, number), 'D', str(1 + translate_pieces))
        self.place_piece(King(color, number), 'E', str(1 + translate_pieces))
        self.place_piece(Bishop(color, number), 'F', str(1 + translate_pieces))
        self.place_piece(Knight(color, number), 'G', str(1 + translate_pieces))
        self.place_piece(Rook(color, number), 'H', str(1 + translate_pieces))
        self.place_piece(Pawn(color, number), 'A', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'B', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'C', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'D', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'E', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'F', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'G', str(2 + translate_pawns))
        self.place_piece(Pawn(color, number), 'H', str(2 + translate_pawns))

    def get_save_data(self):
        """Get save data from Chess Board: Draft"""
        pass
        """
        save_text = ""
        for row_num in range(8):
            for col_num in range(8):
                save_text = save_text + self.board[row_num][col_num].get_save_data()
        save_text = save_text + "TODO: Insert Move History"
        return save_text"""
