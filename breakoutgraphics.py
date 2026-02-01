"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.ball_radius = ball_radius
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.y = window_height - paddle_offset - paddle_height
        self.paddle.x = (window_width - paddle_width)/2
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.x = window_width/2 - ball_radius
        self.ball.y = window_height/2 - ball_radius
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)



        # Default initial velocity for the ball

        self.__dx = 0
        self.__dy = 0
        # 綁定點擊事件
        onmouseclicked(self.start_game)
        # Initialize our mouse listeners
        onmousemoved(self.reset_paddle)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.x = (brick_width + brick_spacing) * j
                brick.y = (brick_height + brick_spacing) * i + brick_offset
                brick.filled = True
                if i < 2:
                    brick.fill_color = 'red'
                elif i < 4 :
                    brick.fill_color = 'orange'
                elif i < 6:
                    brick.fill_color = 'yellow'
                elif i < 8:
                    brick.fill_color = 'green'
                elif i < 10:
                    brick.fill_color = 'blue'

                self.window.add(brick)
        # 計分版：
        self.lives_label = GLabel('Lives: 3')
        self.lives_label.font = '-20'
        self.window.add(self.lives_label, x=10, y=self.lives_label.height + 10)



    def start_game(self, event):
        if self.__dy == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            # 隨機決定往左還是往右噴 (50% 機率)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_paddle (self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x + self.paddle.width>= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x <= 0:
            self.paddle.x = 0
    def reset_ball(self):
        self.__dx = 0
        self.__dy = 0
        self.ball.x = self.window.width / 2 - self.ball_radius
        self.ball.y = self.window.height / 2 - self.ball_radius

    def set_lives(self, new_lives):
        self.lives_label.text = 'Lives: ' + str(new_lives)

    def draw_end_message(self, message):
        label = GLabel(message)
        label.font = '-40'
        label.x = (self.window.width - label.width) / 2
        label.y = (self.window.height + label.ascent) / 2
        self.window.add(label)



