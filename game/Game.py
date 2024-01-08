from collections.abc import Iterable
import game
import graphics
class Game:
    def __init__(self) -> None:
        self.snake = game.Snake()
        self.fruit = game.Fruit()
        
    def update(self):
        self.snake.move_snake()
        self.check_collisions()
        self.check_end()
        
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        graphics.draw_score()
        
    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            for i in range(len(self.snake.body)):
                if self.snake.body[i] == self.fruit.pos:
                    self.fruit.randomize()
            self.snake.add_block()
            
    def check_end(self):
        if not (0 <= self.snake.body[0].x < graphics.CELL_NUMBER and 0 <= self.snake.body[0].y < graphics.CELL_NUMBER):
            print("Game Over SCREEN")
            game.change_current_status(game.GAME_OVER)
            game.add_score_to_json(self.snake.get_score())
        for body_part in self.snake.body[1:]:
            if self.snake.body[0] == body_part:
                print("Game Over EATED")
                game.change_current_status(game.GAME_OVER)
                game.add_score_to_json(self.snake.get_score())
                
                
            
                