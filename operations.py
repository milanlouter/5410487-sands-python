import numpy as np

# add time shift function
def time_shift(x, sample_rate, shift_seconds):
    n = len(x) 
    k = int(round(shift_seconds * sample_rate))
    if k == 0:
        return x.copy()
    if k > 0:
        return np.concatenate([np.zeros(k), x])[:n]
    else:
        k = -k
        return np.concatenate([x[k:], np.zeros(k)])[:n]
    