import numpy as np


def time_shift(x, sample_rate, shift_seconds):
    """
    Shifts a signal in time by a given number of seconds.
    
    Parameters:
        x: input signal.
        sample_rate: sampling rate in samples per second.
        shift_seconds: amount of time to shift.
    
    Returns: the time-shifted signal.
    """
    n = len(x) 
    k = int(round(shift_seconds * sample_rate))
    if k == 0:
        return x.copy()
    if k > 0:
        return np.concatenate([np.zeros(k), x])[:n]
    else:
        k = -k
    return np.concatenate([x[k:], np.zeros(k)])[:n]

    
def time_scale(x, scale):
    """
    Scales a signal in time by a given factor.
    
    Parameters:
        x: input signal.
        scale: scaling factor.
        
    Returns: the time-scaled signal.
    """
    n = len(x)
    if n == 0:
        return x.copy()
    new_len = int(np.floor((n - 1) / scale)) + 1
    t_old = np.arange(n)
    t_new = np.arange(new_len)
    return np.interp(scale * t_new, t_old, x)

   
