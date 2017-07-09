def test_board():
    from chess.objects.board import Board,Player
    my_board = Board()
    player_1 = Player('red')
    player_1.init_pieces("north")
    player_2 = Player('blue')
    player_2.init_pieces('south')

    p1_pieces = player_1.get_pieces()
    for piece in p1_pieces:
        my_board.place_piece(p1_pieces[piece].get_name(), p1_pieces[piece].get_letter(),
                             p1_pieces[piece].get_number())


    p2_pieces = player_2.get_pieces()
    for piece in p2_pieces:
        my_board.place_piece(p2_pieces[piece].get_name(), p2_pieces[piece].get_letter(),
                                 p2_pieces[piece].get_number())

    my_board.print_board()

def test_game():
    from chess.game import play
    play.init_game()

def test_gui():
    from chess.gui import playground

def test_pieces():
    from chess.test import pieces
    pieces.test_pieces()

def test_player():
    from chess.objects import player
    player_one = player.Player()

def test_quit():
    from chess.io import output
    output.run_log("close")
    import sys
    sys.exit(0)

def test_usage():
    print('"board"  -> Test Board')
    print('"game"   -> Test Game')
    print('"player"   -> Test Player')
    print('"return" -> Return to Game Console')
    print('"quit"   -> Quits Program')
    print('"test"   -> Run Testing Console')


commands = {
    'board': test_board,
    'game': test_game,
    'gui': test_gui,
    'pieces': test_pieces,
    'player': test_player,
    'help': test_usage,
    'quit': test_quit
}

def start():
    print('Testing Console')
    while True:
        user_input = input("> ")
        if user_input in commands:
            commands[user_input]()
        elif user_input == 'return':
            print('returning to dev console...')
            break
        else:
            print('type "help" to print usage')
