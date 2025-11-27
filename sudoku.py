import pygame

#define colors
color_beige = (255, 239, 204)
color_dark_brown = (36, 27, 20)
color_light_brown = (173, 106, 57)

def main():
    pygame.init()

    title_font = pygame.font.SysFont("Arial", 32)  # placeholder style
    subtitle_font = pygame.font.SysFont("Arial", 20)  # placeholder style

    screen = pygame.display.set_mode((640, 512))
    clock = pygame.time.Clock()
    running = True

    square_size = 32
    cols = 20
    rows = 16
    width = cols * square_size
    height = rows * square_size

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(color_beige)

            #thin grid lines
            for col in range(cols + 1):
                pygame.draw.line(screen, "gray", (col * square_size, 0), (col * square_size, height), 1)
            for row in range(rows + 1):
                pygame.draw.line(screen, "gray", (0, row * square_size), (width, row * square_size), 1)

            #thick grid lines
            for col in range(0, cols + 1, 3):
                pygame.draw.line(screen, "black", (col * square_size, 0), (col * square_size, height))
            for row in range(0, rows + 1, 3):
                pygame.draw.line(screen, "black", (0, row * square_size), (width, row * square_size), 3)

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
