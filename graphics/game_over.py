import pygame
import game,graphics


REPLAY_BUTTON = pygame.Rect(10 * graphics.CELL_SIZE - 85, 10 * graphics.CELL_SIZE - 25, 170 , 50)


def draw_game_over():
    main_game = game.get_game()
    score = main_game.snake.get_score()
    screen = graphics.get_screen()
    screen.fill("green")
    bg = pygame.image.load("graphics/assets/images/bg.png")
    bg = pygame.transform.scale(bg, (graphics.WINDOW_SIZE, graphics.WINDOW_SIZE))
    screen.blit(bg, (0, 0))
    graphics.draw_text(screen, "GAME OVER!", graphics.SNAKE_COLOR, 40, 10 * graphics.CELL_SIZE, 5 * graphics.CELL_SIZE)
    graphics.draw_text(screen, "Score : " + str(score), graphics.SNAKE_COLOR, 20, 10 * graphics.CELL_SIZE, 7 * graphics.CELL_SIZE)
    # pygame.draw.rect(screen, (0, 0, 0), REPLAY_BUTTON)
    # pygame.draw.rect(screen, (0, 0, 0), graphics.SCOREBOARD_BUTTON)
    graphics.draw_text(screen, "REPLAY", "red", 35, 10 * graphics.CELL_SIZE, 10 * graphics.CELL_SIZE)
    graphics.draw_text(screen, "SCOREBOARD", "red", 35, 10 * graphics.CELL_SIZE, 13 * graphics.CELL_SIZE)
    
    
    pygame.display.update()