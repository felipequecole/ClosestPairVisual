# -*- coding: utf-8 -*-

import sys, pygame

pygame.init()

def draw_point(point, screen):
    pygame.draw.circle(screen, 0x00000, point, 5)


def draw_points(points, screen):
    for point in points:
        draw_point(point, screen)


def reset_screen(points, screen):
    white = 255, 255, 255
    screen.fill(white)
    draw_points(points, screen)


def main():
    size = width, height = 800, 600
    speed = [2,2]
    white = 255,255,255
    black = 0,0,0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Closest Pair')

    objeto = pygame.image.load('bola.jpg')
    objeto_rect = objeto.get_rect()
    screen.fill(white)
    pontos = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                draw_point(pos, screen)
                pontos.append(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print('APERTOU ENTER')

            # draw_points(pontos, screen)
            if (len(pontos) > 1):
                pygame.draw.line(screen, (0,255,0), pontos[0], pontos[-1])
            pygame.display.flip()
            print(pontos)

if __name__ == '__main__':
    main()
