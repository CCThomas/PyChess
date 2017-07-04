import os


class Piece:
    def __init__(self, color):
        self.name = '-'
        self.color = color

    def get_image_path(self):
        return self.image_path

    def get_name(self):
        return self.name

    def set_position(self, letter, number):
        self.letter = letter
        self.number = number

    def get_position(self):
        return [self.letter, self.number]

    def get_letter(self):
        return self.letter

    def get_number(self):
        return self.number


class Bishop(Piece):
    def __init__(self, color):
        self.name = 'b'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/bishop.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/bishop.png')


class King(Piece):
    def __init__(self, color):
        self.name = 'K'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/king.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/king.png')


class Knight(Piece):
    def __init__(self, color):
        self.name = 'k'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/knight.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/knight.png')


class Pawn(Piece):
    def __init__(self, color):
        self.name = 'p'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/pawn.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/pawn.png')


class Queen(Piece):
    def __init__(self, color):
        self.name = 'Q'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/queen.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/queen.png')


class Rook(Piece):
    def __init__(self, color):
        self.name = 'r'
        self.color = color
        current_path = os.path.dirname(__file__)
        if color == 'blue':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/blue/rook.png')
        elif color == 'red':
            self.image_path = os.path.join(current_path, '../resources/images/pieces/red/rook.png')
