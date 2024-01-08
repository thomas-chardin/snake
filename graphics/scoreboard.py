import game,graphics
import pygame

BACK_BUTTON = pygame.Rect(1 * graphics.CELL_SIZE - 25, 2 * graphics.CELL_SIZE - 12, 50 , 24)


# Fonction afficher page scoreboard
def draw_scoreboard():
    screen = graphics.get_screen()
    scores_data = game.open_json()
    dates = []
    scores = []
    
    screen.fill("green")
    bg = pygame.image.load("graphics/assets/images/bg.png")
    bg = pygame.transform.scale(bg, (graphics.WINDOW_SIZE, graphics.WINDOW_SIZE))
    screen.blit(bg, (0, 0))
    graphics.draw_text(screen, "SCOREBOARD", graphics.SNAKE_COLOR, 40, 10 * graphics.CELL_SIZE, 2 * graphics.CELL_SIZE)
    graphics.draw_text(screen,"back", graphics.SNAKE_COLOR,15, 1 * graphics.CELL_SIZE, 2 * graphics.CELL_SIZE)
    # pygame.draw.rect(screen, (0, 0, 0), BACK_BUTTON)
    
    if len(scores_data) >= 1:
        for i in scores_data:
            dates += [i["timestamp"]]
            scores += [str(i["score"])]
        for i in range(1,len(scores_data) + 1):
            graphics.draw_text(screen, f'{dates[-i]} --- {scores[-i]}', "red", 10, 10 * graphics.CELL_SIZE, (3 + i) * graphics.CELL_SIZE)
    else:
        graphics.draw_text(screen,"No scores yet",graphics.SNAKE_COLOR,25, 10 * graphics.CELL_SIZE, 4 * graphics.CELL_SIZE)
        
    
    pygame.display.update()