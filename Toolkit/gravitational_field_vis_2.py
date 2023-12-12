import pygame
import math

# Pygame setup
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 1200
FPS = 60

# Particle properties
particle1_pos = [WIDTH // 4, HEIGHT // 2]
particle1_mass = 1

particle2_pos = [3 * WIDTH // 4, HEIGHT // 2]
particle2_mass = 2  # Making particle2 more massive

# Function to calculate gravitational field at a given point due to a massive particle
def calculate_gravitational_field(mass, position, observation_point):
    G = 6.67430e-11  # Gravitational constant
    distance = math.sqrt((observation_point[0] - position[0])**2 + (observation_point[1] - position[1])**2)

    if distance == 0:
        return [0, 0]  # Avoid division by zero

    inverse_square_distance = 1 / distance**2
    magnitude = G * mass * inverse_square_distance
    direction = [(position[i] - observation_point[i]) for i in range(2)]  # Reverse direction

    gravitational_field = [magnitude * direction[0], magnitude * direction[1]]
    return gravitational_field

# Function to calculate the total gravitational field at a given point due to two massive particles
def calculate_total_gravitational_field(observation_point):
    field1 = calculate_gravitational_field(particle1_mass, particle1_pos, observation_point)
    field2 = calculate_gravitational_field(particle2_mass, particle2_pos, observation_point)

    total_field = [field1[0] + field2[0], field1[1] + field2[1]]
    return total_field

# Function to draw an arrow on the screen
def draw_arrow(screen, color, start_pos, end_pos):
    pygame.draw.line(screen, color, start_pos, end_pos, 2)
    angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
    end_arrow = (end_pos[0] - 10 * math.cos(angle - math.pi / 6), end_pos[1] - 10 * math.sin(angle - math.pi / 6))
    pygame.draw.line(screen, color, end_pos, end_arrow, 2)
    end_arrow = (end_pos[0] - 10 * math.cos(angle + math.pi / 6), end_pos[1] - 10 * math.sin(angle + math.pi / 6))
    pygame.draw.line(screen, color, end_pos, end_arrow, 2)

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))  # Increased height for two sliders
pygame.display.set_caption("Gravitational Field Visualization")
clock = pygame.time.Clock()

# Font for text
font = pygame.font.Font(None, 36)

# Slider properties for Particle 1
slider1_rect = pygame.Rect(10, HEIGHT + 10, WIDTH - 20, 20)
slider1_color = (100, 100, 100)
slider1_handle_color = (150, 150, 150)
slider1_min_value = 0.0
slider1_max_value = 200000000
slider1_value = particle1_mass

# Slider properties for Particle 2
slider2_rect = pygame.Rect(10, HEIGHT + 40, WIDTH - 20, 20)
slider2_color = (100, 100, 100)
slider2_handle_color = (150, 150, 150)
slider2_min_value = 0.0
slider2_max_value = 200000000
slider2_value = particle2_mass

# Initialize moving sliders
moving_slider1 = False
moving_slider2 = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if slider1_rect.collidepoint(event.pos):
                moving_slider1 = True
            elif slider2_rect.collidepoint(event.pos):
                moving_slider2 = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving_slider1 = False
            moving_slider2 = False
        elif event.type == pygame.MOUSEMOTION:
            if moving_slider1:
                slider1_value = max(slider1_min_value, min(slider1_max_value, (event.pos[0] - slider1_rect.left) / slider1_rect.width * (slider1_max_value - slider1_min_value) + slider1_min_value))
                particle1_mass = slider1_value
            elif moving_slider2:
                slider2_value = max(slider2_min_value, min(slider2_max_value, (event.pos[0] - slider2_rect.left) / slider2_rect.width * (slider2_max_value - slider2_min_value) + slider2_min_value))
                particle2_mass = slider2_value

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the gravitational field vectors with arrows
    for x in range(0, WIDTH, 20):
        for y in range(0, HEIGHT, 20):
            observation_point = [x, y]
        
            if particle1_mass == 0 and particle2_mass == 0:
                # If both masses are zero, draw a vector field without calculating gravitational field
                color = (0, 0, 0)  # Set color to black
                pygame.draw.line(screen, color, observation_point,
                             (observation_point[0] + scaled_field[0], observation_point[1] + scaled_field[1]))
            else:
                # Calculate and draw gravitational field vectors
                gravitational_field = calculate_total_gravitational_field(observation_point)

                # Scale the vector for better visibility
                scaling_factor = 1e7
                scaled_field = [scaling_factor * component for component in gravitational_field]

                # Set color based on magnitude
                color = (0, 0, min(255, int(math.sqrt(gravitational_field[0]**2 + gravitational_field[1]**2) * 10)))

                # Draw arrows
                draw_arrow(screen, color, observation_point, (observation_point[0] + scaled_field[0], observation_point[1] + scaled_field[1]))


    # Draw particles
    pygame.draw.circle(screen, (255, 0, 0), (int(particle1_pos[0]), int(particle1_pos[1])), 10)
    pygame.draw.circle(screen, (0, 0, 255), (int(particle2_pos[0]), int(particle2_pos[1])), 10)

    # Draw sliders for Particle 1 and Particle 2
    pygame.draw.rect(screen, slider1_color, slider1_rect)
    slider1_handle_x = int((slider1_value - slider1_min_value) / (slider1_max_value - slider1_min_value) * slider1_rect.width) + slider1_rect.left
    pygame.draw.circle(screen, slider1_handle_color, (slider1_handle_x, slider1_rect.centery), 10)

    pygame.draw.rect(screen, slider2_color, slider2_rect)
    slider2_handle_x = int((slider2_value - slider2_min_value) / (slider2_max_value - slider2_min_value) * slider2_rect.width) + slider2_rect.left
    pygame.draw.circle(screen, slider2_handle_color, (slider2_handle_x, slider2_rect.centery), 10)

    # Draw mass values
    text1 = font.render(f"Particle 1 Mass: {particle1_mass:.2f} kg", True, (0, 0, 0))
    text2 = font.render(f"Particle 2 Mass: {particle2_mass:.2f} kg", True, (0, 0, 0))
    screen.blit(text1, (10, HEIGHT + 30))
    screen.blit(text2, (10, HEIGHT + 60))

    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
