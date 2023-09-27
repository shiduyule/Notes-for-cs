import pygame

# Initialize pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Weiqi (Go) Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize game variables
board_size = 9
board = [[0] * board_size for _ in range(board_size)]  # 0: empty, 1: black, 2: white
stone_size = 40
grid_size = screen_width // board_size
turn = 1  # 1: black, 2: white

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // grid_size
            row = y // grid_size
            if board[row][col] == 0:
                board[row][col] = turn
                turn = 3 - turn  # Switch turn

    screen.fill(white)

    # Draw board grid
    for i in range(board_size):
        pygame.draw.line(screen, black, (0, i * grid_size), (screen_width, i * grid_size))
        pygame.draw.line(screen, black, (i * grid_size, 0), (i * grid_size, screen_height))

    # Draw stones
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                pygame.draw.circle(screen, black, (col * grid_size, row * grid_size), stone_size // 2)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, white, (col * grid_size, row * grid_size), stone_size // 2)

    pygame.display.update()

pygame.quit()
