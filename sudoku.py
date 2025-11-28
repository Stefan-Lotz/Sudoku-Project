import pygame

#define colors
color_beige = (255, 239, 204)
color_dark_brown = (36, 27, 20)
color_light_brown = (173, 106, 57)

def main():
    pygame.init()

    title_font = pygame.font.SysFont("Arial", 48)
    subtitle_font = pygame.font.SysFont("Arial", 28)

    #sudoku grid settings
    cell_size = 50
    grid_size = 9
    board_width = cell_size * grid_size
    board_height = cell_size * grid_size

    #add small space for buttons at bottom
    window_width = board_width
    window_height = board_height + 80

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    running = True

    difficulty = None

    def start_screen():
        #welcome screen
        while True:
            screen.fill(color_beige)

            #title text
            start_surf = title_font.render("Sudoku!", True, color_dark_brown)
            screen.blit(start_surf, (window_width//2 - start_surf.get_width()//2, 80))

            #difficulty text
            sub_start_surf = subtitle_font.render("Please select difficulty:", True, color_dark_brown)
            screen.blit(sub_start_surf, (window_width//2 - sub_start_surf.get_width()//2, 160))


            #difficulty buttons
            easy_rect = pygame.Rect(window_width//2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, easy_rect, border_radius=8)
            easy_text = subtitle_font.render("Easy", True, color_dark_brown)
            screen.blit(easy_text, (easy_rect.centerx - easy_text.get_width()//2, easy_rect.centery - easy_text.get_height()//2))

            medium_rect = pygame.Rect(window_width // 2 - 100, 300, 200, 50)
            pygame.draw.rect(screen, color_light_brown, medium_rect, border_radius=8)
            medium_text = subtitle_font.render("Medium", True, color_dark_brown)
            screen.blit(medium_text, (medium_rect.centerx - medium_text.get_width() // 2, medium_rect.centery - medium_text.get_height() // 2))

            hard_rect = pygame.Rect(window_width // 2 - 100, 360, 200, 50)
            pygame.draw.rect(screen, color_light_brown, hard_rect, border_radius=8)
            hard_text = subtitle_font.render("Hard", True, color_dark_brown)
            screen.blit(hard_text, (hard_rect.centerx - hard_text.get_width() // 2, hard_rect.centery - hard_text.get_height() // 2))

            #event loop bcs I couldn't get it to work out of the function lol
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_rect.collidepoint(event.pos):
                        difficulty = "easy"
                        game_screen(difficulty)
                        break
                    if medium_rect.collidepoint(event.pos):
                        difficulty = "medium"
                        game_screen(difficulty)
                        break
                    if hard_rect.collidepoint(event.pos):
                        difficulty = "hard"
                        game_screen(difficulty)
                        break

            pygame.display.flip()
            clock.tick(60)


    def init_grid():
        screen.fill(color_beige)

        #thin grid lines (every cell)
        for col in range(grid_size + 1):
            pygame.draw.line(screen, color_light_brown, (col * cell_size, 0), (col * cell_size, board_height), 1)
        for row in range(grid_size + 1):
            pygame.draw.line(screen, color_light_brown, (0, row * cell_size), (board_width, row * cell_size), 1)

        #thick grid lines (every 3 cells for 3x3 boxes)
        for col in range(0, grid_size + 1, 3):
            pygame.draw.line(screen, color_dark_brown, (col * cell_size, 0), (col * cell_size, board_height), 4)
        for row in range(0, grid_size + 1, 3):
            pygame.draw.line(screen, color_dark_brown, (0, row * cell_size), (board_width, row * cell_size), 4)

        pygame.display.flip()
        clock.tick(60)


    def game_screen(difficulty):
        init_grid()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
            pygame.display.flip()
            clock.tick(60)



    def game_won_screen():
        #screen for when user wins w/ exit button
        while True:
            screen.fill(color_beige)

            #text
            start_surf = title_font.render("You beat Sudoku!", True, color_dark_brown)
            screen.blit(start_surf, (window_width//2 - start_surf.get_width()//2, 80))

            #exit button
            exit_rect = pygame.Rect(window_width // 2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, exit_rect, border_radius=8)
            exit_text = subtitle_font.render("Exit", True, color_dark_brown)
            screen.blit(exit_text, (exit_rect.centerx - exit_text.get_width() // 2, exit_rect.centery - exit_text.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    exit()


    def game_over_screen():
        #screen for when user loses w/ restart button
        while True:
            screen.fill(color_beige)

            # text
            start_surf = title_font.render("Game Over...", True, color_dark_brown)
            screen.blit(start_surf, (window_width // 2 - start_surf.get_width() // 2, 80))

            #restart button
            restart_rect = pygame.Rect(window_width // 2 - 100, 240, 200, 50)
            pygame.draw.rect(screen, color_light_brown, restart_rect, border_radius=8)
            restart_text = subtitle_font.render("Restart", True, color_dark_brown)
            screen.blit(restart_text, (restart_rect.centerx - restart_text.get_width() // 2,
                                    restart_rect.centery - restart_text.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        start_screen()
                        break

    try:
        start_screen()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

