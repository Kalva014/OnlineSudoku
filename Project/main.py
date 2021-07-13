from grid import *


def main():
    pygame.init()
    pygame.display.set_caption("Online Sudoku")
    WINDOW_SIZE = [600, 600]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == '__main__':
    main()