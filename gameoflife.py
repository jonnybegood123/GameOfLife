import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 15
HEIGHT = 15
MARGIN = 1
RANGE = 45

grid = [[0 for x in range(RANGE)] for x in range(RANGE)]
tempGrid = [[0 for x in range(RANGE)] for x in range(RANGE)]

WINDOW_SIZE = [705, 705]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")
screen.fill(BLACK)

clock = pygame.time.Clock()

def drawObject(objectName):
    if objectName == "Glider":
        grid[10][5] = 1; grid[11][5] = 1; grid[12][5] = 1
        grid[12][4] = 1; grid[11][3] = 1
    elif objectName == "GliderGun":
        grid[10][5] = 1; grid[10][6] = 1; grid[11][5] = 1; grid[11][6] = 1; grid[9][40] = 1
        grid[10][15] = 1; grid[11][15] = 1; grid[12][15] = 1; grid[13][16] = 1; grid[9][16] = 1
        grid[8][17] = 1; grid[8][18] = 1; grid[14][17] = 1; grid[14][18] = 1; grid[11][19] = 1
        grid[9][20] = 1; grid[13][20] = 1; grid[10][21] = 1; grid[11][21] = 1; grid[12][21] = 1
        grid[11][22] = 1; grid[10][25] = 1; grid[9][25] = 1; grid[8][25] = 1; grid[8][26] = 1
        grid[9][26] = 1; grid[10][26] = 1; grid[11][27] = 1; grid[7][27] = 1; grid[7][29] = 1
        grid[6][29] = 1; grid[11][29] = 1; grid[12][29] = 1; grid[8][39] = 1; grid[9][39] = 1
        grid[8][40] = 1;

def getNumberOfNeighbors(row, column):
    numberOfNeighbors = 0
    try:
        if grid[row-1][column] == 1:
            numberOfNeighbors += 1
        if grid[row+1][column] == 1:
            numberOfNeighbors += 1
        if grid[row][column-1] == 1:
            numberOfNeighbors += 1
        if grid[row][column+1] == 1:
            numberOfNeighbors += 1
        if grid[row-1][column-1] == 1:
            numberOfNeighbors += 1
        if grid[row+1][column+1] == 1:
            numberOfNeighbors += 1
        if grid[row+1][column-1] == 1:
            numberOfNeighbors += 1
        if grid[row-1][column+1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            pass
    return numberOfNeighbors

def drawGame(row, column, color):
    pygame.draw.rect(screen,
                     color,
                     [(MARGIN + WIDTH) * column + MARGIN,
                      (MARGIN + HEIGHT) * row + MARGIN,
                      WIDTH,
                      HEIGHT])

def beginGameOfLife(initial_grid):
    gameDone = False
    while gameDone == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                gameDone = True
        for row in range(RANGE):
            for column in range(RANGE):
                numberOfNeighbors = getNumberOfNeighbors(row, column)
                #Conway's Rules
                if numberOfNeighbors < 2:
                    tempGrid[row][column] = 0
                elif initial_grid[row][column] == 1 and numberOfNeighbors == 2:
                    tempGrid[row][column] = 1
                elif numberOfNeighbors > 3:
                    tempGrid[row][column] = 0
                elif numberOfNeighbors == 3:
                    tempGrid[row][column] = 1
        for row in range(RANGE):
            for column in range(RANGE):
                if tempGrid[row][column] == 1:
                    color = GREEN
                    initial_grid[row][column] = 1
                else:
                    color = WHITE
                    initial_grid[row][column] = 0
                drawGame(row, column, color)
        clock.tick(15)
        pygame.display.flip()

def initialInput():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
                print("Click at:", pos, "with Grid Coordinates: Row:", row, " Column: ", column)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                beginGameOfLife(grid)
        for row in range(RANGE):
            for column in range(RANGE):
                if grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                drawGame(row, column, color)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    drawObject("GliderGun")
    initialInput()
