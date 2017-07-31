# to run tests at command line   > pytest test.py

import WP19_analysis as wpa
import numpy as np
import pandas as pd

def test_get_gaps_timestamp():
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    gaps = wpa.get_gaps_timestamp(energy_data)
    # check number of gaps
    assert len(gaps) == 3
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
    # uses messages only to infer the state of the grid
    # test creation of uptime booleans from the message file
    # verifies both in gap and out of gap samples
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    uptime_boolean = wpa.create_uptime_boolean(energy_data, message_data)
    assert type(uptime_boolean) == pd.Series
    # the messages show down time between 5:15-9:45, 13:15-16:45
    # when uptime_boolean is 1, the grid is online
    assert uptime_boolean.iloc[4] == 1
    assert uptime_boolean.iloc[6] == 0
    assert uptime_boolean.iloc[9] == 0
    assert uptime_boolean.iloc[21] == 1

def test_create_downtime_boolean_message():
    # uses messages only to infer state of the grid
    # test creation of downtime booleans from the message file
    # verifies both in gap and out of gap samples
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    downtime_boolean = wpa.create_downtime_boolean_message(energy_data, message_data)
    assert type(downtime_boolean) == pd.Series
    # the messages show down time between 5:15-9:45, 13:15-16:45
    # when downtime_boolean is 1, the grid is offline
    assert downtime_boolean.iloc[5] == 0
    assert downtime_boolean.iloc[8] == 1
    assert downtime_boolean.iloc[13] == 0
    assert downtime_boolean.iloc[15] == 1

def test_create_uptime_boolean_timestamp():
    # uses timestamp only to infer state of the grid
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    uptime_boolean = wpa.create_uptime_boolean_timestamp(energy_data)
    assert type(uptime_boolean) == pd.Series
    # the timestamp file has no data between 5-10, 13-17, and 20-23
    # when uptime_boolean is 1, the grid is online
    assert uptime_boolean.iloc[4] == 1
    assert uptime_boolean.iloc[8] == 0
    assert uptime_boolean.iloc[12] == 1
    assert uptime_boolean.iloc[21] == 0

def test_insert_power_gap_zeros():
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    gap_zeros = wpa.insert_power_gap_zeros(energy_data, message_data)
    # when gap_zeros is >0 there is a difference of power from the previous minute
    assert gap_zeros.iloc[9] == 0
    assert gap_zeros.iloc[10] == 2
    assert gap_zeros.iloc[11] == 0
    assert gap_zeros.iloc[12] == 1
    assert gap_zeros.iloc[13] == 0

def test_insert_zeros_kVA():
    message_data = wpa.load_message_file('test-messages.csv')
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    insert_zeros = wpa.insert_zeros_kVA(energy_data, message_data)
    assert type(insert_zeros) == pd.DataFrame
    # rows 5, 6 and 9, 10 are on the boundaries of a gap
    assert insert_zeros.iloc[5][9] == 2
    assert insert_zeros.iloc[6][9] == 0
    assert insert_zeros.iloc[9][9] == 0
    assert insert_zeros.iloc[10][9] == 2