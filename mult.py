# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def mult_matrix(a, b):
    rows_a = a.shape[0]
    cols_a = a.shape[1]
    cols_b = b.shape[1]
    #rows_b = cols_a
    c = np.zeros(shape=(rows_a, cols_b))
    for i in range(rows_a):
        for j in range(cols_b):
            for p in range(cols_a): 
                c[i, j] = c[i, j] + a[i, p] * b[p, j] 
    return c

def main():
    a = np.array([[5, 8, 7], [1, 2, 3]])
    b = np.array([[1, 2, 11], [3, 4, 12], [5, 6, 13]])
    c = mult_matrix(a, b)
    print(c)
    #print (np.matmul(a, b)) #בדיקה


if __name__ == "__main__": 
    main()        

    