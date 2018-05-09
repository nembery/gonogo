import importlib
import os


def get_tests_for_device(device_id):
    """
    simple function to return a list of tests to be executed for a given device_id
    :param device_id: hostname or id of the device in question
    :return: List of test names to execute
    """

    # test_list = ['common.panic_flag', 'common.local_device_cache']
    test_list = __get_common_tests()
    print 'returning tests for device: %s' % device_id
    # TODO - add additional tests here

    return test_list


def execute_test(test_name, device_id):
    """
    execute a test and return the results. Each test is assumed to be a simple python script
    :param test_name: name of the script to execute
    :param device_id: hostname of id of the device id to use as a parameter
    :return: boolean value if tests / automation may continue
    """

    # default return value
    # TODO - should we always just default to allowing tests to continue in the event of error / exception?
    default_return = False
    
    try:
        test = importlib.import_module("tests.%s" % test_name)
        print test
        if hasattr(test, 'execute'):
            return test.execute(device_id)
        else:
            print dir(test)
            print 'module %s does NOT have an execute function!!!' % test_name
            return default_return
        
    except Exception as e:
        print 'Could not execute test: %s - Error was %s' % (test_name, e)
        return default_return

    return default_return

    
def __get_common_tests():
    """
    Check the common directory and return a list all all modules that are present there
    :return: list of modules to execute for EVERY device in the form ['common.panic_flag', 'common.local_device_cache']
    """
    common_tests = list()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.abspath(os.path.join(current_dir, '../tests/common'))
    all_files = os.listdir(test_dir)
    for f in all_files:
        if 'pyc' not in f and '__init__' not in f:
            test_name = f.replace('.py', '')
            common_tests.append('common.%s' % test_name)

    return common_tests


