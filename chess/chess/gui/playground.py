import os

# current_path = os.path.dirname(__file__) # Where your .py file is located
# resource_path = os.path.join(current_path, '../resources/images/board') # The resource folder path
# image_path = os.path.join(resource_path, 'board.png') # The image folder path
"""from chess.objects.pieces import Bishop
from chess.objects.board import Board
my_bis = Bishop('blue')
my_board = Board()"""

import tkinter as Tk
from chess.objects.board import Board
from chess.game import dimensions



root = Tk.Tk()
canvas = Tk.Canvas(root)
my = Board()
my.init_player('blue',1)
my.print_board()
my.draw_board(canvas)

def callback(event):
    print("clicked at", event.x, event.y)
canvas.bind("<Button-1>", callback)

canvas.pack(fill=Tk.BOTH, expand=1)
root.wm_geometry(dimensions["geometry"])
root.title('PyChess')
root.mainloop()


"""
BOARD CODE
current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(current_path, '../resources/images/board/board.png')
    def print_board(self):
        print('  A B C D E F G H')
        for row in range(0,8):
            print(row+1, end=' ')
            for column in range(0,8):
                if self.board_piece[row][column] is not None:
                    print(self.board_piece[row][column].get_name(), end=' ')
            print('')

    def draw_board(self,canvas):
        from chess.game import dimensions
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    canvas.create_rectangle(col * dimensions["cell_width"], row * dimensions['cell_height'], (col + 1) * dimensions['cell_width'],
                                            (row + 1) * dimensions['cell_height'], fill='black')
                else:
                    canvas.create_rectangle(col * dimensions["cell_width"], row * dimensions['cell_height'],
                                            (col + 1) * dimensions['cell_width'],
                                            (row + 1) * dimensions['cell_height'], fill='gray')


                if self.board_piece[row][col] is not None:
                    self.board_piece[row][col].draw_piece(canvas, row, col)

"""
"""
Piece Code
    def draw_piece(self, canvas, letter, number):
        from chess.game import dimensions
        canvas.create_text(number * dimensions["cell_width"] + dimensions['piece_translation'],
                           letter * dimensions['cell_height'] + dimensions['piece_translation'],
                           text=self.name, font=('Helvetica', dimensions['piece_size']),
                           fill=self.color, activefill='white')
"""