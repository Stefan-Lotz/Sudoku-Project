import pygame, sys

#frank here, moved init() up so that the other funtions work
pygame.init()
screen = pygame.display.set_mode((640, 512))

color_beige = (255, 239, 204)
color_dark_brown = (36, 27, 20)
color_light_brown = (173, 106, 57)

title_font = pygame.font.SysFont("Arial", 32) #placeholder style
subtitle_font = pygame.font.SysFont("Arial", 20) #placeholder style


def start_screen():
    '''
    sudoku welcome screen.
    displays welcome
    select game mode
    ***WIP***
    '''
    screen.fill(color_beige) #switch to an image if have the time

    start_surf = title_font.render("Sudoku!", True, color_dark_brown)
    screen.blit(start_surf, (0, 0)) #placeholder coordinates

    sub_start_surf = subtitle_font.render("Please select difficulty:", True, color_dark_brown)
    screen.blit(sub_start_surf, (100, 100)) #placeholder coordinates




def game_won_screen():
    '''
    sudoku game won screen.
    happens when user wins the game! yay!
    dislays 'game won!' and has exit button that ends the program
    ***WIP***
    '''


def game_over_screen():
    '''
    sudoku game over screen.
    idk how you get a game over on sudoku but alright
    dislays 'game over :(!' and has restart button that ends the program
    ***WIP***
    '''




def main():



    clock = pygame.time.Clock()
    running = True
