# -*- coding: utf-8 -*-

import sys, pygame, time

pygame.init()
pygame.font.init()

class Closest_Pair():
    points = []     # lista de pontos
    lines = []      # lista de linhas divisórias ativas
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


    def draw_line(self,pointA, pointB, color):
        pygame.draw.line(self.screen, color, pointA, pointB)
        self.render()


    def insert_point(self, point):
        self.points.append(point)


    def insert_divider(self, x):
        self.lines.append(((x, 0), (x,600)))


    def render(self):
        pygame.display.flip()


    def nro_points(self):
        return len(self.points)


    def get_distance(self, pA, pB):
        dist = ((pB[0] - pA[0])**2 + (pB[1] - pA[1])**2)**(1/2)
        return dist


    def plot_warning(self, text, position):
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render(text, True, self.colors['red'])
        self.screen.blit(text, position)
        self.render()


    def draw_dividers(self):
        for line in self.lines:
            self.draw_line(line[0], line[1], self.colors['blue'])
            self.render()


    def algorithm_bruteforce(self, points):
        if (self.nro_points() < 2):
            self.plot_warning('Você precisa ter ao menos 2 pontos', (200, 400))
            time.sleep(1)
            self.reset_screen()
        else:
            min_dist = ((0,0), (0,0), sys.float_info.max)
            for pA in points:
                for pB in points:
                    if (pA == pB):
                        continue
                    else:
                        self.draw_line(pA, pB, self.colors['black'])
                        time.sleep(0.2)
                        dist = self.get_distance(pA, pB)
                        if (dist < min_dist[2]):
                            min_dist = (pA, pB, dist)
                    self.reset_screen()
                    self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
            return min_dist


    def closest_pair_brute(self, points):
        if (len(points) < 2):
            return ((0,0), (0,0), sys.float_info.max)
        min_dist = ((0,0), (0,0), sys.float_info.max)
        for pA in points:
            for pB in points:
                if (pA == pB):
                    continue
                else:
                    self.draw_line(pA, pB, self.colors['black'])
                    time.sleep(0.2)
                    dist = self.get_distance(pA, pB)
                    if (dist < min_dist[2]):
                        min_dist = (pA, pB, dist)
                self.reset_screen()
                self.draw_dividers()
                self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
        return min_dist


    def closest_pair_divide(self, points):
        print(points)
        if (len(points) < 4):
            self.closest_pair_brute(points)
        else:
            half = len(points) // 2
            self.insert_divider(points[half][0])
            self.draw_dividers()
            print(half)
            min_left = self.closest_pair_divide(points[:half])
            min_right = self.closest_pair_divide(points[half:])
            self.lines.pop()


    def algorithm_divide_and_conquer(self):
        if (self.nro_points() < 2):
            self.plot_warning('Você precisa ter ao menos 2 pontos', (200, 400))
            time.sleep(1)
            self.reset_screen()
        else:
            sorted_by_x = sorted(self.points, key=lambda tup: tup[0])
            self.closest_pair_divide(sorted_by_x)




    def dump_points(self):
        print(self.points)


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
                elif event.key == pygame.K_b:
                    cp.algorithm_bruteforce(cp.points)
                elif event.key == pygame.K_d:
                    cp.dump_points()
                elif event.key == pygame.K_s:
                    cp.algorithm_divide_and_conquer()
            cp.render()

if __name__ == '__main__':
    main()
