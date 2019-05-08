import cv2
import numpy as np
from polling_functions import Polling




im = cv2.imread('Lenna_test.png')
im_width = im.shape[0]
im_height = im.shape[1]
new_im = Polling(im, im_width,im_height,32,32,'max')

cv2.imshow('new_img',new_im)
cv2.waitKey(0)