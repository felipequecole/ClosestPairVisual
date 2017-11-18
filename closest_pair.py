# -*- coding: utf-8 -*-

import sys, pygame

pygame.init()

class Closest_Pair():
    points = []
    colors = {}
    def __init__(self):
        size = width, height = 800, 600
        self.colors = {
            'white': (255, 255, 255),
            'black': (0,0,0),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255)
        }

        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Closest Pair')
        self.screen.fill(self.colors['white'])

    def draw_point(self, point):
        pygame.draw.circle(self.screen, self.colors['black'], point, 5)


    def draw_points(self):
        for point in self.points:
            self.draw_point(point)


    def reset_screen(self):
        self.screen.fill(self.colors['white'])
        self.draw_points()


    def draw_line(self,pointA, pointB):
        pygame.draw.line(self.screen, self.colors['green'], pointA, pointB)


    def insert_point(self, point):
        self.points.append(point)


    def render(self):
        pygame.display.flip()


    def nro_points(self):
        return len(self.points)


def main():
    cp = Closest_Pair()
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cp.draw_point(pos)
                cp.insert_point(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if (cp.nro_points() > 1):
                        cp.draw_line(cp.points[-1], cp.points[-2])
                elif event.key == pygame.K_r:
                    cp.reset_screen()
            cp.render()

if __name__ == '__main__':
    main()
