"""
File: 
Name:吳竹孟
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550
SIZE = 10
n = 0
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Draw Lines')
circle = GOval(SIZE, SIZE)




def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_lines)




def draw_lines(mouse):
    global circle
    global n
    if n % 2 == 0:
        circle = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        window.add(circle)
    else: # 點偶數次
        line = GLine(circle.x-SIZE/2,circle.y-SIZE/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
    n += 1




if __name__ == "__main__":
    main()
