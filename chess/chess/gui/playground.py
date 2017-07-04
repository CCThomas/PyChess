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
canvas.pack(fill=Tk.BOTH, expand=1)
root.wm_geometry(dimensions["geometry"])
root.title('PyChess')
root.mainloop()