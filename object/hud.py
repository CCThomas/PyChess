from resources.globalvariables import dimensions
from object.spritesheet import Spritesheet
from object.tile import Tile
from tkinter import NW


class Hud:
    hud = [
        Tile('Hud'), Tile('Hud'), Tile('Hud'), Tile('Hud'), Tile('Hud'), Tile('Hud'), Tile('Hud'), Tile('Hud'),
        Tile('Hud')
    ]

    def __init__(self):
        self.hud_font = ("Purisa", 50)
        self.player_one = Spritesheet("piece/Hud-Spritesheet.png", 32, 32)
        self.player_two = Spritesheet("piece/Hud-Spritesheet.png", 32, 32)
        self.image_one = None
        self.image_two = None
        self.white_worth = "+00"
        self.back_worth = '+00'
        self.player_turn = 0
        self.player_in_check = 0
        for tile_num in range(8):
            if tile_num == 0:
                self.hud[tile_num].set_state('left')
            elif tile_num == 7:
                self.hud[tile_num].set_state('right')
            else:
                self.hud[tile_num].set_state('center')

    def set_player_turn(self, player_number):
        self.player_turn = player_number

    def set_player_in_check(self, player_number):
        self.player_in_check = player_number

    def set_worth(self, worth):
        if worth > 0:
            self.white_worth = "+" + str(worth)
            self.back_worth = "+00"
        elif worth < 0:
            self.white_worth = '+00'
            self.back_worth = "+" + str(abs(worth))
        else:
            self.white_worth = '+00'
            self.back_worth = '+00'

    def draw(self, canvas):
        # Draw Hud
        for tile_num in range(8):
            self.hud[tile_num].draw(canvas, tile_num, 8)

        # Draw Play One Stats
        canvas.create_text(10, dimensions['height'] - 100, text="P1", fill='white', font=self.hud_font,
                           anchor=NW)
        canvas.create_text(100, dimensions['height'] - 100, text=self.white_worth, fill='white', font=self.hud_font,
                           anchor=NW)

        # Draw Player Two Stats
        canvas.create_text(dimensions['width'] / 2, dimensions['height'] - 100, text="P2", fill='black',
                           font=self.hud_font, anchor=NW)
        canvas.create_text(dimensions['width'] / 2 + 100, dimensions['height'] - 100, text=self.back_worth,
                           fill='black', font=self.hud_font, anchor=NW)

        if self.player_turn == 1 and self.player_in_check == 1:
            self.image_one = self.player_one.get_sprite(0, 3, dimensions['hud_piece_size'],
                                                                    dimensions['hud_piece_size'])
        elif self.player_turn == 1:
            self.image_one = self.player_one.get_sprite(0, 1, dimensions['hud_piece_size'],
                                                    dimensions['hud_piece_size'])
        elif self.player_in_check == 1:
            self.image_one = self.player_one.get_sprite(0, 2, dimensions['hud_piece_size'],
                                                        dimensions['hud_piece_size'])
        else:
            self.image_one = self.player_one.get_sprite(0, 0, dimensions['hud_piece_size'],
                                                        dimensions['hud_piece_size'])

        if self.player_turn == 2 and self.player_in_check == 2:
            self.image_two = self.player_two.get_sprite(1, 3, dimensions['hud_piece_size'],
                                                                    dimensions['hud_piece_size'])
        elif self.player_turn == 2:
            self.image_two = self.player_two.get_sprite(1, 1, dimensions['hud_piece_size'],
                                                    dimensions['hud_piece_size'])
        elif self.player_in_check == 2:
            self.image_two = self.player_two.get_sprite(1, 2, dimensions['hud_piece_size'],
                                                        dimensions['hud_piece_size'])
        else:
            self.image_two = self.player_two.get_sprite(1, 0, dimensions['hud_piece_size'],
                                                        dimensions['hud_piece_size'])

        canvas.create_image(250, dimensions['height'] - 65, image=self.image_one)
        canvas.create_image(dimensions['width'] / 2 + 250, dimensions['height'] - 65,
                            image=self.image_two)
