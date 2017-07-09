from chess.io import output

test_num = 0
fail_num = 0


def start_report(testing):
    output.pieces_test_log('open')
    output.pieces_test_log('write', "Starting Testing " + testing)
    print("Starting Testing " + testing)


def close_report(testing):
    output.pieces_test_log('write', 'Testing for ' + testing + " is Done!")
    print('Testing for ' + testing + " is Done!")
    output.pieces_test_log('close')


def print_and_restart_tracker():
    output.pieces_test_log('write', "Number of Test: " + str(test_num))
    output.pieces_test_log('write', "Failures ---->: " + str(fail_num))
    print("Number of Test: " + str(test_num))
    print("Failures ---->: " + str(fail_num))


def should_equal(testing, variable, control):
    global fail_num, test_num
    test_num = test_num + 1
    if variable == control:
        pass
    else:
        fail_num = fail_num + 1
        output.pieces_test_log('write', testing + " Failed!")
        output.pieces_test_log('write', str(variable) + " SHOULD EQUAL " + str(control))
        print(testing + " Failed!")
        print(str(variable) + " SHOULD EQUAL " + str(control))


def start_test_on(testing):
    output.pieces_test_log('write', "Starting Test on " + testing)
    print("Starting Test on " + testing)
    global fail_num, test_num
    test_num = 0
    fail_num = 0
