from resources.globalvariables import dimensions, TITLE, VERSION_NUMBER
from tkinter import Canvas, BOTH, Label, Button
from object.board import Board
import tkinter as Tk


class Window:
    def __init__(self):
        """Initialize PyConsole Window"""
        self.master = Tk.Tk()
        self.master.wm_geometry(dimensions["geometry"])

        x = (self.master.winfo_screenwidth() / 2) - (dimensions['width'] / 2)
        y = (self.master.winfo_screenheight() / 2) - (dimensions['height'] / 2)
        self.master.geometry('+%d+%d' % (x, y))

        self.master.title('PyChess')
        self.master.resizable(False, False)

        self.master.home_command_pressed = self.home_command_pressed
        self.master.quit_command_pressed = self.quit_command_pressed

        # Menu Bar
        self.menubar = None
        self.init_menubar()

        # Start Window
        self.start_window = None
        self.init_start_window()

        # Chess Board
        self.chess_board = None

        # Status Bar
        self.status_bar = None
        self.init_status_bar()

    def init_menubar(self):
        """Initialize Menu Bar"""
        file_commands = [
            {
                'type': 'command',
                'label': 'Home',
                'command': self.home_command_pressed
            },
            {
                'type': 'command',
                'label': 'Quit',
                'command': self.quit_command_pressed
            }
        ]
        chess_commands = self.get_chess_basic_commands()
        self.menubar = MenuBar(self.master)
        self.menubar.add_menu(self.master, 'File', file_commands)
        self.menubar.add_menu(self.master, 'Chess', chess_commands)
        self.master.config(menu=self.menubar.get())

    def get_chess_basic_commands(self):
        """Get the Basic commands for the Chess Menu Bar"""
        return [
            {
                'type': 'command',
                'label': 'New Game',
                'command': self.new_game_button_pressed
            },
            {
                'type': 'command',
                'label': 'Load',
                'command': self.load_game_pressed
            }
        ]

    def init_start_window(self):
        """Initialize Start Window"""
        self.start_window = StartWindow(self)

    def init_status_bar(self):
        """Initialize Status Bar"""
        self.status_bar = StatusBar(self.master)
        self.status_bar.set("%s", TITLE + " " + VERSION_NUMBER)
        self.status_bar.pack(side=Tk.BOTTOM, fill=Tk.X)

    def home_command_pressed(self):
        """Called When Home Button is Pressed, called from menubar"""
        self.chess_board.pack_forget()
        self.start_window.pack_forget()
        self.menubar.remove_excess_menus()
        self.init_start_window()

    def new_game_button_pressed(self, is_new_game=True):
        """Initialize a New Chess Game"""
        self.start_window.pack_forget()
        if self.chess_board is not None:
            self.chess_board.pack_forget()
        self.chess_board = ChessBoard(self.master)
        if is_new_game:
            self.chess_board.init_players()
            self.chess_board.draw()
        commands = self.get_chess_basic_commands()
        commands.append({
            'type': 'command',
            'label': 'Save Game',
            'command': self.save_game_pressed
        })
        self.menubar.replace_menu(self.master, 'Chess', commands, 1)

    def quit_command_pressed(self):
        """"Quits Program"""
        self.master.quit()

    def mainloop(self):
        """Main Loop for Program"""
        self.master.mainloop()

    def save_game_pressed(self):
        print("Coming Soon...")

    def load_game_pressed(self):
        print("Coming Soon...")


class MenuBar:
    def __init__(self, master):
        """Initialize MenuBar"""
        self.menubar = Tk.Menu(master)

    def add_menu(self, master, menu_name, commands):
        """Add new Menu to Menu Bar"""
        my_menu = Tk.Menu(master, tearoff=0)
        for command in commands:
            if command['type'] == 'add_separator':
                my_menu.add_separator()
            else:
                my_menu.add_command(label=command['label'], command=command['command'])
        self.menubar.add_cascade(label=menu_name, menu=my_menu)

    def get(self):
        """Return the MenuBar"""
        return self.menubar

    def remove_excess_menus(self):
        """Remove Additional Menu"""
        self.menubar.delete(1)

    def replace_menu(self, master, menu_name, commands, index):
        """Replaces a Menu with a new drop down Menu"""
        self.menubar.delete(index)
        self.add_menu(master, menu_name, commands)


class StartWindow(Tk.Frame):
    def __init__(self, window):
        """Initialize Chess Menu
        :param window: PyConsole Window
        """
        self.title = Label(window.master, text="PyChess", font=("Helvetica", 50))
        self.new_game_button = Button(window.master, width=8,
                                      text="New Game", fg="red",
                                      command=window.new_game_button_pressed)
        self.load_game_button = Button(window.master, width=8,
                                       text="Load Game", fg="red",
                                       command=window.load_game_pressed)
        self.quit_game_button = Button(window.master, width=8,
                                       text="Quit Game", fg="red",
                                       command=window.master.quit_command_pressed)
        self.title.pack(pady=50)
        self.new_game_button.pack()
        self.load_game_button.pack()
        self.quit_game_button.pack()

    def pack_forget(self):
        """Erase Chess Menu"""
        self.title.pack_forget()
        self.new_game_button.pack_forget()
        self.load_game_button.pack_forget()
        self.quit_game_button.pack_forget()


class StatusBar(Tk.Frame):
    def __init__(self, master):
        """Initialize the Status Bar"""
        Tk.Frame.__init__(self, master)
        self.label = Tk.Label(self, bd=1, relief=Tk.SUNKEN, anchor=Tk.W)
        self.label.pack(fill=Tk.X)

    def set(self, format, *args):
        """Set the Status Bar text"""
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        """Clear the Status Bar"""
        self.label.config(text="")
        self.label.update_idletasks()


class ChessBoard:
    def __init__(self, master):
        """Initialize Chess Board"""
        self.canvas = Canvas(master)
        self.my_board = Board()

        def callback(event):
            """Method Called with ChessBoard is Clicked"""
            self.my_board.clicked(event.x, event.y)
            self.my_board.check_for_check()
            self.my_board.draw(self.canvas)

        self.canvas.bind("<Button-1>", callback)

        self.canvas.pack(fill=BOTH, expand=1)

    def pack_forget(self):
        """Erase Chess Board"""
        self.canvas.pack_forget()
        self.my_board = Board()

    def init_players(self):
        """Initialize Chess Pieces"""
        self.my_board.init_player_pieces('white', 1)
        self.my_board.init_player_pieces('black', 2)

    def draw(self):
        """Draw Chess board"""
        self.my_board.draw(self.canvas)

    def get_save_data(self):
        """Get Save Data from Chess Board: Draft"""
        pass
        """
        return self.my_board.get_save_data()
        """

    def place_piece(self, piece_name, piece_team, piece_color, letter, number):
        """Place Piece on Board: Draft for Loading Game"""
        pass
        """
        piece = self.my_board.create_piece_with_name(piece_name, piece_color, piece_team)
        self.my_board.place_piece(piece, letter, number)
        """
