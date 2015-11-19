import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 15
HEIGHT = 15
MARGIN = 1

grid = [[0 for x in range(50)] for x in range(50)]
#tempGrid = [[0 for x in range(30)] for x in range(30)]
#grid[1][5] = 1

WINDOW_SIZE = [801, 801]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")
screen.fill(BLACK)

clock = pygame.time.Clock()

def getNumberOfNeighbors(row, column):
    numberOfNeighbors = 0
    try:
        if grid[row-1][column] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row][column-1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row-1][column-1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row+1][column] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row][column+1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row+1][column+1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row+1][column-1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")
    try:
        if grid[row-1][column+1] == 1:
            numberOfNeighbors += 1
    except IndexError:
            print("")

    return numberOfNeighbors

def beginGameOfLife(grid):
    simDone = False
    while simDone == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                simDone = True
        for row in range(50):
            for column in range(50):
                numberOfNeighbors = getNumberOfNeighbors(row, column)
                if numberOfNeighbors < 2:
                    grid[row][column] = 0
                elif grid[row][column] == 1 and numberOfNeighbors == 2:
                    grid[row][column] = 1
                elif numberOfNeighbors > 3:
                    grid[row][column] = 0
                elif numberOfNeighbors == 3:
                    grid[row][column] = 1

        for row in range(50):
            for column in range(50):
                if grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(10)
        pygame.display.flip()

def mainInitialLoop():
    done = False

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
                print("Click: ", pos, " Grid coordinates: Row:", row, " Column: ", column)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                beginGameOfLife(grid)
                done = True

        for row in range(50):
            for column in range(50):
                if grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    mainInitialLoop()
