import graphics
import pygame
import game

def draw_score():
    main_game = game.get_game()
    score = main_game.snake.get_score()
    screen = graphics.get_screen()
    graphics.draw_text(screen, "SCORE: " + str(score), "red", 15, 18 * graphics.CELL_SIZE, 19 * graphics.CELL_SIZE)
    pygame.display.update()