import pygame

def draw_text(screen ,text, text_col, font_size, x, y):
    font = pygame.font.SysFont("arialblack", font_size)
    text = font.render(text, True, text_col)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text,text_rect)