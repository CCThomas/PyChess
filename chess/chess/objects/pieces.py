from chess.io import output


class Piece:
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

    def __init__(self, color):
        output.run_log('write', "Piece Created")
        self.name = '--'
        self.color = color
        self.position = None

    def get_color(self):
        return self.color

    def convert_letter(self):
        if self.position is None:
            return None
        return self.letter_converter[self.get_letter()]

    def get_letter(self):
        if self.position is None:
            return None
        return self.position[0]

    def get_name(self):
        return self.color[0] + self.name

    def get_number(self):
        if self.position is None:
            return None
        return self.position[1]

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_valid_moves(self):
        valid_moves = []
        for row_num in range(8):
            for col_num in range(8):
                if self.is_move_valid(Piece.board_reference[row_num][col_num]):
                    valid_moves.append(Piece.board_reference[row_num][col_num])
        return valid_moves


class Bishop(Piece):
    def __init__(self, color):
        output.run_log('write', "Bishop Created")
        self.name = 'b'
        self.color = color
        self.position = None

    def is_move_valid(self, move):
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) \
                == abs(int(self.get_number()) - int(move[1])):
            return True
        else:
            return False


class King(Piece):
    def __init__(self, color):
        output.run_log('write', "King Created")
        self.name = 'K'
        self.color = color
        self.position = None

    def is_move_valid(self, move):
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) <= 1 \
                and abs(int(self.get_number()) - int(move[1])) <= 1:
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, color):
        output.run_log('write', "Knight Created")
        self.name = 'k'
        self.color = color
        self.position = None

    def is_move_valid(self, move):
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
        output.run_log('write', "Pawn Created")
        self.name = 'p'
        self.color = color
        self.team = team
        self.position = None
        self.has_moved = False

    def set_position(self, position):
        if self.position is None:
            self.position = position
        else:
            self.has_moved = True
            self.position = position


    def is_move_valid(self, move):
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
        output.run_log('write', "Queen Created")
        self.name = 'Q'
        self.color = color
        self.position = None

    def is_move_valid(self, move):
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
        output.run_log('write', "Rook Created")
        self.name = 'r'
        self.color = color
        self.position = None

    def is_move_valid(self, move):
        if self.get_letter() == move[0] and self.get_number() != move[1]:
            return True
        elif self.get_letter() != move[0] and self.get_number() == move[1]:
            return True
        else:
            return False
