import matplotlib.pyplot as plt

#import signals and operations
from signals import generate_sine_wave, generate_step_function
from operations import time_shift, time_scale

#plot functions + after operations
fs = 100 
dur = 1.0
sine = generate_sine_wave(5, dur, fs)
step = generate_step_function(0.5, dur, fs)

sine_shifted = time_shift(sine, fs, 0.3)

step_scaled  = time_scale(step, 0.2)

plt.figure()
plt.plot(t, sine, label='sine')
plt.plot(t, sine_shifted, '--', label='sine shifted')
plt.legend(); plt.grid(); plt.title('Sine wave shifted')

plt.figure()
plt.plot(tp, step, label='step')
plt.plot(tps, step_scaled, ':', label='step scaled')
plt.legend(); plt.grid(); plt.title('Step function scaled')


