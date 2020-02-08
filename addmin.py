# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:44:10 2020

@author: micha
"""

import numpy as np

def add_min_matrix(a, b):
    rows_a = a.shape[0] #מטאפל
    cols_a = a.shape[1]
    rows_b = b.shape[0]
    cols_b = b.shape[1]
    rows = rows_a
    if rows_a > rows_b: #רוצים מינימלי!! לשים לב בתנאי
        rows = rows_b
    cols = cols_a
    if cols_a > cols_b:
        cols = cols_b
    a = a[0:rows, 0:cols]    
    b = b[0:rows, 0:cols]
    c = np.zeros(shape=(rows, cols)) 
    for i in range(rows):
        for j in range(cols):
            c[i, j] = a[i, j] + b[i, j]    
    return c

def main():
    a = np.array([[5, 8, 7], [1, 2, 3]])
    b = np.array([[1, 2], [3, 4], [5, 6]])
    c = add_min_matrix(a, b)
    print(c)


if __name__ == "__main__": 
    main()        
