from chess.io import output


class Piece:
    """Abstract class for Chess Pieces"""
    board_reference = [
        ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
        ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
        ['A1', 'B2', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    ]
    letter_converter = {
        "-": -1,
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
        "-": -1,
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
    }

    def get_color(self):
        """Return color"""
        return self.color

    def convert_letter(self):
        """Convert letter position to an Integer and return that value."""
        return self.letter_converter[self.get_letter()]

    def convert_number(self):
        """Convert number position to an Integer and return that value."""
        return self.letter_converter[self.get_number()]

    def get_letter(self):
        """Return letter position."""
        return self.position[0]

    def get_name(self):
        """Return Name."""
        return self.name

    def get_abrv_name(self):
        """Return abbreviated name."""
        return self.color[0] + self.name[0]

    def get_number(self):
        """Return number position."""
        return self.position[1]

    def get_need_clear_path(self):
        """Return whether this piece needs a clear path to move."""
        return self.need_clear_path

    def get_position(self):
        """Return position."""
        return self.position

    def set_position(self, position):
        """Set position."""
        self.position = position

    def get_worth(self):
        """Return worth"""
        return self.worth

    def set_worth(self, worth):
        """Set worth"""
        self.worth = worth

    def get_valid_moves(self, board):
        """Return all valid moves this piece can make"""
        valid_moves = []
        for row_num in range(8):
            for col_num in range(8):
                if self.is_move_valid(Piece.board_reference[row_num][col_num])\
                   and Piece.board_reference[row_num][col_num] != self.position:
                    if board.get_piece(row_num, col_num) is not None\
                       and :

                    # TODO check if a piece is at this spot. Handle cases
                    # TODO check if piece needs a clear path
                    valid_moves.append(Piece.board_reference[row_num][col_num])
        return valid_moves


class Bishop(Piece):
    def __init__(self, color):
        """Constructor for Bishop"""
        output.run_log('write', "Bishop Created")
        self.name = 'bishop'
        self.color = color
        self.position = None
        self.need_clear_path = True
        self.worth = 3

    def is_move_valid(self, move):
        """Check if bishop can make this move from it's current position. Return result"""
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) \
                == abs(int(self.get_number()) - int(move[1])):
            return True
        else:
            return False


class King(Piece):
    def __init__(self, color):
        """Constructor for King"""
        output.run_log('write', "King Created")
        self.name = 'King'
        self.color = color
        self.position = None
        self.need_clear_path = True
        self.worth = 0  # Infinitely Valuable

    def is_move_valid(self, move):
        """Check if King can make this move from it's current position. Return result"""
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) <= 1 \
                and abs(int(self.get_number()) - int(move[1])) <= 1:
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, color):
        """Constructor for Knight"""
        output.run_log('write', "Knight Created")
        self.name = 'knight'
        self.color = color
        self.position = None
        self.need_clear_path = False
        self.worth = 3

    def is_move_valid(self, move):
        """Check if knight can make this move from it's current position. Return result"""
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) == 1 \
                and abs(int(self.get_number()) - int(move[1])) == 2:
            return True
        elif abs(self.convert_letter() - Piece.letter_converter[move[0]]) == 2 \
                and abs(int(self.get_number()) - int(move[1])) == 1:
            return True
        else:
            return False


class Pawn(Piece):
    def __init__(self, color, team):
        """Constructor for Pawn"""
        output.run_log('write', "Pawn Created")
        self.name = 'pawn'
        self.color = color
        self.team = team
        self.position = None
        self.has_moved = False
        self.need_clear_path = False
        self.worth = 1

    def is_move_valid(self, move):
        """Check if pawn can make this move from it's current position. Return result"""
        direction = 1
        if self.team == 2:
            direction = -1

        if self.get_letter() == move[0]:
            if int(self.get_number()) + direction == int(move[1]):
                return True
            elif not self.has_moved and int(self.get_number()) + (2*direction) == int(move[1]):
                return True
            else:
                return False
        else:
            return False


class Queen(Piece):
    def __init__(self, color):
        """Constructor for Queen"""
        output.run_log('write', "Queen Created")
        self.name = 'Queen'
        self.color = color
        self.position = None
        self.need_clear_path = True
        self.worth = 9

    def is_move_valid(self, move):
        """Check if queen can make this move from it's current position. Return result"""
        if self.get_letter() == move[0] and self.get_number() != move[1]:
            return True
        elif self.get_letter() != move[0] and self.get_number() == move[1]:
            return True
        elif abs(self.convert_letter() - Piece.letter_converter[move[0]]) \
                == abs(int(self.get_number()) - int(move[1])):
            return True
        else:
            return False


class Rook(Piece):
    def __init__(self, color):
        """Constructor for Rook"""
        output.run_log('write', "Rook Created")
        self.name = 'rook'
        self.color = color
        self.position = None
        self.need_clear_path = True
        self.worth = 5

    def is_move_valid(self, move):
        """Check if rook can make this move from it's current position. Return result"""
        if self.get_letter() == move[0] and self.get_number() != move[1]:
            return True
        elif self.get_letter() != move[0] and self.get_number() == move[1]:
            return True
        else:
            return False
