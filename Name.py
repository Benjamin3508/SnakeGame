import pygame
import sys

pygame.init()

stop = False

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up game window
window_width = 500
window_height = 500
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Input Window")

# Set up font
font = pygame.font.Font(None, 32)

# Create input box
prompt_text = font.render(f'Input Username Please:', True, black)
game_window.blit(prompt_text, [100, 70])
input_box = pygame.Rect(100, 100, 300, 50)
input_text = ""  # for usage in other script, use Name.input_text

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check for text input events
            if event.unicode.isalnum():
                input_text += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                stop = True

    # Fill game window with white color
    game_window.fill((255, 255, 255))

    # Draw input box
    game_window.blit(prompt_text, [100, 70])  # Show the Prompt texts
    pygame.draw.rect(game_window, (0, 0, 0), input_box, 2)
    text_surface = font.render(input_text, True, (0, 0, 0))
    game_window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update game window
    pygame.display.update()

    if stop:
        break

# Quit Pygame and exit program if Name.py is running as main module
if __name__ == '__main__':
    print(f'[System Log] {sys.argv[0]} running as main module.')
    pygame.quit()
    quit()
