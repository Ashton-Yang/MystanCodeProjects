"""
File: bouncing_ball
Name: Ashton Yang
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
clicked = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    create_ball()
    onmouseclicked(execute)


def create_ball():
    global ball
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = 'black'
    ball.color = 'black'
    window.add(ball)


def execute(mouse):
    # Click the mouse to start the animation.
    global clicked
    if not clicked:
        clicked = True
        animation()
        create_ball()
        clicked = False


def animation():
    # Simulates the bouncing ball.
    global ball
    vy = 0
    while True:
        ball.move(VX, vy)
        vy += GRAVITY
        pause(DELAY)
        if ball.y + ball.height >= window.height:
            vy *= -REDUCE
        if ball.x > window.width:
            break


if __name__ == "__main__":
    main()
