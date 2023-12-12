import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.linspace(0, 1, 1000)

# Sine wave
sin_wave = np.sin(2 * np.pi * t)

# Square wave
square_wave = np.sign(np.sin(2 * np.pi * t))

# Triangle wave
triangle_wave = 2 * np.abs(t - np.round(t))

# Sawtooth wave
sawtooth_wave = 2 * (t - np.floor(t + 0.5))

# Pulse wave with 25% duty cycle
duty_cycle = 0.25
pulse_wave = np.where(t % 1 < duty_cycle, 1, 0)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 2, 1)
plt.plot(t, sin_wave)
plt.title('Sine Wave')

plt.subplot(3, 2, 2)
plt.plot(t, square_wave)
plt.title('Square Wave')

plt.subplot(3, 2, 3)
plt.plot(t, triangle_wave)
plt.title('Triangle Wave')

plt.subplot(3, 2, 4)
plt.plot(t, sawtooth_wave)
plt.title('Sawtooth Wave')

plt.subplot(3, 2, 5)
plt.plot(t, pulse_wave)
plt.title('Pulse Wave')

plt.tight_layout()
plt.show()
