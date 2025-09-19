import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)

screen.bgcolor('gray')

turtle.speed(0)
turtle.hideturtle()
turtle.colormode(1) 
turtle.pensize(3)

def draw_spiral(x, y, r, direction, hue, use_black_fill):
    if r < 5:
        return
    line_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0) 
    turtle.pencolor(line_color)
    if use_black_fill:
        turtle.fillcolor('black')
    else:
        turtle.fillcolor('white')
    r2 = r * math.cos(math.radians(36)) / math.cos(math.radians(36 - alpha))
    turtle.up()
    px = x + r * math.cos(math.radians(direction))
    py = y + r * math.sin(math.radians(direction))
    turtle.goto(px, py)
    turtle.down()
    turtle.begin_fill()

    current_direction = direction + 360 / 5
    for _ in range(5):
        px = x + r * math.cos(math.radians(current_direction))
        py = y + r * math.sin(math.radians(current_direction))
        turtle.goto(px, py)
        current_direction += 360 / 5
    
    turtle.end_fill()
    draw_spiral(x, y, r2, direction + alpha, (hue + 0.025) % 1.0, not use_black_fill)

alpha = 3
draw_spiral(0, 0, 900, 90, 0.0, True)

screen.mainloop()