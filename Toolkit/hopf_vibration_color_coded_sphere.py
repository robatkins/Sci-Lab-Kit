import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def hopf_map(theta, phi):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    w = np.sin(2 * theta)
    return x, y, z, w

def animate(frame):
    ax.cla()  # Clear previous frame
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    theta = np.linspace(0, 2 * np.pi, 100)
    phi = frame * 0.02

    x, y, z, w = hopf_map(theta, phi)

    # Use a colormap to get different colors at each frame
    color = plt.cm.viridis(frame / num_frames)

    ax.plot(x, y, z, label='Hopf Vibration', color=color)
    ax.scatter(x, y, z, color=color)

    # Retain the visual history by plotting previous frames
    for i in range(frame):
        prev_phi = i * 0.02
        prev_x, prev_y, prev_z, _ = hopf_map(theta, prev_phi)
        ax.plot(prev_x, prev_y, prev_z, color=plt.cm.viridis(i / num_frames), alpha=0.3)
        ax.scatter(prev_x, prev_y, prev_z, color=plt.cm.viridis(i / num_frames), alpha=0.3)

    ax.set_title('Animated Hopf Vibration')
    ax.legend()

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the number of frames in the animation
num_frames = 200

# Create the animation
animation = FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=False)

# Uncomment the line below to save the animation as a gif
# animation.save('hopf_vibration.gif', writer='imagemagick', fps=30)

# Display the animation
plt.show()

