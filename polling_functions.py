import cv2
import numpy as np
from numpy import linalg as LA




def Polling(img, width, height, Polling_w, Polling_h , P_mode):
    for h in range(0, height,Polling_h):
        for w in range(0,width,Polling_w):
            if img.size - (h*w) > (Polling_w*Polling_h):
                R_matrix = []
                G_matrix = []
                B_matrix = []
                for ph in range(0,Polling_h):
                    R_matrix.append([])
                    G_matrix.append([])
                    B_matrix.append([])
                    for pw in range(0,Polling_w):
                        R_matrix[ph].append(img[w+pw,h+ph][0])
                        G_matrix[ph].append(img[w+pw,h+ph][1])
                        B_matrix[ph].append(img[w+pw,h+ph][2])
                if P_mode == 'max':
                    temp = Matrix_Max(R_matrix, G_matrix, B_matrix)

                if P_mode == 'egien':
                    temp = Matrix_Egien(R_matrix, G_matrix, B_matrix)
                for ph in range(0,Polling_h):
                    for pw in range(0, Polling_w):
                        img[pw+w,ph+h] = temp
            else :
                pass
    return img

def Matrix_Egien(R_matrix, G_matrix, B_matrix):
    R_e_vals, R_e_vecs = LA.eig(R_matrix)
    G_e_vals, G_e_vecs = LA.eig(G_matrix)
    B_e_vals, B_e_vecs = LA.eig(B_matrix)
    RGB_matrix = [0,0,0]
    RGB_matrix[0] = round(max(R_e_vals))
    RGB_matrix[1] = round(max(G_e_vals))
    RGB_matrix[2] = round(max(B_e_vals))
    return RGB_matrix


def Matrix_Max(R_matrix, G_matrix, B_matrix):
    RGB_matrix = [0, 0, 0]
    RGB_matrix[0] = max(R_matrix[0]);
    RGB_matrix[1] = max(G_matrix[0]);
    RGB_matrix[2] = max(B_matrix[0]);

    for value in R_matrix:
        if max(value) >  RGB_matrix[0]:
            RGB_matrix[0] =max(value)

    for value in G_matrix:
        if max(value) > RGB_matrix[1]:
            RGB_matrix[1] = max(value)

    for value in B_matrix:
        if max(value)>RGB_matrix[2]:
            RGB_matrix[2] = max(value)

    return RGB_matrix


def Matrix_Average(R_matrix, G_matrix, B_matrix):
    pass
