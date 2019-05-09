# ImagePooling
# Different type of pooling methods
### Basic setup 
First we have to divide image to the n matrix size of the matrix should be (m*m) we are storing all the value to the R_matrix , G_matrix, B_matrix since we have 3 channle and we are sending this matrix to the different function to process the matrix.


    def Poolling(img, width, height, Polling_w, Polling_h, P_mode):
        for h in range(0, height, Polling_h):
            for w in range(0, width, Polling_w):
                if img.size - (h * w) > (Polling_w * Polling_h):
                    R_matrix = []
                    G_matrix = []
                    B_matrix = []
                    for ph in range(0, Polling_h):
                        R_matrix.append([])
                        G_matrix.append([])
                        B_matrix.append([])
                        for pw in range(0, Polling_w):
                            R_matrix[ph].append(img[w + pw, h + ph][0])
                            G_matrix[ph].append(img[w + pw, h + ph][1])
                            B_matrix[ph].append(img[w + pw, h + ph][2])
                    if P_mode == 'max':
                        temp = Matrix_Max(R_matrix, G_matrix, B_matrix)
                    if P_mode == 'eigen':
                        temp = Matrix_Eigen(R_matrix, G_matrix, B_matrix)
                    if P_mode == 'ave':
                        temp = Matrix_Average(R_matrix, G_matrix, B_matrix)

                    for ph in range(0, Polling_h):
                        for pw in range(0, Polling_w):
                            img[pw + w, ph + h] = temp
                else:
                    pass
        return img


Orginal Image:![Orginal Image](https://github.com/shalayiding/ImagePooling/blob/master/Lenna_test.png)
1.##Max Pooling 👍 
In max pooling we picking up the max number from the Pooling box in this case it will be 4 * 4 pixels matrix,forexample we are picking up the value 163 from 1 channle.
![Max Poolling](https://github.com/shalayiding/ImagePooling/blob/master/wiki%20source/max_explian.PNG)

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

Result : 
![Max Pooling Result](https://github.com/shalayiding/ImagePooling/blob/master/max_value.png)

2.##Average Poolling 👍 
In the Average poolling we are adding all the pixels and divide by the matrix size.

    def Matrix_Average(R_matrix, G_matrix, B_matrix):
    
        RGB_matrix = [0, 0, 0]
        RGB_matrix[0] = round(np.average(R_matrix))
        RGB_matrix[1] = round(np.average(G_matrix))
        RGB_matrix[2] = round(np.average(B_matrix))
    
        return RGB_matrix


Result : ![Average image pooling](https://github.com/shalayiding/ImagePooling/blob/master/average_value.png)

3.##Max Eigen value Poolling 👍 
we are looking for the max eigen value of the matrix.

    def Matrix_Eigen(R_matrix, G_matrix, B_matrix):
        R_e_vals, R_e_vecs = LA.eig(R_matrix)
        G_e_vals, G_e_vecs = LA.eig(G_matrix)
        B_e_vals, B_e_vecs = LA.eig(B_matrix)
        RGB_matrix = [0,0,0]
        RGB_matrix[0] = round(max(R_e_vals))
        RGB_matrix[1] = round(max(G_e_vals))
        RGB_matrix[2] = round(max(B_e_vals))
        return RGB_matrix

Result : ![Eigen image pooling](https://github.com/shalayiding/ImagePooling/blob/master/max_eigen_value.png)






