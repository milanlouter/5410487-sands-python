import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """ 
    Generates a sine wave signal
    
    Parameters:
        frequency: frequency of the sine wave in Hz.
        duration: duration of the signal in seconds.
        sample_rate: sampling rate in samples per second.
    
    Returns: the generated sine wave signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal


def generate_step_function(step_time, duration, sample_rate):
    """ 
    Generates a step function signal
    
    Parameters:
        step_time: time at which the step occurs in seconds.
        duration: duration of the signal in seconds.
        sample_rate: sampling rate in samples/second.
        
    Returns: the generated step signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)
    signal[t >= step_time] = 1.0
    return signal



