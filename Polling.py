import cv2
import numpy as np
from poolling_functions import Poolling

im = cv2.imread('Lenna_test.png')

cv2.imshow('orginal_img',im)
im_width = im.shape[0]
im_height = im.shape[1]
P_mode = 'max'
new_im = Poolling(im, im_width,im_height,4,4,P_mode)

cv2.imshow('new_img',new_im)
if P_mode =='ave':
    cv2.imwrite('result_img/average_value.png', new_im)
elif P_mode == 'max':
    cv2.imwrite('result_img/max_value.png', new_im)
elif P_mode =='eigen':
    cv2.imwrite('result_img/max_eigen_value.png', new_im)

cv2.waitKey(0)