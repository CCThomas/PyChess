import os
global run_log_file, pieces_test_log_file


def run_log(cmd,*argv):
    global run_log_file
    if cmd == 'close':
        run_log_file.close()
    elif cmd == 'open':
        current_path = os.path.dirname(__file__)
        run_log_path = os.path.join(current_path, 'logs/run_log')
        run_log_file = open(run_log_path, 'w')
    elif cmd == 'write':
        run_log_file.write(argv[0] + '\n')


def pieces_test_log(cmd,*argv):
    global pieces_test_log_file
    if cmd == 'close':
        pieces_test_log_file.close()
    elif cmd == 'open':
        current_path = os.path.dirname(__file__)
        run_log_path = os.path.join(current_path, 'logs/tests/pieces_test_log')
        pieces_test_log_file = open(run_log_path, 'w')
    elif cmd == 'write':
        pieces_test_log_file.write(argv[0] + '\n')