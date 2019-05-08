from PIL import Image
from PIL import ImageOps
import image_utils

User_choose = input('(f)ilter an image or (q)uit ')
while User_choose.upper() != 'Q':
    if User_choose.upper() == 'F':
        Output_GUI = '▪ (p)ixelate \n'+'▪ (k)aleidoscope \n'+'▪ (g)ray-day \n'+'▪ (r)ighty \n'
        img_path = input('what is the image path ?')
        img = Image.open(img_path)
        print(Output_GUI)
        User_input = input()
        User_input = User_input.upper()
        for i in User_input:
            if i == 'K':
                img = image_utils.image_Kaleidoscope(img, img.size[0], img.size[1])
            elif i == 'P':
                img = image_utils.image_pixelate(img, img.size[0], img.size[1], 10)
            elif i == 'G':
                img = image_utils.image_Gray_day(img,img.size[0], img.size[1])
            elif i == 'R':
                img = image_utils.image_Righty(img)

        img.show()
    else:
        User_choose = input('(f)ilter an image or (q)uit ')
    User_choose = input('(f)ilter an image or (q)uit ')