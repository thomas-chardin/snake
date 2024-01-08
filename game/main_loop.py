import pygame
import game
import inputs

import graphics



SCREEN_UPDATE = pygame.USEREVENT
clock = pygame.time.Clock()

RUNNING = True

MAIN_MENU = 0
PLAYING = 1
GAME_OVER = 2
SCOREBOARD = 3

main_game = None
current_state = MAIN_MENU

def stop_running():
	"""
	Stops the main loop.
	"""
	global RUNNING
	RUNNING = False

def run():
	"""
	The main loop of the game.
	"""
	global RUNNING, MAIN_MENU, PLAYING,GAME_OVER, SCOREBOARD
	global main_game, current_state
	main_game = game.Game()
	
 
	pygame.time.set_timer(SCREEN_UPDATE, 150)
	while RUNNING == True:
		clock.tick(60)
		graphics.fill_screen()
		if current_state == MAIN_MENU:
			graphics.draw_main_menu()
			inputs.handle_main_menu_inputs()
		elif current_state == PLAYING:
			inputs.handle_main_game_inputs()
			main_game.draw_elements()
			pygame.display.update()
		elif current_state == GAME_OVER:
			inputs.handle_game_over_inputs()
			graphics.draw_game_over()
		elif current_state == SCOREBOARD:
			inputs.handle_scoreboard_inputs()
			graphics.draw_scoreboard()
		
		
	graphics.quit()
  
def get_game():
    return main_game

def set_new_game():
    global main_game
    main_game = game.Game()

def change_current_status(status):
    global current_state
    current_state = status
