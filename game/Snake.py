import pygame as pg
import game
import graphics

class Snake:
    def __init__(self) -> None:
        self.body = [pg.Vector2(10,9)]
        self.direction = pg.Vector2(0,0)
        self.new_block = False
        
        self.one = pg.image.load("graphics/assets/images/one.png")
        self.head_up = pg.image.load("graphics/assets/images/head_up.png")
        self.head_down = pg.image.load("graphics/assets/images/head_down.png")
        self.head_right = pg.image.load("graphics/assets/images/head_right.png")
        self.head_left = pg.image.load("graphics/assets/images/head_left.png")
        self.one = pg.transform.scale(self.one, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.head_up = pg.transform.scale(self.head_up, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.head_down = pg.transform.scale(self.head_down, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.head_right = pg.transform.scale(self.head_right, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.head_left = pg.transform.scale(self.head_left, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        
        self.tail_up = pg.image.load("graphics/assets/images/tail_up.png")
        self.tail_down = pg.image.load("graphics/assets/images/tail_down.png")
        self.tail_right = pg.image.load("graphics/assets/images/tail_right.png")
        self.tail_left = pg.image.load("graphics/assets/images/tail_left.png")
        self.tail_up = pg.transform.scale(self.tail_up, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.tail_down = pg.transform.scale(self.tail_down, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.tail_right = pg.transform.scale(self.tail_right, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.tail_left = pg.transform.scale(self.tail_left, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        
        self.body_vertical = pg.image.load("graphics/assets/images/body_vertical.png")
        self.body_horizontal = pg.image.load("graphics/assets/images/body_horizontal.png")
        self.body_vertical = pg.transform.scale(self.body_vertical, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.body_horizontal = pg.transform.scale(self.body_horizontal, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        
        self.body_bl = pg.image.load("graphics/assets/images/body_bottomleft.png")
        self.body_br = pg.image.load("graphics/assets/images/body_bottomright.png")
        self.body_tl = pg.image.load("graphics/assets/images/body_topleft.png")
        self.body_tr = pg.image.load("graphics/assets/images/body_topright.png")
        self.body_bl = pg.transform.scale(self.body_bl, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.body_br = pg.transform.scale(self.body_br, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.body_tl = pg.transform.scale(self.body_tl, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        self.body_tr = pg.transform.scale(self.body_tr, (graphics.CELL_SIZE, graphics.CELL_SIZE))
        
        self.head = self.update_head_graphics()
        self.tail = self.update_tail_graphics()
    
    def draw_snake(self):
        screen = graphics.get_screen()
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x = int(block.x * graphics.CELL_SIZE)
            y = int(block.y * graphics.CELL_SIZE)
            body_rectangle = pg.Rect(x, y, graphics.CELL_SIZE, graphics.CELL_SIZE)
            
            if len(self.body) > 1:
                if index == 0:
                    screen.blit(self.head,body_rectangle)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail,body_rectangle)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if next_block.x == previous_block.x:
                        screen.blit(self.body_vertical, body_rectangle)
                    elif next_block.y == previous_block.y:
                        screen.blit(self.body_horizontal, body_rectangle)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl,body_rectangle)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl,body_rectangle)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr,body_rectangle)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br,body_rectangle)    
                        
                # else:
                #     pg.draw.rect(screen,'blue', body_rectangle)
            else:
                    # pg.draw.rect(screen,graphics.SNAKE_COLOR, body_rectangle)
                    screen.blit(self.one, body_rectangle)
    
    def update_head_graphics(self):
        if len(self.body) == 1:
            return None
        head_relation = self.body[1] - self.body[0]
        if head_relation == pg.Vector2(1,0):
            self.head = self.head_left
        elif head_relation == pg.Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == pg.Vector2(0,1):
            self.head = self.head_up
        elif head_relation == pg.Vector2(0,-1):
            self.head = self.head_down
        
    def update_tail_graphics(self):
        if len(self.body) == 1:
            return None
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pg.Vector2(1,0):
            self.tail = self.tail_left
        elif tail_relation == pg.Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_relation == pg.Vector2(0,1):
            self.tail = self.tail_up
        elif tail_relation == pg.Vector2(0,-1):
            self.tail = self.tail_down
    
    def move_snake(self):
        if self.direction != pg.Vector2(0,0):
            if self.new_block:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                if len(self.body) == 1:
                    body_copy = self.body
                    body_copy[0] += self.direction
                    self.body = body_copy[:]
                else:
                    body_copy = self.body[:-1]
                    body_copy.insert(0, body_copy[0] + self.direction)
                    self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
    def get_score(self):
        return (len(self.body) - 1)