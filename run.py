import matplotlib.pyplot as plt

from signals import generate_sine_wave
sine_wave = generate_sine_wave(frequency=5, duration=2, sample_rate=100)

plt.plot(sine_wave)

