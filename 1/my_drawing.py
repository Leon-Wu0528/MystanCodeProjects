"""
File: 
Name:吳竹孟
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My Best Friend
    他總能在我無助的時候陪伴我，從來沒有一句怨言。
    """
    window = GWindow(width=800, height=500, title='MyFace')
    face = GOval(230, 250, x=300, y=150)
    face.filled = True
    face.fill_color = 'white'

    r_eye = GOval(30, 30, x=440, y=220)
    r_eye.filled = True
    r_eye.fill_color = 'brown'

    l_eye = GOval(30, 30, x=360, y=220)
    l_eye.filled = True
    l_eye.fill_color = 'brown'

    r_blush = GOval(50, 50, x=465, y=245)
    r_blush.filled = True
    r_blush.fill_color = 'pink'

    l_blush = GOval(50, 50, x=315, y=245)
    l_blush.filled = True
    l_blush.fill_color = 'pink'

    up_mouth =  GOval(40, 25, x=395, y=210)
    up_mouth.filled = True
    up_mouth.fill_color = 'yellow'

    down_mouth =  GOval(30, 20, x=400, y=235)
    down_mouth.filled = True
    down_mouth.fill_color = 'yellow'

    r_hand = GOval(40, 30, x=260, y=275)
    r_hand.filled = True
    r_hand.fill_color = 'white'

    l_hand = GOval(40, 30, x=530, y=275)
    l_hand.filled = True
    l_hand.fill_color = 'white'

    r_feet = GOval(40, 30, x=470, y=375)
    r_feet.filled = True
    r_feet.fill_color = 'white'

    l_feet = GOval(40, 30, x=320, y=375)
    l_feet.filled = True
    l_feet.fill_color = 'white'


    window.add(face)
    window.add(l_eye)
    window.add(r_eye)
    window.add(l_blush)
    window.add(r_blush)
    window.add(up_mouth)
    window.add(down_mouth)
    window.add(r_hand)
    window.add(l_hand)
    window.add(l_feet)
    window.add(r_feet)




if __name__ == '__main__':
    main()
