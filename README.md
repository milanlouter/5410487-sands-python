# Signal operations project S&S

## Introduction
The project in this repository demonstrates generating simple signals and applying time-domain operations on those using Python, Numpy, and Matplotlib.

## Files
### signals.py
Contains two signal generators:
- generate_sine_wave(frequency, duration, sample_rate) -> creates a sine wave.
- generate_step_function(step_time, duration, sample_rate) –> creates a step signal.

### operations.py
Contains two signal operations:
- time_shift(x, sample_rate, shift_seconds) –> shifts a signal forward/backward in time.
- time_scale(x, scale) –> stretches/compresses a signal in time.

### run.py
The main script that:
1. Generates a sine wave and a step function.
2. Applies shifting to the sine wave and scaling to the step function.
3. Plots the original and transformed signals.

## How to use
1. make sure that python, numpy and matplotlib are installed:
pip install numpy matplotlib

2. run the project
python run.py

3. the program will open plots:
- original sine wave and time shifted version
- origninal step signal and time scaled version

