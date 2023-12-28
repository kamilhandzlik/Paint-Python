import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255) ## Python używa palety RGB ustawiając wszystkie trzy wartości na 255 uzyskujemy biały jako ich mieszankę
BLACK = (0, 0, 0)       ## Analogia z czarnym i każdym innym kolorem
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 60

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("Calibri", size)