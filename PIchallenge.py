import pygame
from random import randint
from math import sqrt

# pygame 구조
# pygame 선언
# pygame 초기화 --> pygame.init()
# pygame에서 사용할 전역 변수 선언
# size --> x크기 y크기
# screen --> pygame.display.set_mode(size)
# clock --> pygame.time.Clock()
# pygame loop
# pygame event 설정
# pygame 화면 설정
# 사용자 동작

width = 400
height = 400
fps = 100

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PI")
clock = pygame.time.Clock()

dot_circle = 0
tot_dot = 0
r = 200

draw_dot_x = []
draw_dot_y = []
draw_dot_color = []

pi = 3.141592653589793238462643
print()
print("PI", pi)
print()

# loop
run = True
time_print = pygame.time.get_ticks()
while run:
    # speed
    time = clock.tick(fps) / 100000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x = randint(0, r * 2)
    y = randint(0, r * 2)
    dis = sqrt((r - x) ** 2 + (r - y) ** 2)

    if dis < 200:
        dot_circle += 1
        tot_dot += 1
        color = (48, 240, 31)
    else:
        tot_dot += 1
        color = (235, 52, 0)

    draw_dot_x.append(x)
    draw_dot_y.append(y)
    draw_dot_color.append(color)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, width, height))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(2, 2, width - 4, height - 4))

    pygame.draw.circle(screen, (255, 255, 255), (width // 2, height // 2), r)
    pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), 199)

    for i in range(len(draw_dot_x) - 1):
        x_ = draw_dot_x[i]
        y_ = draw_dot_y[i]
        color = draw_dot_color[i]
        screen.set_at((x_, y_), color)

        if pygame.time.get_ticks() - time_print >= 100:
            PI = 4 * (dot_circle / tot_dot)
            time_print = pygame.time.get_ticks()
            print("calculating PI: ", PI)

        pygame.display.flip()

pygame.quit()
quit()
