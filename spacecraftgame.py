import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BACKGROUND_IMAGE = "space_background.jpeg"
FONT_COLOR = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GAME_DURATION = 60  # 1 minute in seconds
FONT_SIZE_INSTRUCTION = 16
ORANGE_COLOR = (255, 165, 0)
TOTAL_SCORE_FONT_SIZE = 24
SKY_BLUE_COLOR = (135, 206, 250)
GAME_OVER_FONT_SIZE = 36
DARK_BLUE_COLOR = (0, 0, 139)

# Instructions
instructions = [
    "Shoot the asteroids with your spacecraft!",
    "Use the left and right arrow keys to move.",
    "Press SPACE to shoot.",
]

# Game initialization
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
spacecrafts = pygame.sprite.Group()
score_sprites = pygame.sprite.Group()
explosions = pygame.sprite.Group()

# Counters for hits and misses
hit_count = 0
miss_count = 0

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spacecraft Shooter")

# Load spacecraft and asteroid images with alpha channel
SPACECRAFT_IMAGE = "spacecraft.png"
ASTEROID_IMAGE = "asteroid.png"

spacecraft_image = pygame.image.load(SPACECRAFT_IMAGE).convert_alpha()
asteroid_image = pygame.image.load(ASTEROID_IMAGE).convert_alpha()

# Scale the images to the desired size
SPACECRAFT_SIZE = (50, 50)
ASTEROID_SIZE = (40, 40)

spacecraft_image = pygame.transform.scale(spacecraft_image, SPACECRAFT_SIZE)
asteroid_image = pygame.transform.scale(asteroid_image, ASTEROID_SIZE)

# Initialize clock
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Sound effects
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound("shoot.mp3")  # Replace with your sound file
explosion_sound = pygame.mixer.Sound("explosion.mp3")  # Replace with your sound file

# Score sprite
class Score(pygame.sprite.Sprite):
    def __init__(self, text, pos, color):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect(center=pos)


# Player (spacecraft)
class Spacecraft(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spacecraft_image
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.rect.width) // 2
        self.rect.y = HEIGHT - 2 * self.rect.height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 8
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += 8

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        all_sprites.add(bullet)

# Asteroid
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = asteroid_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 2 * self.rect.width)
        self.rect.y = 0
        self.speed = random.randint(4, 8)

    def update(self):
        self.rect.y += self.speed

# Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

# Explosion effects
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def update(self):
        self.alpha -= 15
        if self.alpha > 0:
            pygame.draw.circle(self.image, (255, 69, 0, self.alpha), (15, 15), 15)
        else:
            self.kill()

# Game initialization
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
spacecrafts = pygame.sprite.Group()
score_sprites = pygame.sprite.Group()
explosions = pygame.sprite.Group()

spacecraft = Spacecraft()
all_sprites.add(spacecraft)
spacecrafts.add(spacecraft)

score = 0
total_score = 0
font_instr = pygame.font.Font(None, FONT_SIZE_INSTRUCTION)

# Total score font
font_total_score = pygame.font.Font(None, TOTAL_SCORE_FONT_SIZE)

# Countdown timer
timer = GAME_DURATION  # seconds
font_timer = pygame.font.Font(None, 48)

# Game loop
running = True
while running and timer > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spacecraft.shoot()
                shoot_sound.play()

    all_sprites.update()

    # Spawn asteroids
    if random.randint(0, 30) == 0:
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroids.add(asteroid)

    # Check for collisions
    for spacecraft in spacecrafts:
        hits = pygame.sprite.spritecollide(spacecraft, asteroids, True)
        for asteroid in hits:
            hit_count += 1
            total_score += 1
            explosion_sound.play()

            # Create explosion effects at the hit asteroid position
            explosion = Explosion(asteroid.rect.centerx, asteroid.rect.centery)
            explosions.add(explosion)

            # Remove previous hit score display
            score_sprites.remove(score_sprites.sprites())

            # Display +1 on the right side with incremental value
            score_display = Score(f"+{hit_count}", (WIDTH - 50, HEIGHT // 2), GREEN)
            score_sprites.add(score_display)

    # Check for missed asteroids
    for asteroid in asteroids:
        if asteroid.rect.y >= HEIGHT:
            asteroids.remove(asteroid)
            miss_count += 1

            # Remove previous miss score display
            score_sprites.remove(score_sprites.sprites())

            # Display +1 on the left side with incremental value
            score_display = Score(f"+{miss_count}", (50, HEIGHT // 2), RED)
            score_sprites.add(score_display)

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw all sprites
    all_sprites.draw(screen)
    score_sprites.draw(screen)
    explosions.draw(screen)

    # Display instructions
    y_offset = 20
    for idx, instruction in enumerate(instructions):
        text = font_instr.render(instruction, True, ORANGE_COLOR)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_offset + idx * 20))

    # Display total score
    total_score_text = font_total_score.render(f"Total Score: {total_score}", True, SKY_BLUE_COLOR)
    screen.blit(total_score_text, (WIDTH // 2 - total_score_text.get_width() // 2, HEIGHT - 50))

    # Display countdown timer
    timer_text = font_timer.render(str(timer), True, ORANGE_COLOR)
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Update the countdown timer
    if pygame.time.get_ticks() % 1000 == 0:
        timer -= 1

    # Remove explosions after 1 second
    explosions.update()
    explosions.remove(explosions.sprites())

# Game Over section
font_game_over = pygame.font.Font(None, GAME_OVER_FONT_SIZE)
game_over_text = font_game_over.render("Game Over", True, DARK_BLUE_COLOR)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

score_text = font_total_score.render(f"Total Score: {total_score}", True, DARK_BLUE_COLOR)
score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

exit_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 80, 150, 40)
start_button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 140, 150, 40)

game_over = True

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_rect.collidepoint(event.pos):
                game_over = False
            elif start_button_rect.collidepoint(event.pos):
                # Reset game variables
                timer = GAME_DURATION
                total_score = 0
                hit_count = 0
                miss_count = 0
                spacecrafts.empty()
                asteroids.empty()
                score_sprites.empty()
                explosions.empty()

                # Create a new spacecraft
                spacecraft = Spacecraft()
                all_sprites.add(spacecraft)
                spacecrafts.add(spacecraft)

                # Reset game state
                game_over = False

    # Display Game Over screen
    screen.fill(WHITE)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)

    pygame.draw.rect(screen, DARK_BLUE_COLOR, exit_button_rect)
    pygame.draw.rect(screen, DARK_BLUE_COLOR, start_button_rect)

    font_button = pygame.font.Font(None, 24)
    exit_button_text = font_button.render("Exit", True, WHITE)
    start_button_text = font_button.render("Start New Game", True, WHITE)

    screen.blit(exit_button_text, (exit_button_rect.centerx - exit_button_text.get_width() // 2, exit_button_rect.centery - exit_button_text.get_height() // 2))
    screen.blit(start_button_text, (start_button_rect.centerx - start_button_text.get_width() // 2, start_button_rect.centery - start_button_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

