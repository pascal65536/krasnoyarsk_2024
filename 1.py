import pygame
import sys


def draw_square(screen):
    pygame.display.set_caption('Прямоугольник')
    pygame.draw.rect(screen, 'red', (1, 1, width - 2, height - 2), 0)


if __name__ == '__main__':
    pygame.init()
    try:
        width, height = map(int, input().split())
    except ValueError:
        print("Неправильный формат ввода")
        sys.exit()
    screen = pygame.display.set_mode((width, height))
    draw_square(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    sys.exit()