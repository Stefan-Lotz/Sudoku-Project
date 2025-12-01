import pygame
from sudoku_generator import generate_sudoku  # Add this import

# define colors
color_beige = (255, 239, 204)
color_dark_brown = (36, 27, 20)
color_light_brown = (173, 106, 57)


def main():
    pygame.init()

    title_font = pygame.font.SysFont("Arial", 48)
    subtitle_font = pygame.font.SysFont("Arial", 28)
    button_font = pygame.font.SysFont("Arial", 16, bold=True)
    number_font = pygame.font.SysFont("Arial", 36)  # Font for numbers on grid

    # sudoku grid settings
    cell_size = 50
    grid_size = 9
    board_width = cell_size * grid_size
    board_height = cell_size * grid_size

    # add small space for buttons at bottom
    window_width = board_width
    window_height = board_height + 80

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    running = True

    def start_screen():
        #welcome screen
        while True:
            screen.fill(color_beige)

            #title text
            start_surf = title_font.render("Sudoku!", True, color_dark_brown)
            screen.blit(start_surf, (window_width // 2 - start_surf.get_width() // 2, 80))

            #difficulty text
            sub_start_surf = subtitle_font.render("Please select difficulty:", True, color_dark_brown)
            screen.blit(sub_start_surf, (window_width // 2 - sub_start_surf.get_width() // 2, 160))

            #difficulty buttons
            easy_rect = pygame.Rect(window_width // 2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, easy_rect, border_radius=8)
            easy_text = subtitle_font.render("Easy", True, color_dark_brown)
            screen.blit(easy_text, (easy_rect.centerx - easy_text.get_width() // 2,
                                    easy_rect.centery - easy_text.get_height() // 2))

            medium_rect = pygame.Rect(window_width // 2 - 100, 300, 200, 50)
            pygame.draw.rect(screen, color_light_brown, medium_rect, border_radius=8)
            medium_text = subtitle_font.render("Medium", True, color_dark_brown)
            screen.blit(medium_text, (medium_rect.centerx - medium_text.get_width() // 2,
                                      medium_rect.centery - medium_text.get_height() // 2))

            hard_rect = pygame.Rect(window_width // 2 - 100, 360, 200, 50)
            pygame.draw.rect(screen, color_light_brown, hard_rect, border_radius=8)
            hard_text = subtitle_font.render("Hard", True, color_dark_brown)
            screen.blit(hard_text, (hard_rect.centerx - hard_text.get_width() // 2,
                                    hard_rect.centery - hard_text.get_height() // 2))

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rect.collidepoint(event.pos):
                        return "easy"
                    if medium_rect.collidepoint(event.pos):
                        return "medium"
                    if hard_rect.collidepoint(event.pos):
                        return "hard"

            pygame.display.flip()
            clock.tick(60)

    def draw_numbers(board):
        for row in range(grid_size):
            for col in range(grid_size):
                num = board[row][col]
                if num != 0:
                    #get position to enter the number in cell
                    x = col * cell_size + cell_size // 2
                    y = row * cell_size + cell_size // 2

                    #draw number on da board
                    num_surf = number_font.render(str(num), True, color_dark_brown)
                    num_rect = num_surf.get_rect(center=(x, y))
                    screen.blit(num_surf, num_rect)

    def init_grid():
        screen.fill(color_beige)

        # thin grid lines (every cell)
        for col in range(grid_size + 1):
            pygame.draw.line(screen, color_light_brown, (col * cell_size, 0), (col * cell_size, board_height), 1)
        for row in range(grid_size + 1):
            pygame.draw.line(screen, color_light_brown, (0, row * cell_size), (board_width, row * cell_size), 1)

        # thick grid lines (every 3 cells for 3x3 boxes)
        for col in range(0, grid_size + 1, 3):
            pygame.draw.line(screen, color_dark_brown, (col * cell_size, 0), (col * cell_size, board_height), 4)
        for row in range(0, grid_size + 1, 3):
            pygame.draw.line(screen, color_dark_brown, (0, row * cell_size), (board_width, row * cell_size), 4)

    def draw_numbers(board):
        '''Draw the numbers on the sudoku board'''
        for row in range(grid_size):
            for col in range(grid_size):
                num = board[row][col]
                if num != 0:  # Only draw non-zero numbers
                    # Calculate position to center the number in the cell
                    x = col * cell_size + cell_size // 2
                    y = row * cell_size + cell_size // 2

                    # Render the number
                    num_surf = number_font.render(str(num), True, color_dark_brown)
                    num_rect = num_surf.get_rect(center=(x, y))
                    screen.blit(num_surf, num_rect)

    def draw_game_buttons():
        # draws reset, restart, and exit button below grid
        button_y = board_height + 15
        button_width = 100
        button_height = 50
        spacing = 25

        # center buttons
        total_width = (button_width * 3) + (spacing * 2)
        start_x = (window_width - total_width) // 2

        # reset button
        reset_rect = pygame.Rect(start_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, color_light_brown, reset_rect, border_radius=5)
        pygame.draw.rect(screen, color_dark_brown, reset_rect, 3, border_radius=5)
        reset_text = button_font.render("RESET", True, color_dark_brown)
        screen.blit(reset_text, (reset_rect.centerx - reset_text.get_width() // 2,
                                 reset_rect.centery - reset_text.get_height() // 2))

        # restart button
        restart_rect = pygame.Rect(start_x + button_width + spacing, button_y, button_width, button_height)
        pygame.draw.rect(screen, color_light_brown, restart_rect, border_radius=5)
        pygame.draw.rect(screen, color_dark_brown, restart_rect, 3, border_radius=5)
        restart_text = button_font.render("RESTART", True, color_dark_brown)
        screen.blit(restart_text, (restart_rect.centerx - restart_text.get_width() // 2,
                                   restart_rect.centery - restart_text.get_height() // 2))

        # exit button
        exit_rect = pygame.Rect(start_x + (button_width + spacing) * 2, button_y, button_width, button_height)
        pygame.draw.rect(screen, color_light_brown, exit_rect, border_radius=5)
        pygame.draw.rect(screen, color_dark_brown, exit_rect, 3, border_radius=5)
        exit_text = button_font.render("EXIT", True, color_dark_brown)
        screen.blit(exit_text,
                    (exit_rect.centerx - exit_text.get_width() // 2, exit_rect.centery - exit_text.get_height() // 2))

        return reset_rect, restart_rect, exit_rect

    def game_screen(difficulty):
        # Generate the sudoku board based on difficulty
        if difficulty == "easy":
            board = generate_sudoku(9, 30)
        elif difficulty == "medium":
            board = generate_sudoku(9, 40)
        else:  # hard
            board = generate_sudoku(9, 50)

        original_board = [row[:] for row in board]  # Save original board for reset

        while True:
            # draw grid with numbers and buttons
            init_grid()
            draw_numbers(board)  # Draw the numbers!
            reset_rect, restart_rect, exit_rect = draw_game_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reset_rect.collidepoint(event.pos):
                        # Reset to original board
                        board = [row[:] for row in original_board]
                        print(f"Reset clicked - Difficulty: {difficulty}")
                    elif restart_rect.collidepoint(event.pos):
                        return "restart"
                    elif exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            pygame.display.flip()
            clock.tick(60)

    def game_won_screen():
        # screen for when user wins w/ exit button
        while True:
            screen.fill(color_beige)

            # text
            won_surf = title_font.render("You beat Sudoku!", True, color_dark_brown)
            screen.blit(won_surf, (window_width // 2 - won_surf.get_width() // 2, 80))

            # exit button
            exit_rect = pygame.Rect(window_width // 2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, exit_rect, border_radius=8)
            exit_text = subtitle_font.render("Exit", True, color_dark_brown)
            screen.blit(exit_text, (exit_rect.centerx - exit_text.get_width() // 2,
                                    exit_rect.centery - exit_text.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                        event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos)):
                    pygame.quit()
                    exit()

            pygame.display.flip()
            clock.tick(60)

    def game_over_screen():
        # screen for when user loses w/ restart button
        while True:
            screen.fill(color_beige)

            # text
            over_surf = title_font.render("Game Over...", True, color_dark_brown)
            screen.blit(over_surf, (window_width // 2 - over_surf.get_width() // 2, 80))

            # restart button
            restart_rect = pygame.Rect(window_width // 2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, restart_rect, border_radius=8)
            restart_text = subtitle_font.render("Restart", True, color_dark_brown)
            screen.blit(restart_text, (restart_rect.centerx - restart_text.get_width() // 2,
                                       restart_rect.centery - restart_text.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        return "restart"

            pygame.display.flip()
            clock.tick(60)

    try:
        while True:
            difficulty = start_screen()
            result = game_screen(difficulty)
            if result != "restart":
                break

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()