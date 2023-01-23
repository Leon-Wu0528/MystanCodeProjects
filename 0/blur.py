"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""
#圖片長寬都是300
from simpleimage import SimpleImage

def blur(old_img):
    """
    :param img:
    :return:
    """
    # old_img = SimpleImage(filename)
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):  # 寬有幾個pixel
        for y in range(old_img.height):  # 高有幾個pixel
            r_sum = 0
            b_sum = 0
            g_sum = 0
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = x + i
                    neighbor_y = y + i
                    if 0 <= neighbor_x < old_img.width:
                        if 0 <= neighbor_y < old_img.height:
                            old_pixel = old_img.get_pixel(neighbor_x, neighbor_y)
                            r_sum += old_pixel.red
                            b_sum += old_pixel.blue
                            g_sum += old_pixel.green
                            count += 1
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.blue = b_sum / count
            new_pixel.green = g_sum / count
    return new_img




def main():
    """
    TODO:
    """

    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
