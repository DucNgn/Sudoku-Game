import pygame
import algorithms

black = (0,0,0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

display_width = 800
display_height = 600

class game:
    board = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],   
            [5, 2, 0, 0, 0, 0, 0, 0, 0],   
            [0, 8, 7, 0, 0, 0, 0, 3, 1],   
            [0, 0, 3, 0, 1, 0, 0, 8, 0],   
            [9, 0, 0, 8, 6, 3, 0, 0, 5],   
            [0, 5, 0, 0, 9, 0, 6, 0, 0],   
            [1, 3, 0, 0, 0, 0, 2, 5, 0],   
            [0, 0, 0, 0, 0, 0, 0, 7, 4],   
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    def __init__(self, rows, cols, frame):
        self.rows = rows
        self.cols = cols
        self.cubeMap = [[Cube(i, j, self.board[i][j], frame) for j in range(cols)] for i in range(rows)] 
        self.frame = frame
        (self.subMatrixDigit, self.RowDigit, self.ColDigit) = algorithms.setUpBitwises(self.board)
        setUpBoard()

    def setUpBoard():
        for each in self.cubeMap:
            each.draw()


# x: cols  y: rows
class Cube:
    def __init__(self, x, y, value, frame):
        self.x = x
        self.y = y
        self.value = value
        self.frame = frame

    def setValue(value):
        self.value = value

    def draw(self):
        font = pygame.font.SysFont("comicsans", 40)
        edge = display_width / 9
        pygame.draw.rect(frame, white, (self.x, self.y, self.x+edge, self.y+edge))

        if (self.value is not 0):
            text = font.render(str(self.value), 1,grey)
            self.frame.blit(text, (self.x+5, self.y+5))
        
        
    def update(self, frame):
        font = pygame.font.SysFont("comicsans", 40)
        edge = display_width / 9
        pygame.draw.rect(frame, white, (self.x, self.y, self.x+edge, self.y+edge))


def main():
    pygame.init()
    pygame.font.init()
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Sudoku')
    clock = pygame.time.Clock()
    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

            pygame.display.update()
        
        clock.tick(60)

    pygame.quit()
    quit()

main()