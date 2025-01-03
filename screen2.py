import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Dimensions and Colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
HEADING_FONT = pygame.font.Font(None, 64)
TEXT_FONT = pygame.font.Font(None, 36)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess My Number - Screen 2")


def draw_rules(alpha):
    """Render the rules with optional fade-out effect."""
    screen.fill(BLACK)

    # Heading
    heading_surface = HEADING_FONT.render("Rules and Guidelines", True, WHITE)
    heading_surface.set_alpha(alpha)
    heading_rect = heading_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(heading_surface, heading_rect)

    # Rules Text (Left-Aligned)
    rules = [
        "1. My number is between 0 to 1000",
        "",
        "2. You can enter your guessed number",
        "",
        "3. Guess the number within 60 seconds",
    ]

    start_x = WIDTH // 4
    start_y = HEIGHT // 2 

    for i, rule in enumerate(rules):
        rule_surface = TEXT_FONT.render(rule, True, WHITE)
        rule_surface.set_alpha(alpha)
        rule_rect = rule_surface.get_rect(topleft=(start_x-25, start_y- 60+ i * 40))
        screen.blit(rule_surface, rule_rect)


def main():
    """Main loop for Screen 2."""
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    fade_duration = 2000  # Fade-out duration in milliseconds
    alpha = 255  # Full opacity

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # Fade out effect after 6 seconds
        if elapsed_time > 6000:
            alpha = max(0, 255 - int((elapsed_time - 6000) / fade_duration * 255))
            if alpha == 0:
                return "screen3"  # Transition to Screen 3

        # Draw rules with fading effect
        draw_rules(alpha)

        # Update display
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    # Run Screen 2
    next_screen = main()
    print(f"Transitioning to: {next_screen}")

