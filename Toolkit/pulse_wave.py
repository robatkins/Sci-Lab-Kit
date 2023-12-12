import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
duration = 10  # seconds
fps = 40  # frames per second
num_frames = duration * fps
t = np.linspace(0, duration, num_frames)
frequency = 1  # Hz
amplitude = 1

# Function to generate pulse wave data
def generate_pulse_wave(t, frequency, amplitude):
    period = 1 / frequency
    pulse_width = 0.5  # Adjust the pulse width as needed
    signal = amplitude * np.where((t % period) < pulse_width * period, 1, -1)
    return signal

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, duration)
ax.set_xticks([])  # Remove x-axis ticks for performance
ax.set_yticks([])  # Remove y-axis ticks for performance
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Pulse Wave Animation')  # Update the title

# Preallocate the line data to be updated
line_data = np.empty((num_frames, 2))

# Animation function
def update(frame):
    y = generate_pulse_wave(t[:frame + 1], frequency, amplitude)
    line_data[:frame + 1, 0] = t[:frame + 1]
    line_data[:frame + 1, 1] = y
    line.set_data(line_data[:frame + 1, 0], line_data[:frame + 1, 1])
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=25)

# Use TkAgg backend for potential performance improvement
# plt.switch_backend('TkAgg')

# Create a separate figure for the GUI window and set its title
plt.figure(1).canvas.setWindowTitle('Pulse Wave Animation')

# Show the plot
plt.show()
