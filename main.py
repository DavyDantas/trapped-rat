import pygame 
from random import choice

RES = width, height = 1202, 902
TILE = 25
cols, rows = width // TILE, height // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top':True, 'bottom':True, 'right':True, 'left':True}
        self.visit = False

    def draw(self):
        x ,y = self.x * TILE, self.y * TILE

        if self.visit:
            pygame.draw.rect(sc, pygame.color('black'), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 2)
        
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x, y + TILE), 2)

        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 2)

        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 2)

    def draw_current_cell(self):


grid_cells = [cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
stack = []

while True:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in grid_cells]
    pygame.display.flip()
    clock.tick(30)


