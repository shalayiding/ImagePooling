import cv2
import numpy as np
from polling_functions import Polling




im = cv2.imread('Lenna_test.png')

cv2.imshow('orginal_img',im)
im_width = im.shape[0]
im_height = im.shape[1]
new_im = Polling(im, im_width,im_height,4,4,'egien')

cv2.imshow('new_img',new_im)
cv2.imwrite('Max_egien_value.png', new_im)
cv2.waitKey(0)