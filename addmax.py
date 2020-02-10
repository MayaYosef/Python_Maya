# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:38:56 2020

@author: micha
"""

import numpy as np

def add_max_matrix(a, b):
    rows_a = a.shape[0] #מטאפל
    cols_a = a.shape[1]
    rows_b = b.shape[0]
    cols_b = b.shape[1]
    rows = rows_a
    if rows_a < rows_b: #רוצים הפעם מקסימלי!! לשים לב בתנאי
        rows = rows_b
    cols = cols_a
    if cols_a < cols_b:
        cols = cols_b
    if rows_a < rows:
        for i in range(rows-rows_a):
            a = np.insert(a, rows_a, 0, axis = 0)
            rows_a=+1
    if rows_b < rows:
        for i in range(rows-rows_b):
            b = np.insert(b, rows_b, 0, axis = 0)
            rows_b=+1
    if cols_a < cols:
        for i in range(cols-cols_a):
            a = np.insert(a, cols_a, 0, axis = 1)
            cols_a=+1
    if cols_b < cols:
        for i in range(cols-cols_b):
            b = np.insert(b, cols_b, 0, axis = 1)
            cols_b=+1                
    c = np.zeros(shape=(rows, cols)) 
    for i in range(rows):
        for j in range(cols):
            c[i, j] = a[i, j] + b[i, j]    
    return c

def main():
    a = np.array([[5, 8, 7], [1, 2, 3]])
    b = np.array([[1, 2, 11], [3, 4, 12], [5, 6, 13]])
    c = add_max_matrix(a, b)
    print(c)


if __name__ == "__main__": 
    main()        
