test_num = 0
fail_num = 0


def print_and_close_report():
    print("Number of Test: " + str(test_num))
    print("Failures ---->: " + str(fail_num))
    print("Closing Report...")


def should_equal(testing, variable, control):
    global fail_num, test_num
    test_num = test_num + 1
    if variable == control:
        pass
    else:
        fail_num = fail_num + 1
        print(testing + " Failed!")
        print(str(variable) + " SHOULD EQUAL " + str(control))


def should_not_equal(testing, variable, control):
    global fail_num, test_num
    test_num = test_num + 1
    if variable != control:
        pass
    else:
        fail_num = fail_num + 1
        print(testing + " Failed!")
        print(str(variable) + " SHOULD NOT EQUAL " + str(control))


def start_report(testing):
    print("Starting Test Report on " + testing)
    global fail_num, test_num
    test_num = 0
    fail_num = 0