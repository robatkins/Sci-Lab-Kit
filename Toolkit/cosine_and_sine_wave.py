import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
duration = 10  # seconds
fps = 40  # frames per second
num_frames = duration * fps
t = np.linspace(0, duration, num_frames)
frequency_cosine = 1  # Hz
frequency_sine = 0.5  # Hz
amplitude = 1

# Function to generate cosine and sine wave data
def generate_wave_data(t, frequency, amplitude, wave_type):
    if wave_type == 'cosine':
        return amplitude * np.cos(2 * np.pi * frequency * t)
    elif wave_type == 'sine':
        return amplitude * np.sin(2 * np.pi * frequency * t)

# Create a figure and axis
fig, ax = plt.subplots()
line_cosine, = ax.plot([], [], lw=2, color='blue', label='Cosine Wave')
line_sine, = ax.plot([], [], lw=2, color='red', label='Sine Wave')
ax.legend()
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, duration)
ax.set_xticks([])  # Remove x-axis ticks for performance
ax.set_yticks([])  # Remove y-axis ticks for performance
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Cosine and Sine Wave Animation')  # Update the title

# Preallocate the line data to be updated
line_cosine_data = np.empty((num_frames, 2))
line_sine_data = np.empty((num_frames, 2))

# Animation function
def update(frame):
    y_cosine = generate_wave_data(t[:frame + 1], frequency_cosine, amplitude, 'cosine')
    y_sine = generate_wave_data(t[:frame + 1], frequency_sine, amplitude, 'sine')

    line_cosine_data[:frame + 1, 0] = t[:frame + 1]
    line_cosine_data[:frame + 1, 1] = y_cosine
    line_cosine.set_data(line_cosine_data[:frame + 1, 0], line_cosine_data[:frame + 1, 1])

    line_sine_data[:frame + 1, 0] = t[:frame + 1]
    line_sine_data[:frame + 1, 1] = y_sine
    line_sine.set_data(line_sine_data[:frame + 1, 0], line_sine_data[:frame + 1, 1])

    return line_cosine, line_sine

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=25)

# Use TkAgg backend for potential performance improvement
# plt.switch_backend('TkAgg')

# Show the plot
plt.show()
