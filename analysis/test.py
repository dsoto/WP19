# to run tests at command line   > pytest test.py

import WP19_analysis as wpa
import numpy as np

def test_get_gaps_timestamp():
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    gaps = wpa.get_gaps_timestamp(energy_data)
    assert len(gaps) == 2
    assert gaps[0] == np.timedelta64(5,'m')
    assert gaps[1] == np.timedelta64(4,'m')
    # TODO: test that gaps have the correct start date

def test_get_gaps_messages():
    pass
    # TODO test that messages function gives correct results


def test_create_uptime_boolean():
    # test creation of uptime booleans from the message file
    # verifies both in gap and out of gap samples
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    uptime_boolean = wpa.create_uptime_boolean(energy_data, message_data)
    assert uptime_boolean.iloc[4][0] == 1
    assert uptime_boolean.iloc[6][0] == 0
    assert uptime_boolean.iloc[9][0] == 0



