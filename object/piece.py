from resources.globalvariables import dimensions
from object.spritesheet import Spritesheet

class Piece:
    """Abstract class for Chess Pieces"""
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

    def get_color(self):
        """Return color"""
        return self.color

    def convert_letter(self):
        """Convert letter position to an Integer and return that value."""
        return self.letter_converter[self.get_letter()]

    def convert_number(self):
        """Convert number position to an Integer and return that value."""
        return self.number_converter[self.get_number()]

    def get_letter(self):
        """Return letter position."""
        return self.position[0]

    def get_name(self):
        """Return Name."""
        return self.name

    def get_abbr_name(self):
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

    def get_has_moved(self):
        return self.has_moved

    def set_has_moved(self, has_moved):
        """Set has moved"""
        self.has_moved = has_moved

    def get_worth(self):
        """Return worth"""
        return self.worth

    def set_worth(self, worth):
        """Set worth"""
        self.worth = worth

    def get_team(self):
        return self.team

    def is_path_clear(self, board, current_location, destination):
        """Checks if there is a clear path between current location and destination"""
        new_location = current_location
        if new_location[0] < destination[0]:
            new_location[0] = new_location[0] + 1
        elif new_location[0] > destination[0]:
            new_location[0] = new_location[0] - 1

        if new_location[1] < destination[1]:
            new_location[1] = new_location[1] + 1
        elif new_location[1] > destination[1]:
            new_location[1] = new_location[1] - 1

        if new_location == destination:
            return True
        elif board.get_piece(new_location[0], new_location[1]) is None:
            return self.is_path_clear(board, new_location, destination)
        else:
            return False

    def get_valid_moves(self, board):
        """Return all valid moves this piece can make"""
        valid_moves = []
        for row_num in range(8):
            for col_num in range(8):
                if self.is_move_valid(Piece.board_reference[row_num][col_num], board) \
                        and Piece.board_reference[row_num][col_num] != self.position:
                    if board.get_piece(row_num, col_num) is not None:
                        if board.get_piece(row_num, col_num).get_color() != self.get_color():
                            if self.get_need_clear_path():
                                if self.is_path_clear(board, [self.convert_letter(), self.convert_number()],
                                                      [row_num, col_num]):
                                    valid_moves.append([Piece.board_reference[row_num][col_num], "enemy"])
                            else:
                                valid_moves.append([Piece.board_reference[row_num][col_num], "enemy"])
                    else:
                        if self.get_need_clear_path():
                            if self.is_path_clear(board, [self.convert_letter(), self.convert_number()],
                                                  [row_num, col_num]):
                                valid_moves.append([Piece.board_reference[row_num][col_num], "empty"])
                        else:
                            valid_moves.append([Piece.board_reference[row_num][col_num], "empty"])
        return valid_moves

    def is_move_valid(self, move, board):
        pass  # Overwrite in Subclass

    def draw(self, canvas, x, y, state, tile_color):
        self.get_image(state, tile_color)
        canvas.create_image(x, y, image=self.image)

    def get_state(self, state):
        if state == 'normal':
            return 0
        elif state == 'selected':
            return 1
        elif state == 'target':
            return 2
        else:
            print("Error:", state)
            return 0

    def get_image(self, state, tile_color):
        color_number = 0
        if self.color == 'black':
            color_number = 2
        if tile_color == 'Light':
            color_number = color_number + 1
        self.image = self.spritesheet.get_sprite(color_number, self.get_state(state), dimensions['piece_size'], dimensions['piece_size'])


class Bishop(Piece):
    def __init__(self, color, team):
        """Constructor for Bishop"""
        self.name = 'bishop'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = True
        self.team = team
        self.worth = 3
        self.my_image = None
        self.spritesheet = Spritesheet("piece/Bishop-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
        """Check if bishop can make this move from it's current position. Return result"""
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) \
                == abs(int(self.get_number()) - int(move[1])):
            return True
        else:
            return False


class King(Piece):
    def __init__(self, color, team):
        """Constructor for King"""
        self.name = 'King'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = True
        self.team = team
        self.worth = 0  # Infinitely Valuable
        self.spritesheet = Spritesheet("piece/King-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
        """Check if King can make this move from it's current position. Return result"""
        if abs(self.convert_letter() - Piece.letter_converter[move[0]]) <= 1 \
                and abs(int(self.get_number()) - int(move[1])) <= 1:
            return True
        elif not self.has_moved:
            # TODO Check is the King can switch with a Rook
            if board.get_piece(self.letter_converter[move[0]], self.number_converter[move[1]]) is not None and board.get_piece(self.letter_converter[move[0]], self.number_converter[move[1]]).get_name() == 'rook' and not \
                    board.get_piece(self.letter_converter[move[0]], self.number_converter[move[1]]).get_has_moved():
                num = self.number_converter[move[1]]
                for col_num in range(num, 0):
                    if board.get_piece(self.letter_converter[move[0]],self.number_converter[move[1]]) is None:
                        break
        else:
            return False


class Knight(Piece):
    def __init__(self, color, team):
        """Constructor for Knight"""
        self.name = 'knight'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = False
        self.team = team
        self.worth = 3
        self.spritesheet = Spritesheet("piece/Knight-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
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
        self.name = 'pawn'
        self.color = color
        self.team = team
        self.position = None
        self.has_moved = False
        self.need_clear_path = True
        self.worth = 1
        self.spritesheet = Spritesheet("piece/Pawn-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
        """Check if pawn can make this move from it's current position. Return result"""
        direction = 1
        if self.team == 2:
            direction = -1

        if self.get_letter() == move[0]:
            if int(self.get_number()) + direction == int(move[1]) and board.get_piece(self.letter_converter[move[0]],
                                                                                      self.number_converter[
                                                                                          move[1]]) is None:
                return True
            elif not self.has_moved and int(self.get_number()) + (2 * direction) == int(move[1]) and board.get_piece(
                    self.letter_converter[move[0]], self.number_converter[move[1]]) is None:
                return True  # 'en passant'
            else:
                return False
        if self.left_letter() is not None and self.left_letter() == move[0]:
            piece_to_attack = board.get_piece(self.letter_converter[move[0]], self.number_converter[move[1]])
            if int(self.get_number()) + direction == int(
                    move[1]) and piece_to_attack is not None and piece_to_attack.get_color() != self.color:
                return True
            else:
                return False
        if self.right_letter() is not None and self.right_letter() == move[0]:
            piece_to_attack = board.get_piece(self.letter_converter[move[0]], self.number_converter[move[1]])
            if int(self.get_number()) + direction == int(
                    move[1]) and piece_to_attack is not None and piece_to_attack.get_color() != self.color:
                return True
            else:
                return False
        else:
            return False

    def left_letter(self):
        if self.convert_letter() - 1 >= 0:
            return self.letter_mapper[self.convert_letter() - 1]
        else:
            return None

    def right_letter(self):
        if self.convert_letter() + 1 <= 7:
            return self.letter_mapper[self.convert_letter() + 1]
        else:
            return None


class PawnPlaceHolder(Piece):
    def __init__(self, color, team):
        """Constructor for Queen"""
        self.name = 'pawnplaceholder'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = False
        self.team = team
        self.worth = 0


class Queen(Piece):
    def __init__(self, color, team):
        """Constructor for Queen"""
        self.name = 'Queen'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = True
        self.team = team
        self.worth = 9
        self.spritesheet = Spritesheet("piece/Queen-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
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
    def __init__(self, color, team):
        """Constructor for Rook"""
        self.name = 'rook'
        self.color = color
        self.position = None
        self.has_moved = False
        self.need_clear_path = True
        self.team = team
        self.worth = 5
        self.spritesheet = Spritesheet("piece/Rook-Spritesheet.png", 32, 32)

    def is_move_valid(self, move, board):
        """Check if rook can make this move from it's current position. Return result"""
        if self.get_letter() == move[0] and self.get_number() != move[1]:
            return True
        elif self.get_letter() != move[0] and self.get_number() == move[1]:
            return True
        else:
            return False
