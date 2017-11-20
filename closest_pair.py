# -*- coding: utf-8 -*-

import sys, pygame, time, os

pygame.init()
try:
    icon = pygame.image.load(os.path.join('assets', 'icon.png'))
    pygame.display.set_icon(icon)
except Exception as e:
    pass

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


    def draw_border(self):
        # caso tenha um background, é aqui que a gente setaria ele, como não tem..
        self.screen.fill(self.colors['white'])


    def draw_point(self, point, color=(0,0,0)):
        pygame.draw.circle(self.screen, color, point, 5)


    def draw_points(self, points=points):
        for point in self.points:
            self.draw_point(point)


    def reset_screen(self):
        self.draw_border()
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


    def clean_board(self):
        del self.points[:]
        self.reset_screen()
        self.render()


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


    def draw_tunnel(self, x, dist):
        self.reset_screen()
        self.draw_line((x-dist, 0), (x-dist, 600), self.colors['blue'])
        self.draw_line((x+dist, 0), (x+dist, 600), self.colors['blue'])
        self.render()


    def blink_line(self, pA, pB, color, times=3, dividers=True):
        for p in range(times):
                self.reset_screen()
                if (dividers):
                    self.draw_dividers()
                self.render()
                time.sleep(0.2)
                self.draw_line(pA, pB, color)
                self.render()
                time.sleep(0.2)

    def algorithm_bruteforce(self, points=points):
        if (self.nro_points() < 2):
            self.plot_warning('Você precisa ter ao menos 2 pontos', (200, 400))
            time.sleep(1)
            self.reset_screen()
        else:
            self.reset_screen()
            min_dist = ((0,0), (0,0), sys.float_info.max)
            for i in range(len(points)-1):
                for j in range(i+1,len(points)):
                    pA = points[i]
                    pB = points[j]
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
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                pA = points[i]
                pB = points[j]
                self.draw_line(pA, pB, self.colors['black'])
                time.sleep(0.5)
                dist = self.get_distance(pA, pB)
                if (dist < min_dist[2]):
                    min_dist = (pA, pB, dist)
            self.reset_screen()
            self.draw_dividers()
            self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
        return min_dist


    def closest_pair_divide(self, points):
        # print(points)
        if (len(points) < 4):
            return self.closest_pair_brute(points)
        else:
            half = len(points) // 2
            cut = points[half]
            self.insert_divider(cut[0])
            self.draw_dividers()
            self.render()
            # print(half)
            min_left = self.closest_pair_divide(points[:half])
            min_right = self.closest_pair_divide(points[half:])
            self.reset_screen()
            self.draw_dividers()
            self.draw_line(min_left[0], min_left[1], color=self.colors['red'])
            self.draw_line(min_right[0], min_right[1], color=self.colors['red'])
            self.render()
            time.sleep(0.3)
            self.reset_screen()
            self.draw_dividers()
            if(min_right[2] > min_left[2]):
                self.blink_line(pA = min_left[0], pB = min_left[1], color=self.colors['red'], times=3)
                self.lines.pop()
                min_div =  min_left
            else:
                self.blink_line(pA = min_right[0], pB = min_right[1], color=self.colors['red'], times=3)
                self.lines.pop()
                min_div =  min_right
            tunnel = list(filter(lambda p: abs(cut[0] - p[:][0]) < min_div[2], points))
            min_dist = min_div
            if (len(tunnel) > 0):
                self.reset_screen()
                self.draw_tunnel(cut[0], min_div[2])
                self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
                for i in range(len(tunnel)-1):
                    for j in range(i, len(tunnel)):
                        if (abs(tunnel[i][1] - tunnel[j][1]) > min_div[2] or tunnel[i] == tunnel[j]):
                            continue
                        else:
                            dist = self.get_distance(tunnel[i], tunnel[j])
                            self.draw_line(tunnel[i], tunnel[j], self.colors['black'])
                            # self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
                            # self.render()
                            if (dist < min_dist[2]):
                                min_dist = (tunnel[i], tunnel[j], dist)
                            self.reset_screen()
                            self.draw_tunnel(cut[0], min_div[2])
                            self.draw_line(min_dist[0], min_dist[1], self.colors['red'])
                            time.sleep(0.2)

            # print(tunnel)
            # self.reset_screen()
            return min_dist


    def sort_by_coordinate(self, list, coord = 0):
        return sorted(list, key=lambda tup: tup[coord])


    def algorithm_divide_and_conquer(self):
        if (self.nro_points() < 2):
            self.plot_warning('Você precisa ter ao menos 2 pontos', (200, 400))
            time.sleep(1)
            self.reset_screen()
            return ((0,0), (0,0), sys.float_info.max)
        else:
            sorted_by_x = self.sort_by_coordinate(self.points, 0)
            closest_pair = self.closest_pair_divide(sorted_by_x)
            print(closest_pair)
            self.reset_screen()
            self.draw_line(closest_pair[0], closest_pair[1], self.colors['red'])
            self.draw_point(closest_pair[0], color=self.colors['red'])
            self.draw_point(closest_pair[1], color=self.colors['red'])
            self.render()
            return closest_pair




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
                        cp.draw_line(cp.points[-1], cp.points[-2], cp.colors['blue'])
                elif event.key == pygame.K_r:
                    cp.reset_screen()
                elif event.key == pygame.K_b:
                    cp.algorithm_bruteforce()
                elif event.key == pygame.K_d:
                    cp.dump_points()
                elif event.key == pygame.K_s:
                    closest_pair = cp.algorithm_divide_and_conquer()
                    cp.draw_point(closest_pair[0], cp.colors['red'])
                    cp.draw_point(closest_pair[1], cp.colors['red'])
                    # cp.render()
                elif event.key == pygame.K_e:
                    cp.clean_board()
        cp.render()

if __name__ == '__main__':
    main()
