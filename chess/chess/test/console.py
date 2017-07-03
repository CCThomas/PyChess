def test_board():
    from chess.objects.board import Board
    my_board = Board()

def test_quit():
    import sys
    sys.exit(0)

def test_usage():
    print('"board"  -> Test Board')
    print('"return" -> Return to Game Console')
    print('"quit"   -> Quits Program')
    print('"test"   -> Run Testing Console')


commands = {
    'board': test_board,
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
