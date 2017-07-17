import numpy as np
import pandas as pd
from pint import UnitRegistry

raw_file_data = [{'files':['4. April/Data_Logs AJAU April 22 - 30.xls',
         '5. May/Data_Logs AJAU MAY.xls',
         '6. June/Data_Logs AJAU June.xls',
         '7. July/Data_Logs AJAU July.xls',
         '8. Agustus/Data_Logs Ajau Agustus.xls'
         ],
'skiprows':[32, 32, 32, 32, 32],
'output_file':'ajau.csv',
'village_name':'ajau'},
{'files':['4. April/Data_Logs ASEI April 22 - 30.xls',
         '5. May/Data_Logs ASEI MAY.xls',
         '6. June/Data_Logs ASEI June.xls',
         '7. July/Data_Logs ASEI July.xls',
         ],
'skiprows':[32, 32, 32, 32],
'output_file':'asei.csv',
'village_name':'asei'},
{'files':['4. April/Data_Logs ATAMALI 24 - 30.xls',
         '5. May/Data_Logs ATAMALI MAY.xls',
         '6. June/Data_Logs ATAMALI June.xls',
         '7. July/Data_Logs ATAMALI July.xls',
         '8. Agustus/Data_Logs Atamali Agustus.xls'
         ],
'skiprows':[32, 32, 24, 32, 32],
'output_file':'atamali.csv',
'village_name':'atamali'},
{'files':['4. April/Data_Logs AYAPO April 22 - 30.xls',
         '5. May/Data_Logs AYAPO MAY.xls',
         '6. June/Data_Logs AYAPO June.xls',
         '7. July/Data_Logs AYAPO July.xls',
         '8. Agustus/Data_Logs Ayapo Agustus.xls'
         ],
'skiprows':[32, 32, 32, 24, 24],
'output_file':'ayapo.csv',
'village_name':'ayapo'},
{'files':['5. May/Data_Logs KENSIO MAY.xls',
         '6. June/Data_Logs KENSIO June.xls',
         '7. July/Data_Logs KENSIO July.xls',
         '8. Agustus/Data_Logs Kensio Agustus.xls'
         ],
'skiprows':[32, 24, 32, 32, 32],
'output_file':'kensio.csv',
'village_name':'kensio'},
]

def load_message_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True)

def load_timeseries_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True)

def get_gaps_timestamp(energy_data):
    # returns a series of gap durations with the start time as index
    differences = np.diff(energy_data.index.values)
    gaps = pd.Series(index=energy_data.index[:-1], data=differences)
    gaps = gaps[gaps > np.timedelta64(1,'m')]
    return gaps

def get_gaps_messages(messages):
    # returns a series of gap durations with the start time as index
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return pd.Series(data = (power_up.index - power_down.index), index=power_down.index)

def get_total_duration(energy_data):
    return (energy_data.index[-1] - energy_data.index[0])/np.timedelta64(1, 'h')

def get_start_time(energy_data):
    return energy_data.index[0]

def get_end_time(energy_data):
    return energy_data.index[-1]

def calculate_uptime(energy_data):
    # take the discrete difference between time samples
    # convert to seconds from nanoseconds
    # put in pandas series
    differences = np.diff(energy_data.index.values)/1e9
    differences = differences.astype(int)
    diff_series = pd.Series(differences)

    # use value counts to see intervals
    dsvc = diff_series.value_counts()
    dsvc.sort_index()

    # intervals greater than 60 seconds are considered downtime
    cutoff_seconds = 60
    uptime = dsvc[dsvc.index <= cutoff_seconds]
    downtime = dsvc[dsvc.index > cutoff_seconds]

    # determine total downtime and uptime
    u = UnitRegistry()
    inferred_uptime = (uptime.index * uptime).values.sum() * u.second
    inferred_downtime = (downtime.index * downtime).values.sum() * u.second

    # use total observation period to get fraction of uptime
    clock_time = (energy_data.index[-1] - energy_data.index[0]).total_seconds() * u.seconds
    fraction_available = inferred_uptime / clock_time

    return fraction_available

def get_uptime_timestamps(energy_data):
    return calculate_uptime(energy_data)

def get_durations_messages(messages):
    return get_durations(messages)

def get_durations(messages):
    print('this is a deprecated function')
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return pd.DataFrame(data = {'durations':(power_up.index - power_down.index)/np.timedelta64(1, 'h')},
                        index=power_down.index)

def num_gaps_timestamp(energy_data):
    print('this is a deprecated function')
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return len(time_gaps[time_gaps > 60.0])

def num_gaps_messages(messages):
    print('this is a deprecated function')
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return len(power_down)

def num_gaps_timestamp(energy_data):
    # todo: use get_gaps_timestamp
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return len(time_gaps[time_gaps > 60.0])

def num_gaps_messages(messages):
    # todo: use get_gaps_messages
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return len(power_down)

def create_uptime_boolean(energy_data, messages):
    # todo: decide if this should be a deprecated function?
    index = pd.DatetimeIndex(start=get_start_time(energy_data),
                             end=get_end_time(energy_data),
                             freq='1T').values
    power_down = messages[messages['message']=='Power Down'].index.values
    power_up = messages[messages['message']=='Power Up'].index.values

    on = []
    for i in index:
        # if the insertion point of the index is one greater for the power_down time, you are in a gap
        if np.searchsorted(power_down, i) == np.searchsorted(power_up, i) + 1:
            on.append(0)
        else:
            on.append(1)

    return pd.DataFrame(index=index, data=on)

def create_downtime_boolean_message(energy_data, messages):
    # create boolean array of whether timestamp falls in recorded power gap
    # todo: create test function
    index = pd.DatetimeIndex(start=get_start_time(energy_data),
                             end=get_end_time(energy_data),
                             freq='1T').values
    power_down = messages[messages['message']=='Power Down'].index.values
    power_up = messages[messages['message']=='Power Up'].index.values

    downtime = []
    for i in index:
        # if the insertion point of the index is one greater for the power_down time, you are in a gap
        if np.searchsorted(power_down, i) == np.searchsorted(power_up, i) + 1:
            downtime.append(1)
        else:
            downtime.append(0)

    return pd.Series(index=index, data=downtime)

def create_uptime_boolean_timestamp(energy_data):
    # create boolean array of whether timestamp is during a valid power observation
    # todo: create test function
    acc_energy = energy_data['kWh export']
    rs_acc_energy = acc_energy.resample('1T').asfreq()
    boolean_uptime = (~rs_acc_energy.isnull()).astype(int)
    return boolean_uptime
