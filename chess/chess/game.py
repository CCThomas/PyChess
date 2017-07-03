def start():
    print('==========================')
    print('Python 3 Chess Application')
    print('==========================')


#
# Developer Mode
#
def dev_quit():
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
