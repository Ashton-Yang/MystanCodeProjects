"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
Name: Ashton Yang
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 3    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # counts the number of bricks
        self.brick_counts = brick_rows * brick_cols
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.set_ball_position()
        self.window.add(self.ball)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=j*(brick_width+brick_spacing),
                                   y=brick_offset+i*(brick_height+brick_spacing))
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                elif i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                elif i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                elif i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                elif i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)
        #   Control paddle
        onmousemoved(self.move_paddle)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width)/2
        self.ball.y = (self.window.height - self.ball.height)/2

    def move_paddle(self, mouse):
        self.paddle.x = (mouse.x - self.paddle.width / 2)
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def set_ball_velocity(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
        # self.ball.move(self.__dx, self.__dy)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_dx(self):
        self.__dx = 0
        return self.__dx

    def reset_dy(self):
        self.__dy = 0
        return self.__dy

    def rebound_dx(self):
        self.__dx = -self.__dx

    def rebound_dy(self):
        self.__dy = -self.__dy



