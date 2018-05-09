#!/usr/bin/env python
# Simple REST API to execute a series of tests and return a boolean value

from lib import testUtils
from tests.common import panic_flag
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    current_panic_state = panic_flag.check_panic_flag()
    return render_template('index.html', title='GONOGO', panic=current_panic_state)


@app.route('/api/v0.1/checkDevice/<string:device_id>', methods=['GET'])
def get_device_status(device_id):
    print 'Here we go!'
    test_list = testUtils.get_tests_for_device(device_id)

    for test in test_list:
        print 'Checking test %s for device_id %s' % (test, device_id)
        if not testUtils.execute_test(test, device_id):
            print 'Test %s for device_id %s FAILED' % (test, device_id)
            return "NOT-HOTDOG"

    print 'All systems Go!'
    return "HOTDOG"


@app.route('/api/v0.1/disablePanic')
def disable_panic():
    panic_flag.clear_panic_flag()
    current_panic_state = False
    return render_template('index.html', title='GONOGO', panic=current_panic_state)


@app.route('/api/v0.1/enablePanic')
def enable_panic():
    panic_flag.set_panic_flag()
    current_panic_state = True
    return render_template('index.html', title='GONOGO', panic=current_panic_state)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
