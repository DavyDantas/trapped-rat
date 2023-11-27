import pygame
from random import choice
import mapGenerator as mapGen

TILE = 25
cols, rows = mapGen.coluns, mapGen.rows
height ,width = TILE * rows + 2, TILE * cols + 2
RES = width, height
mapCells = mapGen.mapCells

movements = []

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class cell:
    def __init__(self, x, y, path):
        self.x, self.y = x, y
        self.walls = {'top':True, 'bottom':True, 'right':True, 'left':True}
        self.visit = False
        self.path = path

    def draw(self):
        x ,y = self.x * TILE, self.y * TILE
        
        if self.path == '0':
            pygame.draw.rect(sc, pygame.Color('white'), (x, y, TILE, TILE))

        elif self.path == 'e':
            pygame.draw.rect(sc, pygame.Color('yellow'), (x, y, TILE, TILE))
            
        else:
            pygame.draw.rect(sc, pygame.Color('black'), (x, y, TILE, TILE))

        if self.visit  or self.path == 'm' :
            pygame.draw.rect(sc, pygame.Color('blue'), (x, y, TILE, TILE))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + TILE, y), 2)

        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y + TILE), (x, y + TILE), 2)

        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + TILE, y), (x + TILE, y + TILE), 2)

        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + TILE), (x, y), 2)

    def draw_current_cell(self):
        self.visit = True
        x ,y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('red'), (x + 2, y + 2, TILE - 2, TILE - 2))

    def check_cell(self, x, y):
        find_local = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows -1:
            return False
        return grid_cells[find_local(x,y)]

    def check_neighbors(self):
        neighbors = []
        top =self.check_cell(self.x, self.y - 1)
        bottom =self.check_cell(self.x, self.y +  1)
        right =self.check_cell(self.x + 1, self.y)
        left =self.check_cell(self.x - 1, self.y)
        
        if right and not right.visit and (right.path == '0' or right.path == 'e'):
            neighbors.append(right)
            movements.append(right)

        elif left and not left.visit and (left.path == '0' or left.path == 'e'):
            neighbors.append(left)
            movements.append(left)

        elif bottom and not bottom.visit and (bottom.path == '0' or bottom.path == 'e'):
            neighbors.append(bottom)
            movements.append(bottom)

        elif top and not top.visit and (top.path == '0' or top.path == 'e'):
            neighbors.append(top)
            movements.append(top)
        
        else:
            if movements:
                neighbors.append(movements.pop())

        return neighbors[0] if neighbors else False


grid_cells = []
current_cell = cell
final_cell = cell

for row in range(rows):
    for col in range(cols):
        grid_cells.append(cell(col, row, mapCells[row][col]))
        
        if mapCells[row][col] == 'm':
            current_cell = cell(col, row, mapCells[row][col])
        
        if mapCells[row][col] == 'e':
            final_cell = cell(col, row, mapCells[row][col])
while True:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

    [cell.draw() for cell in grid_cells]

    next_cell = current_cell.check_neighbors()
    if next_cell:
        
        current_cell = next_cell
        next_cell.visit=True

        if current_cell.x == final_cell.x and current_cell.y == final_cell.y:
            print(current_cell.x, current_cell.y, final_cell.x, final_cell.y)
            print("GANHOU")
            exit()

    current_cell.draw_current_cell()
    
    pygame.display.flip()
    clock.tick(5)


