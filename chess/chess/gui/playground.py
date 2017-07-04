import os

# current_path = os.path.dirname(__file__) # Where your .py file is located
# resource_path = os.path.join(current_path, '../resources/images/board') # The resource folder path
# image_path = os.path.join(resource_path, 'board.png') # The image folder path
from chess.objects.pieces import Bishop
from chess.objects.board import Board
my_bis = Bishop('blue')
my_board = Board()

import tkinter as Tk
root = Tk.Tk()
canvas = Tk.Canvas(root)

background_image=Tk.PhotoImage(file=my_board.get_image_path())

bis_image=Tk.PhotoImage(file=my_bis.get_image_path())
canvas.pack(fill=Tk.BOTH, expand=1) # Stretch canvas to root window size.
image1 = canvas.create_image(0, 0, anchor=Tk.NW, image=background_image)
image2 = canvas.create_image(0, 0, anchor=Tk.NW, image=bis_image)
root.wm_geometry("800x800")
root.title('Map')
root.mainloop()