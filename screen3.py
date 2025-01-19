import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
GOLD_YELLOW = (255, 215, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

TITLE_FONT = pygame.font.Font(None, 64)
TEXT_FONT = pygame.font.Font(None, 36)
BUTTON_FONT = pygame.font.Font(None, 48)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guessing Game")

button_rect = pygame.Rect(WIDTH // 2 + 80, HEIGHT // 2 - 20, 100, 50)


def draw_timer(seconds_left):
    """Draw the countdown timer as a shrinking pie circle."""
    center = (WIDTH - 100, 50)
    radius = 40
    total_angle = 360
    angle = (seconds_left / 60) * total_angle  
    
    # Draw the background circle
    pygame.draw.circle(screen, BLACK, center, radius)

    # Draw the shrinking pie with a thinner width
    pygame.draw.arc(screen, CYAN, (center[0] - radius, center[1] - radius, radius * 2, radius * 2),
                    0, angle * 3.14 / 180, width=10)

    # Draw the time left
    time_surface = TEXT_FONT.render(str(seconds_left), True, WHITE)
    time_rect = time_surface.get_rect(center=center)
    screen.blit(time_surface, time_rect)


def draw_game(random_number, t1_text, user_guess, seconds_left, is_game_over, won):
    """Render the gameplay elements."""
    screen.fill(BLACK)

    title_surface = TITLE_FONT.render(t1_text, True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_surface, title_rect)

    draw_timer(seconds_left)

    text_field_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 150, 50)
    pygame.draw.rect(screen, GREY, text_field_rect, border_radius=5)

    text_surface = TEXT_FONT.render(user_guess, True, WHITE)
    text_rect = text_surface.get_rect(center=text_field_rect.center)
    screen.blit(text_surface, text_rect)

    mouse_pos = pygame.mouse.get_pos()
    button_color = CYAN if button_rect.collidepoint(mouse_pos) else (0, 200, 200)
    pygame.draw.rect(screen, button_color, button_rect, border_radius=5)

    button_surface = BUTTON_FONT.render("OK", True, BLACK)
    button_text_rect = button_surface.get_rect(center=button_rect.center)
    screen.blit(button_surface, button_text_rect)

    # Game Over or Congratulations Popup
    if is_game_over:
        popup_rect = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, HEIGHT // 3)
        pygame.draw.rect(screen, BLACK, popup_rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, popup_rect, 5, border_radius=10)

        popup_text = "Congratulations!" if won else "Game Over"
        popup_surface = TITLE_FONT.render(popup_text, True, GREEN if won else RED)
        popup_rect = popup_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        screen.blit(popup_surface, popup_rect)

        # Restart Button (Grey Circle with Golden Yellow Text)
        restart_rect = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 + 30, 50, 50)
        pygame.draw.ellipse(screen, GREY, restart_rect)

        restart_surface = BUTTON_FONT.render(">", True, GOLD_YELLOW)
        restart_text_rect = restart_surface.get_rect(center=restart_rect.center)
        screen.blit(restart_surface, restart_text_rect)

        return restart_rect


def main():
    """Main loop for Screen 3."""
    clock = pygame.time.Clock()

    random_number = random.randint(0, 1000)
    user_guess = ""
    t1_text = "Guess My Number!"
    is_game_over = False
    won = False
    timer_start = pygame.time.get_ticks()
    seconds_left = 60  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not is_game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_guess = user_guess[:-1]
                    elif event.key == pygame.K_RETURN:
                        pass  # Ignore Enter
                    elif event.unicode.isdigit():
                        user_guess += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        if user_guess.isdigit():
                            guessed_number = int(user_guess)
                            if guessed_number < random_number:
                                t1_text = "Too Low"
                            elif guessed_number > random_number:
                                t1_text = "Too High"
                            else:
                                is_game_over = True
                                won = True
                        user_guess = ""  # Clear text field 
        
        if not is_game_over:  # Stop updating timer when game is over
            elapsed_time = (pygame.time.get_ticks() - timer_start) / 1000
            seconds_left = max(0, 60 - int(elapsed_time))

            if seconds_left == 0:
                is_game_over = True

        restart_rect = draw_game(random_number, t1_text, user_guess, seconds_left, is_game_over, won)

        if is_game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                return "screen1" if won else "screen3"  # Navigate based on popup type

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    next_screen = main()
    print(f"Transitioning to: {next_screen}")

