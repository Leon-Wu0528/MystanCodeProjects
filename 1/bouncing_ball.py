"""
File: 
Name:
-------------------------
TODO:
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
ball = GOval(SIZE, SIZE)
activate = True
n = 1

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bouncing)


def bouncing(mouse):
    global activate, n
    vy = 0
    if activate:
        activate = False
        while True:
            while n <= 3:
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y >= window.height:
                    speed = -0.9 * vy
                    vy = speed + GRAVITY
                    ball.move(VX, vy)
                    if ball.x > window.width:
                        ball.x = START_X
                        ball.y = START_Y
                        n += 1
                        break
                pause(DELAY)
            break
        activate = True








if __name__ == "__main__":
    main()
