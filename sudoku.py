import pygame

#define colors
color_beige = (255, 239, 204)
color_dark_brown = (36, 27, 20)
color_light_brown = (173, 106, 57)

def main():
    pygame.init()

    title_font = pygame.font.SysFont("Arial", 32)  # placeholder style
    subtitle_font = pygame.font.SysFont("Arial", 20)  # placeholder style

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

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(color_beige)

            #thin grid lines (every cell)
            for col in range(grid_size + 1):
                pygame.draw.line(screen, "gray", (col * cell_size, 0), (col * cell_size, board_height), 1)
            for row in range(grid_size + 1):
                pygame.draw.line(screen, "gray", (0, row * cell_size), (board_width, row * cell_size), 1)

            #thick grid lines (every 3 cells for 3x3 boxes)
            for col in range(0, grid_size + 1, 3):
                pygame.draw.line(screen, "black", (col * cell_size, 0), (col * cell_size, board_height), 4)
            for row in range(0, grid_size + 1, 3):
                pygame.draw.line(screen, "black", (0, row * cell_size), (board_width, row * cell_size), 4)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

# def start_screen():
#     '''
#     sudoku welcome screen.
#     displays welcome
#     select game mode
#     ***WIP***
#     '''
#     screen.fill(color_beige) #switch to an image if have the time
#
#     start_surf = title_font.render("Sudoku!", True, color_dark_brown)
#     screen.blit(start_surf, (0, 0)) #placeholder coordinates
#
#     sub_start_surf = subtitle_font.render("Please select difficulty:", True, color_dark_brown)
#     screen.blit(sub_start_surf, (100, 100)) #placeholder coordinates
#
#
#
#
# def game_won_screen():
#     '''
#     sudoku game won screen.
#     happens when user wins the game! yay!
#     dislays 'game won!' and has exit button that ends the program
#     ***WIP***
#     '''
#
#
# def game_over_screen():
#     '''
#     sudoku game over screen.
#     idk how you get a game over on sudoku but alright
#     dislays 'game over :(!' and has restart button that ends the program
#     ***WIP***
#     '''



# def main():
#
#     clock = pygame.time.Clock()
#     running = True
