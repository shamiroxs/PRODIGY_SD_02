import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
HOVER_COLOR = (0, 200, 200)
BLACK = (0, 0, 0)

TITLE_FONT = pygame.font.Font(None, 74)
BUTTON_FONT = pygame.font.Font(None, 48)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Guessing Game")

button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 60)


def draw_screen():
    """Render the screen with title and button."""
    screen.fill(BLACK)

    title_surface = TITLE_FONT.render("Guess My Number", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_surface, title_rect)

    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, HOVER_COLOR, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, CYAN, button_rect, border_radius=10)

    button_surface = BUTTON_FONT.render("Start", True, BLACK)
    button_text_rect = button_surface.get_rect(center=button_rect.center)
    screen.blit(button_surface, button_text_rect)


def main():
    """Main loop for Screen 1."""
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return "screen2"  # Transition to Screen 2

        draw_screen()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    next_screen = main()
    print(f"Transitioning to: {next_screen}")

