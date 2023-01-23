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
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        self.__dx = 0
        self.__dy = 0

        self.activate = True # 球在動的時候點按無效
        self.activate_1 = True # 球被reset的時候不動，滑鼠點按才開始動
        self.bricks = brick_cols * brick_rows
        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.paddle_move)
        self.draw_bricks()

        # Default initial velocity for the ball
    def handle_click(self, mouse):
        if self.activate: # 球在動的時候點按無效
            self.activate = False
            self.set_ball_velocity()
            self.activate_1 = True


    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx


    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width * 2) / 2
        self.ball.y = (self.window.height - self.ball.height * 2) / 2
        self.window.add(self.ball)
        self.activate = True
        self.__dx = 0
        self.__dy = 0



    def paddle_move(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

        # Draw bricks
    def draw_bricks(self, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_spacing=BRICK_SPACING, brick_offset=BRICK_OFFSET):
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=0+j*(brick_width+brick_spacing), y=brick_offset+i*(brick_height+brick_spacing))
                brick.filled = True
                if i < 2:
                    brick.fill_color = 'red'
                elif i < 4:
                    brick.fill_color = 'orange'
                elif i < 6:
                    brick.fill_color = 'yellow'
                elif i < 8:
                    brick.fill_color = 'green'
                elif i < 10:
                    brick.fill_color = 'blue'
                self.window.add(brick)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx
        return self.__dx
    def set_dy(self):
        self.__dy = -self.__dy
        return self.__dy

    def remove(self):
        maybe_obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_obj_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        maybe_obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if maybe_obj_1 is not None: # 以免點到空白會跳錯
            if maybe_obj_1 is not self.paddle:
                self.bricks -= 1
                self.window.remove(maybe_obj_1)
                self.set_dy()
            else:
                if self.get_dy()>0:
                    self.set_dy()

        elif maybe_obj_2 is not None: # 以免點到空白會跳錯
            if maybe_obj_2 is not self.paddle:
                self.bricks -= 1
                self.window.remove(maybe_obj_2)
                self.set_dy()
            else:
                if self.get_dy() > 0:
                    self.set_dy()

        elif maybe_obj_3 is not None: # 以免點到空白會跳錯
            if maybe_obj_3 is not self.paddle:
                self.bricks -= 1
                self.window.remove(maybe_obj_3)
                self.set_dy()
            else:
                if self.get_dy() > 0:
                    self.set_dy()

        elif maybe_obj_4 is not None:  # 以免點到空白會跳錯
            if maybe_obj_4 is not self.paddle:
                self.bricks -= 1
                self.window.remove(maybe_obj_4)
                self.set_dy()
            else:
                if self.get_dy() > 0:
                    self.set_dy()
