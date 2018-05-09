import os
import yaml

cache_file = '/tmp/go-no-go_cache.yaml'


def execute(device_id):
    """
    Mandatory function to execute this test
    :param device_id: hostname or id of the device in question
    :return: boolean if tests may continue
    """
    print 'running test %s for device_id: %s' % (__name__, device_id)
    return check_device_cache(device_id)


def check_device_cache(device_id):
    """
    Check whether a device is in the device list cache
    :param device_id: the device name or id of the device in question
    :return: boolean if device is in the list
    """

    device_list = __get_device_list_from_cache()

    if device_id in device_list:
        print 'Found device id in the maintenance local cache!'
        return False

    # default return value
    return True


def __get_device_list_from_cache():

    if not os.path.exists(cache_file):
        open(cache_file, 'w').close()

    device_list = list()
    with open(cache_file, 'r') as f:
        try:
            device_list = yaml.load(f)
            if device_list is None:
                return list()
        except ValueError as ve:
            print 'Could not parse yaml file!'

    print 'device list is:'
    print device_list
    print '^^^'

    return device_list

