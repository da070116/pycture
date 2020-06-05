from pycture.graph import *


def draw_angry_smile():
    """ Function draws an angry smile using standard primitives"""
    print('once there will be a picture')


def test():
    penColor(255,0,255)
    penSize(5)
    brushColor("blue")
    rectangle(100, 100, 300, 200)
    


def draw_triangle(x,y, /, *, width: int, height: int,  color: tuple, border: int = 0):
    """ Draw a triangle at point x, y """
    penSize(border)
    if border == 0 and color == (255,255,255):
        penSize(1)
        penColor(0, 0, 0)
    points_list = [(x, y), (x, y+height), (x+width, y+height), (x, y)]
    brushColor(color)
    polygon(points_list)


if __name__ == '__main__':
    brushColor(255, 225, 0)
    penSize(0)
    rectangle(0, 0, 220, 420)
    draw_triangle(10, 10, width=100, height=200, color=(0, 0, 0), border=3)
    draw_triangle(110, 10, width=100, height=200, color=(0, 0, 0), border=3)
    draw_triangle(110, 210, width=100, height=200, color=(0, 0, 0), border=3)
    run()
