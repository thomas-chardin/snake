import pygame
import game
import inputs
import graphics

def handle_main_game_inputs():
	"""
	Handles main game inputs.
	"""
	global main_game
	main_game = game.get_game()
	snake = main_game.snake
	fruit = main_game.fruit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game.stop_running()
   
		if event.type == game.SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				game.stop_running()
			if event.key == pygame.K_UP:
				if snake.direction != inputs.down or len(snake.body) == 1:
					snake.direction = inputs.up
			if event.key == pygame.K_DOWN:
				if snake.direction != inputs.up or len(snake.body) == 1:
					snake.direction = inputs.down
			if event.key == pygame.K_RIGHT:
				if snake.direction != inputs.left or len(snake.body) == 1:
					snake.direction = inputs.right
			if event.key == pygame.K_LEFT:
				if snake.direction != inputs.right or len(snake.body) == 1:
					snake.direction = inputs.left

def handle_main_menu_inputs():
    """
	Handles menu inputs.
	"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.stop_running()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if graphics.PLAY_BUTTON.collidepoint(mouse_pos):
                game.change_current_status(game.PLAYING)
            elif graphics.SCOREBOARD_BUTTON.collidepoint(mouse_pos):
                game.change_current_status(game.SCOREBOARD)

def handle_game_over_inputs():
    """
	Handles game-over screen inputs.
	"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.stop_running()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if graphics.REPLAY_BUTTON.collidepoint(mouse_pos):
                game.set_new_game()
                game.change_current_status(game.PLAYING)
            elif graphics.SCOREBOARD_BUTTON.collidepoint(mouse_pos):
                game.change_current_status(game.SCOREBOARD)
                 
                 
def handle_scoreboard_inputs():
    """
	Handles scoreboard inputs.
	"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.stop_running()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if graphics.BACK_BUTTON.collidepoint(mouse_pos):
                game.set_new_game()
                game.change_current_status(game.MAIN_MENU)
