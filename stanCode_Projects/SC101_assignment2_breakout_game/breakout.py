"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
Name: Ashton Yang
"""


from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

switch = False           # 判斷球是否連續2次撞到paddle
score = 0                # 消滅的磚塊數量


def main():
    global score
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)
        rebound_x(graphics, vx)
        rebound_y(graphics, vy)
        check_for_collisions(graphics, vx, vy)
        pause(FRAME_RATE)
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            graphics.reset_dx()
            graphics.reset_dy()
            graphics.set_ball_position()
        if lives == 0:
            break
        if score == graphics.brick_counts:
            break


def rebound_x(graphics, vx):
    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
        global switch
        vx = graphics.rebound_dx()
        switch = False
    return vx


def rebound_y(graphics, vy):
    if graphics.ball.y <= 0:
        global switch
        vy = graphics.rebound_dy()
        switch = False
    return vy


def check_for_collisions(graphics, vx, vy):
    global switch, score
    ball_top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    ball_top_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
    ball_bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
    ball_bottom_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                      graphics.ball.y + graphics.ball.height)
    obj = ball_top_left or ball_top_right or ball_bottom_left or ball_bottom_right
    if obj is not None and obj is not graphics.paddle:
        switch = False
        graphics.window.remove(obj)
        score += 1
        vy = graphics.rebound_dy()
    # the ball hits the paddle top.
    if ball_bottom_left is graphics.paddle:
        if graphics.paddle.x <= graphics.ball.x <= graphics.paddle.x + graphics.paddle.width:
            if graphics.paddle.y <= graphics.ball.y + graphics.ball.height < graphics.paddle.y+graphics.paddle.height:
                if switch is False:
                    vy = graphics.rebound_dy()
                    switch = True
    elif ball_bottom_right is graphics.paddle:
        if graphics.paddle.x <= graphics.ball.x + graphics.ball.width <= graphics.paddle.x + graphics.paddle.width:
            if graphics.paddle.y <= graphics.ball.y + graphics.ball.height < graphics.paddle.y+graphics.paddle.height:
                if switch is False:
                    vy = graphics.rebound_dy()
                    switch = True
    # the ball hits the left side of the paddle
    elif ball_top_right is graphics.paddle:
        if graphics.ball.y >= graphics.paddle.y:
            if graphics.ball.x + graphics.ball.width >= graphics.paddle.x and vx > 0:
                if switch is False:
                    vx = graphics.rebound_dx()
                    switch = True
    elif ball_bottom_right is graphics.paddle:
        if graphics.ball.y + graphics.ball.height >= graphics.paddle.y:
            if graphics.ball.x + graphics.ball.width >= graphics.paddle.x and vx > 0:
                if switch is False:
                    vx = graphics.rebound_dx()
                    switch = True
    # the ball hits the right side of the paddle:
    elif ball_top_left is graphics.paddle:
        if graphics.ball.y > graphics.paddle.y:
            if graphics.ball.x <= graphics.paddle.x + graphics.paddle.width and vx < 0:
                if switch is False:
                    vx = graphics.rebound_dx()
                    switch = True
    elif ball_bottom_left is graphics.paddle:
        if graphics.ball.y + graphics.ball.height > graphics.paddle.y:
            if graphics.ball.x <= graphics.paddle.x + graphics.paddle.width and vx < 0:
                if switch is False:
                    vx = graphics.rebound_dx()
                    switch = True
    return vx and vy


if __name__ == '__main__':
    main()
