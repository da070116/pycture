from graph import * 


def draw_angry_face(x, y, radius:int):
    """ Function draws an angry face using standard primitives"""
    draw_circle(x, y, radius=radius)
    draw_eye(x-radius//2, y-radius//4, radius=15*radius//100)
    draw_eye(x+radius//2, y-radius//4, radius=15*radius//100)
    penColor(0, 0, 0)
    penSize(5)
    arc(x-radius//2, y+radius//5, x+radius//2, y+radius, 0, 180, ARC)


def draw_circle(x, y, *, radius:int):
    penSize(0)
    brushColor("red")
    circle(x, y, radius)
    

def draw_eye(x, y, radius):
    x1 = x - 2*radius
    x2 = x + 2*radius
    y1 = y - radius
    y2 = y + radius
    brushColor(255, 255, 255)
    oval(x1, y1, x2, y2)
    brushColor(0, 200, 0)
    circle(x, y, radius)
    penSize(radius//3)
    brushColor(0, 0, 0)
    circle(x, y, radius//3)

    brow_x1 = x1
    brow_y1 = y1 - radius
    brow_x2 = x2
    brow_y2 = y2 - radius
    arc(brow_x1, brow_y1, brow_x2, brow_y2, 10, 160, ARC)
    penSize(0)

    
def draw_triangle(x, y, /, *, width: int, height: int,  color: tuple, border: int = 0):
    """ 
        Draw a triangle at point (x, y) 
        with defined width and height,
        color and border
    """
    penColor(0, 0, 0)
    if color == (255, 255, 255):
        penSize(1) 
    elif not border == 0:
        penSize(border)

    points_list = [(x, y), (x, y + height), (x + width, y + height), (x, y)]
    brushColor(color)
    polygon(points_list)


if __name__ == '__main__':

    center_x, center_y = [int(i/2) for i in canvasSize()]
    draw_angry_face(center_x, center_y, 60)
   
    run()
