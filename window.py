import pygame, sys
from assets.pygame_assets.Tiles import Tile


# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UNMAPPED = (30, 50, 130)
MAPPED = (60, 200, 230)

pygame.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map")

clock = pygame.time.Clock()

def terminate():
    pygame.quit()
    sys.exit()

grid = [[Tile() for x in range(10)] for y in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            column = pos[0] // (60)
            row = pos[1] // (60)
            grid[row][column].mapped = True

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            if grid[row][column].mapped == True:
                color = MAPPED
            else:
                color = UNMAPPED
            pygame.draw.rect(screen, color, [60 * column, 60 * row, 58, 58])

    pygame.display.flip()

    clock.tick(60)


