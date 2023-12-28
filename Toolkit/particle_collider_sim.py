import numpy as np
import matplotlib.pyplot as plt

class ParticleType:
    def __init__(self, mass, radius, color):
        self.mass = mass
        self.radius = radius
        self.color = color

class Particle:
    def __init__(self, particle_type, position, velocity, energy):
        self.particle_type = particle_type
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.energy = energy

def collide(particle1, particle2):
    # Elastic collision with energy conservation
    relative_position = particle2.position - particle1.position
    relative_velocity = particle2.velocity - particle1.velocity
    distance = np.linalg.norm(relative_position)
    
    if distance < particle1.particle_type.radius + particle2.particle_type.radius:
        normal = relative_position / distance
        relative_speed = np.dot(relative_velocity, normal)
        
        # Coefficient of restitution (elasticity)
        e = 0.8
        
        # Update velocities using elastic collision formula with energy conservation
        particle1.velocity += (2 * particle2.particle_type.mass / (particle1.particle_type.mass + particle2.particle_type.mass)) * relative_speed * normal * e
        particle2.velocity -= (2 * particle1.particle_type.mass / (particle1.particle_type.mass + particle2.particle_type.mass)) * relative_speed * normal * e

        # Update energies after collision
        particle1.energy = 0.5 * particle1.particle_type.mass * np.linalg.norm(particle1.velocity)**2
        particle2.energy = 0.5 * particle2.particle_type.mass * np.linalg.norm(particle2.velocity)**2

def initialize_particles(num_particles):
    particles = []
    for _ in range(num_particles):
        particle_type = ParticleType(mass=np.random.uniform(0.5, 2.0),
                                     radius=np.random.uniform(0.1, 0.5),
                                     color=np.random.rand(3))
        position = np.random.uniform(-10, 10, size=2)
        velocity_angle = np.random.uniform(0, 2 * np.pi)
        velocity_magnitude = np.random.uniform(1, 5)
        velocity = velocity_magnitude * np.array([np.cos(velocity_angle), np.sin(velocity_angle)])
        energy = 0.5 * particle_type.mass * velocity_magnitude**2
        particle = Particle(particle_type, position, velocity, energy)
        particles.append(particle)
    return particles

def simulate_collisions(particles, num_steps):
    for _ in range(num_steps):
        # Check for collisions
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                collide(particles[i], particles[j])
        
        # Update particle positions
        for particle in particles:
            particle.position += particle.velocity

def visualize_particles(particles):
    plt.figure(figsize=(8, 8))
    for particle in particles:
        plt.scatter(particle.position[0], particle.position[1], s=100 * particle.particle_type.radius, c=[particle.particle_type.color], label=f'Mass: {particle.particle_type.mass:.2f}, Radius: {particle.particle_type.radius:.2f}')
    
    plt.title('Particle Collisions Simulation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

# Example Usage
particles = initialize_particles(num_particles=5)

# Simulate collisions for 100 steps
simulate_collisions(particles, num_steps=100)

# Visualize the particles after collisions
visualize_particles(particles)
