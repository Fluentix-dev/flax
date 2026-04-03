import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

center_x = WIDTH // 2
center_y = HEIGHT // 2
scale = 40  # pixels per unit

def to_screen(x, y):
    sx = center_x + x * scale
    sy = center_y - y * scale
    return int(sx), int(sy)

def f(x):
    return x**2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # draw axes
    pygame.draw.line(screen, (255,255,255), (0, center_y), (WIDTH, center_y))
    pygame.draw.line(screen, (255,255,255), (center_x, 0), (center_x, HEIGHT))

    # draw graph
    prev = None
    for px in range(WIDTH):
        x = (px - center_x) / scale
        y = f(x)

        point = to_screen(x, y)

        if prev:
            pygame.draw.line(screen, (0,255,0), prev, point)

        prev = point

    pygame.display.flip()
    clock.tick(60)