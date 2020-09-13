import pygame
import sys
pygame.font.init()


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

win = pygame.display.set_mode((502 , 550))

pygame.display.set_caption("Sudoku")
win.fill((255,255,255))

gap = 500/9
run = True

def printBoard(brd, win):
    for i  in range(10):
        thick = 1
        if i % 3 == 0:
            thick = 4
        pygame.draw.line(win, (0,0,0), (i*(500/9), 0), (i*(500/9), 500), thick)
        pygame.draw.line(win, (0,0,0), (0, i*(500/9)), (500, i*(500/9)), thick)
    add_numbers(brd, win)

def add_numbers(brd, win):
    font = pygame.font.SysFont("comicsans", 40)
    for j in range(9):
        for i in range(9):
            if brd[j][i] != 0:
                text = font.render(str(brd[j][i]), 1, (0,0,0))
                win.blit(text, ((i + 0.5)*gap - text.get_width()/2 , (j + 0.5)*gap - text.get_height()/2))
                pygame.display.update()

            

def find_empty(brd):
    for i in range(9):
        for j in range(9):
            if brd[i][j] == 0:
                return i,j

    return False     

def is_valid(brd, pos, num):
    i,j = pos
    for rows in range(9):
        if brd[i][rows] == num and i != rows:
            wrong = 1
            return False
        elif brd[rows][j] == num and j != rows:
            wrong = 1
            return False
    box_x = i//3
    box_y = j//3


    for x in range(box_x*3, box_x*3 + 3):
        for y in range(box_y*3,  box_y*3 + 3):
            if brd[x][y] == num:
                return False

    return True


def draw_box(brd, i, j, green, num):

    pygame.draw.rect(win, (255,255,255), (j*gap + 2, i*gap + 2, gap - 2, gap - 2), 0)
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render(str(num), 1, (0,0,0))
    win.blit(text, ((j + 0.5)*gap - text.get_width()/2 , (i + 0.5)*gap - text.get_height()/2))

    if green:
        pygame.draw.rect(win, (0,255,0), (j*gap, i*gap, gap, gap), 3)
    else:
        pygame.draw.rect(win, (255,0,0), (j*gap, i*gap, gap, gap), 3)

def solve(brd):
    if find_empty(brd) == False:
        return True
    else:
        i,j = find_empty(brd)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()


    for n in range(1,10):
        
        if is_valid(brd, (i,j), n):
            brd[i][j] = n
            pygame.time.delay(10)
            draw_box(brd, i, j, True, n)
            pygame.display.update()
            pygame.time.delay(100)
            if solve(brd):
                return True

            brd[i][j] = 0
            pygame.time.delay(10)
            draw_box(brd, i, j, False, n)
            pygame.display.update()
            pygame.time.delay(100)

    return False
        

def redraw_window():
    printBoard(board, win)
    add_numbers(board, win)

redraw_window()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve(board)
                win.fill((255,255,255))
                redraw_window()
    pygame.display.update()
