import pygame, sys
from pygame.locals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, area, pos):
        super().__init__()
        self.area = area
        self.pos = pos
        self.image = pygame.Surface(self.area)
        self.rect = self.image.get_rect()
        self.mapped = False

    
    def set_color(self, color):
        self.image.fill(color, self.rect.inflate(-2, -2))

    def check_unmapped(self):
        pass

def draw_brick(brick, outline_color, fill_color):
    # Fill with the outline color
    brick.image.fill(outline_color, brick.rect)#brick.rect
    # Fill with the actual block color
    brick.image.fill(fill_color, brick.rect.inflate(-2, -2))
    return brick.image

def get_brick(area, pos, outline_color, fill_color):
    # Create brick object
    b = Block(area, pos)
    # Draw the object
    b.image = draw_brick(b, outline_color, fill_color)
    return b


pygame.init()
WINDOWWIDTH = 600
WIDNOWHEIGHT = 600


window = pygame.display.set_mode((WINDOWWIDTH, WIDNOWHEIGHT), 0, 32)
pygame.display.set_caption("test")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
UNMAPPED = (30, 50, 130)
MAPPED = (60, 200, 230)

window.fill(WHITE)

def terminate():
    pygame.quit()
    sys.exit()

def draw_map():
    block_size = 60
    tiles = []
    # for x in range(0, WINDOWWIDTH, block_size):
    #     for y in range(0, WIDNOWHEIGHT, block_size):
    #         rect = pygame.Rect(x, y, block_size, block_size)
    #         pygame.draw.rect(window, BLACK, rect, 1)
    area = (block_size, block_size)
    for x in range(0, WINDOWWIDTH, block_size):
        for y in range(0, WIDNOWHEIGHT, block_size):
            pos = (x, y)
            tiles.append(get_brick(area, pos, BLACK, UNMAPPED))
            
    return tiles


tiles = draw_map()
print(len(tiles))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_tiles = [tile for tile in tiles if tile.rect.collidepoint(pos)]
            print(len(clicked_tiles))
            print(pos)
            for tile in clicked_tiles:
                tile.mapped = True

    for tile in tiles:
        if tile.mapped:
            tile.set_color(MAPPED)
        window.blit(tile.image, tile.pos)
        
    pygame.display.flip()
    

            