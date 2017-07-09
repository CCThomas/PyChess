dimensions = {
    "geometry": "600x600",
    "cell_width": 600/8,
    "cell_height": 600/8,
    "piece_size": int(600/8),
    "piece_translation": int(600/8)*.5
}

def start():
    print('==========================')
    print('Python 3 Chess Application')
    print('==========================')


#
# Developer Mode
#
def dev_quit():
    from chess.io import output
    output.run_log("close")
    import sys
    sys.exit(0)


def dev_test():
    from chess.test import console
    console.start()


def dev_usage():
    print('"quit" -> Quits Program')
    print('"test" -> Run Testing Console')


commands = {
    'help': dev_usage,
    'quit': dev_quit,
    'test': dev_test
}


def dev_console():
    print('==========================')
    print('Python 3 Chess Application')
    print('      Developer Mode')
    print('==========================')

    while True:
        user_input = input("> ")
        if user_input in commands:
            commands[user_input]()
        else:
            print('type "help" to print usage')
