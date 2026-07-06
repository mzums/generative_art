import pygame
import math
import random

WIDTH, HEIGHT = 800, 800


def generate_scene():
    points = []
    for _ in range(1000):
        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)

        d = math.sqrt(x*x + y*y)
        chance = (d / 400) ** 2

        if random.random() < chance:
            size = 2 + 4 * (d / 400)
            points.append((x, y, size))
    return points

def draw_scene(screen, points):
    for x, y, size in points:
        px = WIDTH // 2 + x
        py = HEIGHT // 2 + y
        pygame.draw.circle(screen, (150, 150, 200), (int(px), int(py)), int(size))


def rotate(x, y, angle):
    c = math.cos(angle)
    s = math.sin(angle)
    return x*c - y*s, x*s + y*c


def draw_line(screen, x1, y1, x2, y2):
    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)


def draw_circle(screen, x, y, r):
    pygame.draw.circle(screen, (100, 100, 150), (int(x), int(y)), int(r))


def draw_snowflake(screen, cx, cy):
    white = (255, 255, 255)
    fill_color = (100, 100, 150)

    angle = math.radians(-60)

    for _ in range(6):
        x1, y1 = rotate(0, 0, angle)
        x2, y2 = rotate(225, 0, angle)
        pygame.draw.line(screen, white, (cx + x1, cy + y1), (cx + x2, cy + y2), 2)

        for sx, sy in [(15, -30), (15, 30)]:
            x1, y1 = rotate(sx, sy, angle)
            x2, y2 = rotate(60, 0, angle)
            pygame.draw.line(screen, white, (cx + x1, cy + y1), (cx + x2, cy + y2), 2)

        for base in [120, 135, 150]:
            for dy in [-22.5, 22.5]:
                x1, y1 = rotate(base, 0, angle)
                x2, y2 = rotate(base + 30, dy, angle)
                pygame.draw.line(screen, white, (cx + x1, cy + y1), (cx + x2, cy + y2), 2)

        x, y = rotate(225, 0, angle)
        pygame.draw.circle(screen, fill_color, (int(cx + x), int(cy + y)), 15)
        pygame.draw.circle(screen, white, (int(cx + x), int(cy + y)), 15, 2)

        angle += math.radians(30)

        x1, y1 = rotate(30, 0, angle)
        x2, y2 = rotate(90, 0, angle)
        pygame.draw.line(screen, white, (cx + x1, cy + y1), (cx + x2, cy + y2), 2)

        x, y = rotate(120, 0, angle)
        pygame.draw.circle(screen, fill_color, (int(cx + x), int(cy + y)), 15)
        pygame.draw.circle(screen, white, (int(cx + x), int(cy + y)), 15, 2)

        angle += math.radians(30)

    for _ in range(18):
        for dy in [-30, 30]:
            x1, y1 = rotate(67.5, dy, angle)
            x2, y2 = rotate(105, 0, angle)
            pygame.draw.line(screen, white, (cx + x1, cy + y1), (cx + x2, cy + y2), 2)
        angle += math.radians(20)



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    scene = generate_scene()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        screen.fill((10, 5, 100))

        draw_scene(screen, scene)
        draw_snowflake(screen, WIDTH // 2, HEIGHT // 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()