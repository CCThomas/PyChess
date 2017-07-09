from chess.io import output


class Piece:
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
        pass


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
