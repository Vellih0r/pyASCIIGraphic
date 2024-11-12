from PIL import Image
import numpy as np

gradient = ".:!/r(l1Z4H9W8$@"

# anme to create txt, x - side of image
def draw(name, namefile, x):
    # get and resize image
    size = (x, x)
    
    im = Image.open(name)

    im = im.resize(size)
    iar = np.asarray(im)
    height = len(iar)
    width = len(iar)

    # Create map with brightness of each pixel
    brightness = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            r = int(iar[i][j][0])
            g = int(iar[i][j][1])
            b = int(iar[i][j][2])
            brightness[i][j] = 0.21 * r + 0.72 * g + 0.07 * b

    # Drawing with borders
    border_char = '#' # char to draw border


    # with open(namefile, 'w') as file:
    #     file.write(border_char * (width + 2))  # top border
    #     for i in brightness: 
    #         file.write(border_char + border_char) # left border
    #         for j in i:
    #             x = int(j//11.25)
    #             # if number is too big of too small - just validate it
    #             if x > 15:
    #                 x = 15
    #             elif x < 0:
    #                 x = 0
    #             ch = gradient[x]
    #             # write image in txt
    #             file.write(ch)
    #         file.write(border_char + border_char)  # right border
    #         file.write('\n')
            
    #     file.write(border_char * (width + 2))  # bottom border


    # draw image into console

    print(border_char * (width + 4))  # top border
    for i in brightness:
        print(border_char + border_char, end='')  # left border
        for j in i:
            x = int(j / 11.25)
            if x > 15:
                x = 15
            elif x < 0:
                x = 0
            ch = gradient[x]
            print(ch, end='')
        print(border_char + border_char)  # right border

    print(border_char * (width + 4))  # bottiom border

draw('nm3.png', 'output.txt', 100)