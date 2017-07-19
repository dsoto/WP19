# to run tests at command line   > pytest test.py

import WP19_analysis as wpa
import numpy as np
import pandas as pd

def test_get_gaps_timestamp():
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    gaps = wpa.get_gaps_timestamp(energy_data)
    # check number of gaps
    assert len(gaps) == 2
    # check length of gaps
    assert gaps[0] == np.timedelta64(5,'m')
    assert gaps[1] == np.timedelta64(4,'m')
    # check gap start times
    assert gaps.index[0] == pd.Timestamp('2017-01-01 00:05:00')
    assert gaps.index[1] == pd.Timestamp('2017-01-01 00:13:00')

def test_get_gaps_messages():
    message_data = wpa.load_message_file('test-messages.csv')
    gaps = wpa.get_gaps_messages(message_data)
    # check number of gaps
    assert len(gaps) == 2
    # check length of gaps
    assert gaps[0] == (np.timedelta64(4, 'm') + np.timedelta64(30, 's'))
    assert gaps[1] == (np.timedelta64(3, 'm') + np.timedelta64(30, 's'))
    # check gap start times
    assert gaps.index[0] == pd.Timestamp('2017-01-01 00:05:15')
    assert gaps.index[1] == pd.Timestamp('2017-01-01 00:13:15')

def test_create_uptime_boolean():
    # test creation of uptime booleans from the message file
    # verifies both in gap and out of gap samples
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    uptime_boolean = wpa.create_uptime_boolean(energy_data, message_data)
    assert uptime_boolean.iloc[4][0] == 1
    assert uptime_boolean.iloc[6][0] == 0
    assert uptime_boolean.iloc[9][0] == 0

def test_create_downtime_boolean_message():
    #import pdb; pdb.set_trace()
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    downtime_boolean = wpa.create_downtime_boolean_message(energy_data, message_data)
    assert downtime_boolean.iloc[5] == 0
    assert downtime_boolean.iloc[8] == 1
    assert downtime_boolean.iloc[13] == 0
    assert downtime_boolean.iloc[15] == 1




