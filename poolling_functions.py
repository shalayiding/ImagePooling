import cv2
import numpy as np
from numpy import linalg as LA




def Poolling(img, width, height, Polling_w, Polling_h , P_mode):
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
                if P_mode == 'eigen':
                    temp = Matrix_Eigen(R_matrix, G_matrix, B_matrix)
                if P_mode == 'ave':
                    temp = Matrix_Average(R_matrix, G_matrix, B_matrix)
                if P_mode =='relation_eigen':
                    R_relation_matrix = Matrix_absolute_Relation(R_matrix)
                    G_relation_matrix = Matrix_absolute_Relation(G_matrix)
                    B_relation_matrix = Matrix_absolute_Relation(B_matrix)
                    temp = Matrix_Eigen(R_relation_matrix,G_relation_matrix,B_relation_matrix)

                for ph in range(0,Polling_h):
                    for pw in range(0, Polling_w):
                        img[pw+w,ph+h] = temp
            else :
                pass
    return img


def Matrix_Eigen(R_matrix, G_matrix, B_matrix): #return RGB_matrix or array of the max element
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
    RGB_matrix[0] = max(R_matrix[0])
    RGB_matrix[1] = max(G_matrix[0])
    RGB_matrix[2] = max(B_matrix[0])

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


def Matrix_Average(R_matrix, G_matrix, B_matrix):#find the average value of the matrix and round it

    RGB_matrix = [0, 0, 0]
    RGB_matrix[0] = round(np.average(R_matrix))
    RGB_matrix[1] = round(np.average(G_matrix))
    RGB_matrix[2] = round(np.average(B_matrix))

    return RGB_matrix


def Matrix_absolute_Relation(R_matrix): # find the relation matrix of the given matrix
    R_arr_abso = []
    for row1 in R_matrix:
        for col1 in row1:
            for row2 in R_matrix:
                for col2 in row2:
                    if col2 - col1 < 0:
                        R_arr_abso.append(-1*(col2-col1))
                    else:
                        R_arr_abso.append(col2-col1)
    R_matrix_abso =[]
    for row in range(0,len(R_arr_abso),len(R_matrix)*len(R_matrix[0])):
        s=[]
        for cols in range(len(R_matrix)*len(R_matrix[0])):
            s.append(R_arr_abso[cols+row])
        R_matrix_abso.append(s)

    return R_matrix_abso