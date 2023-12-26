import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
ANT_SIZE = 10
ANT_SPEED = 2
PHEROMONE_RADIUS = 20
PHEROMONE_STRENGTH = 1
PHEROMONE_DECAY = 0.01

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ant class
class Ant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ANT_SIZE, ANT_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        dx = ANT_SPEED * math.cos(self.angle)
        dy = ANT_SPEED * math.sin(self.angle)
        self.rect.x += dx
        self.rect.y += dy

# Pheromone class
class Pheromone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((2 * PHEROMONE_RADIUS, 2 * PHEROMONE_RADIUS), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0, 100), (PHEROMONE_RADIUS, PHEROMONE_RADIUS), PHEROMONE_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))
        self.strength = PHEROMONE_STRENGTH

    def update(self):
        self.strength -= PHEROMONE_DECAY
        if self.strength <= 0:
            self.kill()

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Colony Simulation")
clock = pygame.time.Clock()

# Sprites groups
all_sprites = pygame.sprite.Group()
ants = pygame.sprite.Group()
pheromones = pygame.sprite.Group()

# Create ants
for _ in range(10):
    ant = Ant(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(ant)
    ants.add(ant)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ants
    for ant in ants:
        ant.update()

    # Check if ants are near pheromones and update their direction
    for ant in ants:
        ant.rect.x = (ant.rect.x + WIDTH) % WIDTH  # Wrap around screen
        ant.rect.y = (ant.rect.y + HEIGHT) % HEIGHT
        nearby_pheromones = pygame.sprite.spritecollide(ant, pheromones, False, pygame.sprite.collide_circle)
        if nearby_pheromones:
            pheromone = max(nearby_pheromones, key=lambda p: p.strength)
            angle_to_pheromone = math.atan2(pheromone.rect.centery - ant.rect.centery,
                                            pheromone.rect.centerx - ant.rect.centerx)
            ant.angle = angle_to_pheromone

    # Create pheromones
    if random.random() < 0.02:
        pheromone = Pheromone(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        all_sprites.add(pheromone)
        pheromones.add(pheromone)

    # Update pheromones
    for pheromone in pheromones:
        pheromone.update()

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
