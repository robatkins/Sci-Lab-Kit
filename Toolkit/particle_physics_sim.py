import matplotlib.pyplot as plt
import numpy as np

def plot_particle_interaction(particle_type, energy):
    # Plot the particle interaction point
    plt.scatter(0, 0, marker='o', color='blue', label=f'{particle_type} Interaction')

    # Plot the detector geometry
    detector_radius = 5
    theta = np.linspace(0, 2*np.pi, 100)
    detector_x = detector_radius * np.cos(theta)
    detector_y = detector_radius * np.sin(theta)
    plt.plot(detector_x, detector_y, color='black', label='Detector Geometry')

    plt.title(f'{particle_type} Interaction at Energy {energy} GeV')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
plot_particle_interaction('Muon', 10)
