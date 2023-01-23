"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    num_lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.bricks != 0: # 若沒磚塊了 停止
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.remove()

            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0:
                graphics.set_dy()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                num_lives -= 1
                if num_lives == 0:
                    # break
                    pass
                else:
                    graphics.activate = True
                    graphics.reset_ball()
        else:
            break







if __name__ == '__main__':
    main()
