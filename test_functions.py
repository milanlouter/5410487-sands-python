import numpy as np
from signals import generate_sine_wave, generate_step_function
from operations import time_shift, time_scale

def test_sine_wave():
    """
    Test that sine wave has correct length and stays witihin range.
    """
    fs, dur, f = 100, 1.0, 5
    x = generate_sine_wave(f, dur, fs)
    assert len(x) == fs * dur
    assert np.all(np.abs(x) <= 1.0)

def test_step_function():
    """
    Test that step function goes from 0 to 1 at the right time.
    """
    fs, dur, t0 = 100, 1.0, 0.5
    x = generate_step_function(t0, dur, fs)
    idx = int(t0 * fs)
    assert np.all(x[:idx] == 0)
    assert np.all(x[idx:] == 1)

def test_shift():
    """
    Test that the time shift operation delays the signal and keeps same length
    """
    fs, dur = 100, 1.0
    x = generate_step_function(0.3, dur, fs)
    y = time_shift(x, fs, 0.2)
    assert len(x) == len(y)
    assert np.argmax(np.diff(y)) > np.argmax(np.diff(x))

def test_scale():
    """
    Test that time scale operation streches and ciompresses the signal right
    """
    fs, dur = 100, 1.0
    x = generate_sine_wave(5, dur, fs)
    y = time_scale(x, 0.5)
    z = time_scale(x, 2.0)
    assert len(y) > len(x)
    assert len(z) < len(x)
