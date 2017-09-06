from resources.globalvariables import dimensions
from object.spritesheet import Spritesheet
from tkinter import NW


class Tile:
    def __init__(self, tile_color):
        self.tile_color = tile_color
        self.spritesheet = Spritesheet("tile/" + tile_color + "-Spritesheet.png", 32, 32)

        self.piece = None
        self.state = 'normal'

    def clicked(self, board):
        self.state = 'selected'
        valid_moves = self.piece.get_valid_moves(board)
        return valid_moves

    def set_state(self, state):
        self.state = state

    def get_state(self):
        if self.state == 'normal' or self.state == 'left':
            return 0
        elif self.state == 'selected' or self.state == 'center':
            return 1
        elif self.state == 'highlighted' or self.state == 'right':
            return 2
        elif self.state == 'target':
            return 3

    def reset_state(self):
        if self.state not in ['left', 'center', 'right']:
            self.state = 'normal'

    def get_image(self):
        self.image = self.spritesheet.get_sprite(0, self.get_state(), int(dimensions['cell_width']), int(dimensions['cell_height']))

    def draw(self, canvas, x, y):
        x_translated = x * dimensions["cell_width"] + dimensions['cell_translation']
        y_translated = y * dimensions['cell_height'] + dimensions['cell_translation']
        self.get_image()  # Make call to save image. Otherwise Garbage Collection will take it
        canvas.create_image(x_translated, y_translated, image=self.image, anchor=NW)

        if self.piece is not None:
            x_translated = x_translated + dimensions['piece_translation']
            y_translated = y_translated + dimensions['piece_translation']
            self.piece.draw(canvas, x_translated, y_translated, self.state, self.tile_color)

        self.reset_state()

    def get_save_data(self):
        if self.piece is not None:
            return self.piece.get_position() + ' ' + self.piece.get_color() + ' ' + str(self.piece.get_team()) + ' '\
                   + self.piece.get_name() + '\n'
        else:
            return ""

    def get_piece(self) -> object:
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_name(self):
        if self.highLighted and self.highLight_color == 'red':
            return "xx"
        if self.highLighted and self.highLight_color == 'yellow':
            return "yy"
        if self.piece is not None:
            return self.get_piece().get_abbr_name()
        return "--"
