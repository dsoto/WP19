import WP19_analysis as wpa
import numpy as np

def test_get_gaps_timestamp():
    energy_data = wpa.load_timeseries_file('test-clean.csv')
    gaps = wpa.get_gaps_timestamp(energy_data)
    assert len(gaps) == 2
    assert gaps[0] == np.timedelta64(5,'m')
    assert gaps[1] == np.timedelta64(4,'m')
