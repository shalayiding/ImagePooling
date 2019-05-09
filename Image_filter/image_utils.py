from PIL import Image
from PIL import ImageOps

def image_pixelate(img, orginal_width, orginal_height, Pooling_size):
    pix = img.load()
    for x in range(0, orginal_width, 10):
        for y in range(0, orginal_height, 10):
            temp = pix[x, y]
            for w in range(0, 10):
                for h in range(0, 10):
                    if w+x < orginal_width and h+y <orginal_height:
                        pix[w + x, h + y] = temp
    return img

def image_Kaleidoscope(img,orginal_width, orginal_height):
    filter_width = int(orginal_width / 2)
    filter_height = int(orginal_height / 2)

    im_left_bot = ImageOps.mirror(img)
    im_right_bot = img.resize((filter_width, filter_height), Image.ANTIALIAS)
    im_left_bot = im_left_bot.resize((filter_width, filter_height), Image.ANTIALIAS)
    im_left_top = im_left_bot.rotate(180)
    im_right_top = im_right_bot.rotate(180)

    img.paste(im_right_top, (0, 0))
    img.paste(im_left_top, (filter_width, 0))
    img.paste(im_right_bot, (0, filter_height))
    img.paste(im_left_bot, (filter_width, filter_height))

    return img


def image_Gray_day(img,orginal_width,orginal_height):
    pix = img.load()
    for x in range(0, orginal_width):
        for y in range(0, orginal_height):
            Gray = (pix[x,y][0] + pix[x,y][1] + pix[x,y][2]) / 3
            pix[x,y]=(int(Gray),int(Gray),int(Gray))
    return img


def image_Righty(img):
    img = img.rotate(270)
    return img