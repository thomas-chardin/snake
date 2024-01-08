import pygame
import graphics

PLAY_BUTTON = pygame.Rect(10 * graphics.CELL_SIZE - 60, 10 * graphics.CELL_SIZE - 25, 120 , 50)
SCOREBOARD_BUTTON = pygame.Rect(10 * graphics.CELL_SIZE - 145, 13 * graphics.CELL_SIZE - 25, 290, 50)

def draw_main_menu():
    screen = graphics.get_screen()
    screen.fill("green")
    bg = pygame.image.load("graphics/assets/images/bg.png")
    bg = pygame.transform.scale(bg, (graphics.WINDOW_SIZE, graphics.WINDOW_SIZE))
    screen.blit(bg, (0, 0))
    graphics.draw_text(screen, "SNAKE GAME!", graphics.SNAKE_COLOR, 40, 10 * graphics.CELL_SIZE, 5 * graphics.CELL_SIZE)
    # pygame.draw.rect(screen, (0, 0, 0), PLAY_BUTTON)
    # pygame.draw.rect(screen, (0, 0, 0), SCOREBOARD_BUTTON)
    graphics.draw_text(screen, "PLAY", "red", 35, 10 * graphics.CELL_SIZE, 10 * graphics.CELL_SIZE)
    graphics.draw_text(screen, "SCOREBOARD", "red", 35, 10 * graphics.CELL_SIZE, 13 * graphics.CELL_SIZE)
    
    
    pygame.display.update()
    
