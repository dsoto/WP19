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

def get_gaps_messages(messages):
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return pd.Series(data = (power_up.index - power_down.index), index=power_down.index)

def load_message_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True)

def load_timeseries_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True)

def get_total_duration(observations):
    return (observations.index[-1] - observations.index[0])/np.timedelta64(1, 'h')

def num_gaps_timestamp(energy_data):
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return len(time_gaps[time_gaps > 60.0])

def num_gaps_messages(messages):
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
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return len(time_gaps[time_gaps > 60.0])

def num_gaps_messages(messages):
    power_down = messages[messages['message']=='Power Down']
    power_up = messages[messages['message']=='Power Up']

    # first message should be a power down
    assert (power_down.index[0] < power_up.index[0]), 'first message not power down'
    # last message should be a power up
    assert (power_down.index[-1] < power_up.index[-1]), 'last message not power up'
    # should be same number of up and down messages
    assert (len(power_down) == len(power_up)), 'unequal up and down messages'

    return len(power_down)

def get_downtime_timestamps(energy_data):
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return time_gaps[time_gaps > 60.0].sum()

def get_gaps_timestamp(energy_data):
    time_gaps = np.diff(energy_data.index.values) / np.timedelta64(1,'s')
    time_gaps = pd.Series(time_gaps)
    return time_gaps[time_gaps > 60.0]
