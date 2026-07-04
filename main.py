import py5
import math
import random

def setup():
    py5.size(800, 800)
    py5.circle(80, 0, 20)

    py5.background(10,5,100)
    py5.translate(py5.width / 2, py5.height / 2)

    draw_snowflake()
    draw_scene()


def draw_scene():
    py5.scale(-1)
    py5.rotate(math.radians(60))

    py5.stroke(150, 150, 200)
    py5.fill(100, 100, 150)

    for i in range(1000):

        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)

        d = py5.dist(x, y, 0, 0)

        chance = (d / 400) ** 2

        if random.random() < chance:
            size = 2 + 4 * (d / 400)
            py5.circle(x, y, size)

def draw():
    pass


def draw_snowflake():

    py5.stroke(255)
    py5.stroke_weight(2)

    py5.rotate(math.radians(-60))

    py5.fill(100, 100, 150)

    for i in range(6):
        py5.line(0, 0, 225, 0)

        py5.line(15, -30, 60, 0)
        py5.line(15,  30, 60, 0)

        py5.line(120, 0, 150, -22.5)
        py5.line(120, 0, 150, 22.5)

        py5.line(135, 0, 165, -22.5)
        py5.line(135, 0, 165, 22.5)

        py5.line(150, 0, 180, -22.5)
        py5.line(150, 0, 180, 22.5)

        py5.circle(225, 0, 30)

        py5.rotate(math.radians(30))

        py5.line(30, 0, 90, 0)
        py5.circle(120, 0, 30)

        py5.rotate(math.radians(30))


    for i in range(18):
        py5.line(67.5, -30, 105, 0)
        py5.line(67.5,  30, 105, 0)

        py5.rotate(math.radians(20))

py5.run_sketch()
