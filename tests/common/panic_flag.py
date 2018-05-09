import os

PANIC_FILE = '/tmp/go-no-go_panic'


def execute(device_id):
    """
    Mandatory function to execute this test
    :param device_id: hostname or id of the device in question
    :return: boolean if tests may continue
    """
    print 'running test %s for device_id: %s' % (__name__, device_id)
    return check_panic_flag()


def check_panic_flag():
    if not os.path.exists(PANIC_FILE):
        open(PANIC_FILE, 'w').close()

    with open(PANIC_FILE, 'r') as f:
        contents = f.readline()
        print 'panic file contents are:'
        print contents
        if 'panic' in contents:
            return False

    return True


def set_panic_flag():
    with open(PANIC_FILE, 'w') as f:
        f.write('panic')


def clear_panic_flag():
    with open(PANIC_FILE, 'w') as f:
        f.write('')
