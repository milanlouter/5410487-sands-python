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

    
    
# add function for time scale
def time_scale(x, scale):
    n = len(x)
    if n == 0:
        return x.copy
    new_len = int(np.floor((n - 1) / scale)) + 1
    t_old = np.arange(n)
    t_new = np.arange(new_len)
    return np.interp(scale * t_new, t_old, x)

   
