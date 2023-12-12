import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to compute Hopf fibration
def hopf_fibration(theta, phi):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z

# Generate theta and phi values
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)

theta, phi = np.meshgrid(theta, phi)

# Compute Hopf fibration
x, y, z = hopf_fibration(theta, phi)

# Plot the 3D sphere
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', alpha=0.6, edgecolors='k')

# Set axis properties
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Hopf Fibration - S^3 to S^2')

plt.show()
